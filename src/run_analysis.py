import logging
import json
import pathlib

from preprocessing import load_data, preprocess, validate_data
from analysis import peak_hour_analysis, demand_by_city, kpi_metrics, root_cause_analysis
from visualization import plot_peak_hours, plot_city_demand
from prediction import train_and_evaluate
from sql_runner import run_queries

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

BASE = pathlib.Path(__file__).resolve().parent.parent
DATA_DIR = BASE / "data"
OUTPUTS_DIR = BASE / "outputs"
DASHBOARD_DIR = BASE / "dashboard"


def ensure_directories() -> None:
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    DASHBOARD_DIR.mkdir(parents=True, exist_ok=True)


def run_pipeline() -> None:
    try:
        logging.info("Starting food delivery analytics pipeline")
        ensure_directories()

        df = load_data(DATA_DIR / "raw_orders.csv")
        df = preprocess(df)
        validate_data(df)
        logging.info("Data loaded: %d records", len(df))

        kpis = kpi_metrics(df)
        logging.info("KPI Metrics: %s", kpis)
        with open(DASHBOARD_DIR / "kpi_metrics.json", "w") as f:
            json.dump(kpis, f, indent=4)

        root = root_cause_analysis(df)
        logging.info("Root Cause Analysis:\n%s", root)

        peak = peak_hour_analysis(df)
        city = demand_by_city(df)
        peak.to_csv(DASHBOARD_DIR / "peak_hour_data.csv", index=False)
        city.to_csv(DASHBOARD_DIR / "city_data.csv", index=False)
        logging.info("Dashboard data saved")

        plot_peak_hours(peak)
        plot_city_demand(city)
        logging.info("Visualizations saved")

        model, mae, r2 = train_and_evaluate(df)
        logging.info("Model — MAE: %.2f  R2: %.2f", mae, r2)
        with open(OUTPUTS_DIR / "model_metrics.json", "w") as f:
            json.dump({"MAE": mae, "R2": r2}, f, indent=4)

        logging.info("Running SQL analytics...")
        run_queries()

        logging.info("Pipeline completed successfully")

    except Exception:
        logging.exception("Pipeline failed")
        raise


if __name__ == "__main__":
    run_pipeline()
