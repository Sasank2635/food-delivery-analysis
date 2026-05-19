import pandas as pd


def peak_hour_analysis(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby('hour')['delivery_duration'].mean().reset_index()


def demand_by_city(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby('city')['order_id'].count().reset_index(name='total_orders')


def kpi_metrics(df: pd.DataFrame) -> dict[str, float]:
    return {
        "avg_delivery_time": float(df['delivery_duration'].mean()),
        "peak_delivery_time": float(df[df['is_peak_hour'] == 1]['delivery_duration'].mean()),
        "non_peak_delivery_time": float(df[df['is_peak_hour'] == 0]['delivery_duration'].mean()),
        "total_orders": float(len(df)),
    }


def root_cause_analysis(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby('is_peak_hour')[['delivery_duration', 'distance_km']].mean()
