"""
Feature engineering module.
"""

import pandas as pd
from sklearn.model_selection import train_test_split


def split_features_target(df: pd.DataFrame, target: str):
    """
    Split DataFrame into features and target.
    """
    X = df.drop(columns=[target])
    y = df[target]
    return X, y


def train_test_split_data(
    X,
    y,
    test_size: float = 0.2,
    random_state: int = 42
):
    """
    Split data into train and test sets.
    """
    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state
    )
