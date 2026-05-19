import logging
import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['order_time'] = pd.to_datetime(df['order_time'])
    df['delivery_time'] = pd.to_datetime(df['delivery_time'])
    df['delivery_duration'] = (
        df['delivery_time'] - df['order_time']
    ).dt.total_seconds() / 60
    df['hour'] = df['order_time'].dt.hour
    df['is_peak_hour'] = df['hour'].between(19, 22).astype(int)
    return df


def validate_data(df: pd.DataFrame) -> None:
    if df.isnull().sum().sum() > 0:
        raise ValueError("Missing values found")
    if (df['delivery_duration'] <= 0).any():
        raise ValueError("Invalid delivery time")
    logging.info("Data validation passed")
