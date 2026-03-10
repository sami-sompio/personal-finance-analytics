# Analytics Workflow Diagram

The project follows a layered analytics workflow typical for modern BI systems.

```bash
Raw Transaction Exports
        │
        ▼
Python Data Pipeline
(src/main.py)
        │
        ▼
Clean Transactions Dataset
(output/transactions_enriched.csv)
        │
        ▼
Category Aggregations
(output/monthly_category_summary.csv)
        │
        ▼
Power BI Semantic Model
(FactTransactions, DimDate, DimCategory, Budget)
        │
        ▼
Budget & Expense Dashboards
```