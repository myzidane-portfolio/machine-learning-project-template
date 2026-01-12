"""
Utility helper functions.
"""


def print_metrics(metrics: dict):
    """
    Pretty-print evaluation metrics.
    """
    for key, value in metrics.items():
        print(f"{key.upper()}: {value:.4f}")
