import sqlite3
import pandas as pd
import logging


# 🔥 Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def run_queries():
    try:
        logging.info("🗄️ Starting SQL query execution...")

        # 📥 Load CSV
        df = pd.read_csv("../data/raw_orders.csv")
        logging.info(f"Loaded dataset with {len(df)} rows")

        # 🧠 Create in-memory DB
        conn = sqlite3.connect(":memory:")
        df.to_sql("orders", conn, index=False, if_exists="replace")

        logging.info("SQLite in-memory database created")

        # 📊 Queries
        queries = {

            "delivery_by_hour": """
            SELECT 
                strftime('%H', order_time) AS hour,
                COUNT(*) AS total_orders,
                AVG((julianday(delivery_time) - julianday(order_time)) * 24 * 60) AS avg_delivery_time
            FROM orders
            GROUP BY hour
            ORDER BY hour;
            """,

            "peak_vs_non_peak": """
            SELECT 
                CASE 
                    WHEN CAST(strftime('%H', order_time) AS INTEGER) BETWEEN 19 AND 22 THEN 'Peak'
                    ELSE 'Non-Peak'
                END AS time_bucket,
                COUNT(*) AS total_orders,
                AVG((julianday(delivery_time) - julianday(order_time)) * 24 * 60) AS avg_delivery_time
            FROM orders
            GROUP BY time_bucket;
            """,

            "city_performance": """
            SELECT 
                city,
                COUNT(*) AS total_orders,
                AVG((julianday(delivery_time) - julianday(order_time)) * 24 * 60) AS avg_delivery_time
            FROM orders
            GROUP BY city;
            """
        }

        # ▶️ Run queries
        for name, query in queries.items():
            logging.info(f"📊 Running query: {name}")

            result = pd.read_sql(query, conn)

            logging.info(f"Result:\n{result}")

        conn.close()
        logging.info("✅ SQL execution completed successfully")

    except Exception as e:
        logging.error("❌ SQL execution failed")
        logging.error(str(e))


if __name__ == "__main__":
    run_queries()