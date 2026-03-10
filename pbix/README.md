# Power BI Files

This folder is intended for sanitized or portfolio safe Power BI assets related to the Personal Finance Analytics project.

## What belongs here

Examples:
- a portfolio safe `.pbix` file built only from synthetic or sanitized data
- exported schema reference images
- model notes related to the published BI version

## What must never be published

Do not publish:
- `.pbix` files containing real personal financial data
- cached model files tied to real source exports
- screenshots showing real transactions, counterparties, references, balances, or account details
- hidden pages that still contain sensitive visuals or tables

## Recommended public workflow

1. Build the report using synthetic sample data or fully sanitized extracts
2. Verify all visuals, filters, tooltips, drillthrough pages, and hidden tabs
3. Confirm that no personal identifiers appear anywhere in the report
4. Publish only the privacy safe version

## Suggested naming

Example public file names:
- `personal_finance_analytics_synthetic.pbix`
- `personal_finance_budget_demo.pbix`