# React UI — Food Delivery Analysis Dashboard

**Date:** 2026-05-19  
**Status:** Approved  
**Model used for architecture:** claude-opus-4-7

---

## Overview

Add a full interactive web app to the existing food delivery analysis pipeline. Users upload a CSV, the app runs the full Python pipeline, and displays results across five pages in a dark-themed React dashboard.

---

## Architecture

Two new top-level directories added. Existing `src/` is untouched except for one small addition to `sql_runner.py`.

```
food-delivery-analysis/
├── api/                          # FastAPI backend
│   ├── main.py                   # app, CORS, route registration
│   ├── routes/
│   │   ├── __init__.py
│   │   └── analysis.py           # POST /api/analyze, GET /api/health
│   ├── services/
│   │   ├── __init__.py
│   │   └── pipeline.py           # wraps src/ modules, returns AnalysisResult
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── analysis.py           # Pydantic request/response models
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py             # MAX_UPLOAD_BYTES, ALLOWED_EXT, CORS origins
│   │   └── errors.py             # AppError, exception handlers
│   ├── tests/
│   │   ├── test_pipeline.py
│   │   └── test_routes.py
│   └── requirements.txt
│
├── ui/                           # React + Vite + TypeScript frontend
│   ├── index.html
│   ├── vite.config.ts            # proxy /api → http://localhost:8000
│   ├── tsconfig.json
│   ├── package.json
│   └── src/
│       ├── main.tsx
│       ├── App.tsx               # Router + AnalysisProvider
│       ├── routes.tsx
│       ├── api/
│       │   └── client.ts         # fetch wrapper, uploadCsv(file)
│       ├── state/
│       │   └── AnalysisContext.tsx  # Context + reducer for single result
│       ├── types/
│       │   └── analysis.ts       # TypeScript mirrors of Pydantic shapes
│       ├── pages/
│       │   ├── UploadPage.tsx
│       │   ├── OverviewPage.tsx
│       │   ├── ChartsPage.tsx
│       │   ├── MLResultsPage.tsx
│       │   └── SQLResultsPage.tsx
│       ├── components/
│       │   ├── layout/
│       │   │   ├── AppShell.tsx  # dark shell with sidebar
│       │   │   └── NavTabs.tsx   # tab nav, disables tabs until result loaded
│       │   ├── upload/
│       │   │   ├── Dropzone.tsx  # react-dropzone, .csv only
│       │   │   └── RunButton.tsx # disabled until file selected, spinner while loading
│       │   ├── kpi/
│       │   │   └── KpiCard.tsx   # label + value + unit
│       │   ├── charts/
│       │   │   ├── PeakHourChart.tsx   # Recharts LineChart, shaded peak zone 19-22
│       │   │   └── CityDemandChart.tsx # Recharts BarChart sorted desc
│       │   ├── ml/
│       │   │   └── MetricTile.tsx      # single big metric with tooltip
│       │   ├── sql/
│       │   │   └── ResultTable.tsx     # generic typed table, infers columns
│       │   └── common/
│       │       ├── EmptyState.tsx      # shown when no result, CTA to upload
│       │       ├── LoadingOverlay.tsx  # full-screen blocker during API call
│       │       └── ErrorBanner.tsx     # top-of-page error display
│       ├── styles/
│       │   ├── tokens.css        # dark theme CSS variables
│       │   └── global.css
│       └── utils/
│           └── format.ts         # number/duration formatting helpers
│
└── src/   (existing — minimal change only)
```

---

## API Design

### `POST /api/analyze`

- **Content-Type:** `multipart/form-data`
- **Field:** `file` — CSV file
- **Limits:** 10 MB max, `.csv` extension only
- **Status codes:** `200` success, `400` invalid CSV/schema, `413` too large, `500` pipeline error

**Response shape (`AnalysisResult`):**

```ts
{
  meta: {
    row_count: number,
    columns: string[],
    duration_ms: number,
    generated_at: string   // ISO 8601
  },
  kpis: {
    total_orders: number,
    avg_delivery_time: number,     // minutes
    peak_delivery_time: number,
    non_peak_delivery_time: number
  },
  peak_hour_trend: Array<{
    hour: number,                  // 0–23
    avg_delivery_duration: number,
    is_peak: boolean               // true for hours 19–22
  }>,
  city_demand: Array<{
    city: string,
    total_orders: number
  }>,
  ml: {
    model: string,                 // "LinearRegression"
    features: string[],
    target: string,
    mae: number,
    r2: number,
    test_size: number,
    random_seed: number
  },
  sql: {
    delivery_by_hour: Array<{ hour: string, total_orders: number, avg_delivery_time: number }>,
    peak_vs_non_peak: Array<{ time_bucket: string, total_orders: number, avg_delivery_time: number }>,
    city_performance: Array<{ city: string, total_orders: number, avg_delivery_time: number }>
  }
}
```

