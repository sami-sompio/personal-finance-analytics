import pandas as pd


def add_month_column(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result["transaction_date"] = pd.to_datetime(result["transaction_date"])
    result["month"] = result["transaction_date"].dt.strftime("%Y-%m")
    return result


def summarize_transactions(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.groupby(["month", "category"], as_index=False)["amount"]
        .sum()
        .sort_values(["month", "category"])
    )
    return summary