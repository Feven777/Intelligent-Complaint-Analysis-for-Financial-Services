import pandas as pd
from .config import DATA_PATH


def load_clean_data():
    """
    Load cleaned complaint data for embedding.
    """
    return pd.read_csv(DATA_PATH)
