import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

RANDOM_SEED = 42
TEST_SIZE = 0.2


def train_and_evaluate(df: pd.DataFrame) -> tuple[LinearRegression, float, float]:
    X = df[['distance_km', 'hour', 'is_peak_hour']]
    y = df['delivery_duration']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_SEED
    )

    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    return model, float(mean_absolute_error(y_test, predictions)), float(r2_score(y_test, predictions))
