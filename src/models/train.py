"""
Model training module.
"""

from sklearn.linear_model import LinearRegression


def train_baseline_model(X_train, y_train):
    """
    Train a baseline regression model.
    """
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model
