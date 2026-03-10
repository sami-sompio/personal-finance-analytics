from pathlib import Path

import pandas as pd


def load_transactions(file_path: Path) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    return df


def load_budget(file_path: Path) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    return df