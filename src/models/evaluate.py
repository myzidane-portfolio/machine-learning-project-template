"""
Model evaluation module.
"""

from sklearn.metrics import mean_squared_error, r2_score


def evaluate_regression(model, X_test, y_test):
    """
    Evaluate regression model performance.
    """
    predictions = model.predict(X_test)

    metrics = {
        "rmse": mean_squared_error(y_test, predictions, squared=False),
        "r2": r2_score(y_test, predictions),
    }

    return metrics
