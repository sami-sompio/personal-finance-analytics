# Sample Data

This folder contains synthetic datasets for the Personal Finance Analytics project.

These files are included so the repository can be understood, tested, and demonstrated without exposing any real personal financial data.

## Files

### synthetic_transactions.csv
Synthetic transaction level data that represents example income and expense activity across multiple categories.

Main fields:
- transaction_id
- transaction_date
- account_type
- account_name
- category
- merchant
- description
- amount
- currency
- payment_method
- notes

### synthetic_budget.csv
Synthetic monthly budget data used for budget versus actual analysis in Power BI.

Main fields:
- budget_month
- category
- budget_amount
- currency
- notes

## Privacy Notice

All data in this folder is fictional and created for demonstration purposes only.

No real bank exports, personal identifiers, account numbers, merchants tied to a real individual, or actual financial records are included in this repository.

## Intended Use

These files are meant to:

- support local testing of the Python pipeline
- demonstrate expected input structure
- enable portfolio safe Power BI examples
- provide reproducible sample analytics outputs