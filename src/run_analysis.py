import logging
import os
import json

from preprocessing import load_data, preprocess, validate_data
from analysis import (
    peak_hour_analysis,
    demand_by_city,
    kpi_metrics,
    root_cause_analysis
)
from visualization import plot_peak_hours, plot_city_demand
from prediction import train_and_evaluate
from sql_runner import run_queries


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def ensure_directories():
    os.makedirs("../outputs", exist_ok=True)
    os.makedirs("../dashboard", exist_ok=True)


def run_pipeline():
    try:
        logging.info("🚀 Starting food delivery analytics pipeline")

        ensure_directories()

        df = load_data("../data/raw_orders.csv")
        df = preprocess(df)
        validate_data(df)

        logging.info(f"✅ Data loaded: {len(df)} records")

        kpis = kpi_metrics(df)
        logging.info("📊 KPI Metrics:")
        for k, v in kpis.items():
            logging.info(f"{k}: {v:.2f}")

        # 💾 Save KPI for dashboard
        with open("../dashboard/kpi_metrics.json", "w") as f:
            json.dump(kpis, f, indent=4)
        logging.info("📁 KPI saved to dashboard/kpi_metrics.json")

        # 🔍 Root Cause Analysis
        root = root_cause_analysis(df)
        logging.info("🔍 Root Cause Analysis:")
        logging.info(f"\n{root}")

        # 📈 Aggregations for visualization + dashboard
        peak = peak_hour_analysis(df)
        city = demand_by_city(df)

        # 💾 Save for dashboard
        peak.to_csv("../dashboard/peak_hour_data.csv", index=False)
        city.to_csv("../dashboard/city_data.csv", index=False)

        logging.info("📁 Dashboard data saved")

        # 📊 Visualization
        plot_peak_hours(peak)
        plot_city_demand(city)

        logging.info("📈 Visualizations saved in outputs/")

        # 🤖 ML Model
        model, mae, r2 = train_and_evaluate(df)

        logging.info("🤖 Model Performance:")
        logging.info(f"MAE: {mae:.2f}")
        logging.info(f"R2 Score: {r2:.2f}")

        # 💾 Save model metrics
        model_metrics = {"MAE": mae, "R2": r2}
        with open("../outputs/model_metrics.json", "w") as f:
            json.dump(model_metrics, f, indent=4)

        logging.info("📁 Model metrics saved")

        # 🗄️ SQL Execution
        logging.info("🗄️ Running SQL analytics...")
        run_queries()

        logging.info("✅ Pipeline completed successfully")

    except Exception as e:
        logging.error("❌ Pipeline failed")
        logging.error(str(e))


if __name__ == "__main__":
    run_pipeline()