"""
Data loading module.

Responsible for fetching or loading raw data
and returning it as a pandas DataFrame.
"""

import pandas as pd
from sklearn.datasets import fetch_california_housing


def load_data(as_frame: bool = True) -> pd.DataFrame:
    """
    Load dataset.

    Currently uses sklearn's California Housing dataset.
    Can later be replaced with CSV, database, or API.

    Returns
    -------
    pd.DataFrame
        Dataset with target column included.
    """
    dataset = fetch_california_housing(as_frame=as_frame)
    df = dataset.frame
    return df
