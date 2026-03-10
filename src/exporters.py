from pathlib import Path

import pandas as pd


def export_csv(df: pd.DataFrame, output_path: Path) -> None:
    df.to_csv(output_path, index=False)