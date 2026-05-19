import sqlite3
import logging
import pandas as pd


def run_queries(df: pd.DataFrame) -> None:
    logging.info("Starting SQL query execution...")

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
        """,
    }

    with sqlite3.connect(":memory:") as conn:
        df.to_sql("orders", conn, index=False, if_exists="replace")
        logging.info("SQLite in-memory database created with %d rows", len(df))
        for name, query in queries.items():
            result = pd.read_sql(query, conn)
            logging.info("Query [%s]:\n%s", name, result)

    logging.info("SQL execution completed")


def run_queries_json(df: pd.DataFrame) -> dict[str, list[dict]]:
    """Run analytical queries and return results as plain dicts."""
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
        """,
    }

    with sqlite3.connect(":memory:") as conn:
        df.to_sql("orders", conn, index=False, if_exists="replace")
        return {
            name: pd.read_sql(query, conn).to_dict(orient="records")
            for name, query in queries.items()
        }


if __name__ == "__main__":
    import pathlib
    import sys
    sys.path.insert(0, str(pathlib.Path(__file__).parent))
    from preprocessing import load_data, preprocess
    BASE = pathlib.Path(__file__).resolve().parent.parent
    df = preprocess(load_data(BASE / "data" / "raw_orders.csv"))
    run_queries(df)
