import pandas as pd

def open_data(filepath: str):
    """
    Args:
        filepath (str): _description_
    """
    assert filepath.endswith(".csv"), "only csv supported"

    return pd.read_csv(filepath)