**Error response:**
```ts
{ error: { code: string, message: string } }
```

### `GET /api/health` → `{ "status": "ok" }`

---

## Data Flow

```
User drops CSV onto Dropzone
  → file held in component state
  → clicks "Run Analysis"
  → api/client.ts uploadCsv(file): FormData → POST /api/analyze
  → AnalysisContext dispatches START (shows LoadingOverlay)

FastAPI receives upload
  → validates extension + size
  → reads bytes into io.BytesIO buffer
  → services/pipeline.py run_full_pipeline(buffer)
      1. pd.read_csv(buffer)
      2. preprocess(df)              ← src/preprocessing.py
      3. validate_data(df)           ← raises → 400 on bad schema
      4. kpi_metrics(df)             ← src/analysis.py
      5. peak_hour_analysis(df)
      6. demand_by_city(df)
      7. train_and_evaluate(df)      ← src/prediction.py
      8. run_queries_json(df)        ← src/sql_runner.py (new function)
      9. assemble AnalysisResult Pydantic model
  → return JSON (no disk writes in API path)

Browser receives response
  → AnalysisContext dispatches SUCCESS(payload)
  → Router navigates to /overview
  → All pages read result via useAnalysis() hook
```

---

## Pages

| Page | Route | Content |
|------|-------|---------|
| Upload | `/upload` | Dropzone + RunButton + LoadingOverlay |
| Overview | `/overview` | 4 KpiCards (total orders, avg/peak/non-peak delivery time) |
| Charts | `/charts` | PeakHourChart + CityDemandChart side-by-side |
| ML Results | `/ml` | 2 MetricTiles (MAE, R²) + feature list |
| SQL Results | `/sql` | 3 ResultTables (delivery by hour, peak vs non-peak, city performance) |

Non-upload pages render `<EmptyState />` with a CTA back to `/upload` when `result === null`. NavTabs disables all non-upload links until a result is loaded.

---

## State Management

React Context only — no Redux/Zustand needed.

```ts
type Status = 'idle' | 'loading' | 'success' | 'error';

interface AnalysisState {
  status: Status;
  result: AnalysisResult | null;
  error: { code: string; message: string } | null;
  fileName: string | null;
}
```

Actions: `START`, `SUCCESS(payload)`, `FAILURE(error)`, `RESET`  
Hook: `useAnalysis()` → `{ state, runAnalysis(file), reset() }`

No sessionStorage/localStorage persistence — refresh resets state intentionally.

---

## Change to Existing Code

**Only one change** to `src/sql_runner.py`: add `run_queries_json(df) -> dict[str, list[dict]]` that returns the three query results as JSON-serializable lists. The existing `run_queries()` function stays unchanged for CLI use.

`src/preprocessing.py::load_data` takes a path — the pipeline service calls `pd.read_csv(buffer)` directly and passes the DataFrame into `preprocess()`. No changes to `preprocess`, `analysis`, `prediction`, or any other module.

---

## Dependencies

### Backend (`api/requirements.txt`)
```
fastapi==0.115.0
uvicorn[standard]==0.32.0
python-multipart==0.0.12
pydantic==2.9.2
pandas==2.2.3
scikit-learn==1.5.2
numpy==2.1.3
pytest==8.3.3
httpx==0.27.2
```

### Frontend (`ui/package.json`)
```json
{
  "dependencies": {
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-router-dom": "^6.27.0",
    "recharts": "^2.13.0",
    "react-dropzone": "^14.3.5"
  },
  "devDependencies": {
    "typescript": "^5.6.3",
    "vite": "^5.4.10",
    "@vitejs/plugin-react": "^4.3.3",
    "@types/react": "^18.3.12",
    "@types/react-dom": "^18.3.1",
    "vitest": "^2.1.4",
    "@testing-library/react": "^16.0.1",
    "jsdom": "^25.0.1"
  }
}
```

---

## Dev Commands

```bash
# Backend
cd api && uvicorn main:app --reload --port 8000

# Frontend (separate terminal)
cd ui && npm run dev    # proxies /api → localhost:8000

# Tests
cd api && pytest
cd ui && npm run test
```
