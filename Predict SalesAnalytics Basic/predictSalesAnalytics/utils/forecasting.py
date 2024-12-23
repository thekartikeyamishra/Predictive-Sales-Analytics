import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def train_forecast_model(data):
    data["Time"] = range(len(data))
    X = data(["Time"])
    y = data(["Sales"])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model, X_test, y_test


def save_model(model, path="models/sales_forecast.pkl"):
    joblib.dump(model, path)


def predict_future_sales(model, future_periods=30):
    future_time = [[i] for i in range(model.n_features_in_, model.n_features_in_ + future_periods)]
    predictions = model.predict(future_time)
    return predictions
