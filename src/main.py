from pathlib import Path

from utils import ensure_output_dir
from data_loader import load_transactions, load_budget
from transformations import add_month_column, summarize_transactions
from exporters import export_csv


def main() -> None:
    project_root = Path(__file__).resolve().parent.parent

    transactions_path = project_root / "data" / "sample" / "synthetic_transactions.csv"
    budget_path = project_root / "data" / "sample" / "synthetic_budget.csv"
    output_dir = project_root / "output"

    ensure_output_dir(output_dir)

    transactions_df = load_transactions(transactions_path)
    budget_df = load_budget(budget_path)

    transactions_df = add_month_column(transactions_df)
    monthly_summary_df = summarize_transactions(transactions_df)

    export_csv(transactions_df, output_dir / "transactions_enriched.csv")
    export_csv(monthly_summary_df, output_dir / "monthly_category_summary.csv")
    export_csv(budget_df, output_dir / "budget_clean.csv")

    print("Pipeline completed successfully.")
    print(f"Rows loaded from transactions: {len(transactions_df)}")
    print(f"Rows loaded from budget: {len(budget_df)}")
    print(f"Files written to: {output_dir}")


if __name__ == "__main__":
    main()