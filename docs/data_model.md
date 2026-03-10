# Data Model

## Overview

The reporting model follows a star schema designed for budget analysis and personal finance reporting.

The model separates transactional data from descriptive dimensions to support clean analytics and efficient calculations.

## Core Tables

### FactTransactions

The central fact table containing transaction-level financial movements.

Typical fields include:

- TransactionDate
- Amount
- CategoryKey
- TransactionType
- Account
- DescriptionStandardized

Each row represents a single financial transaction.

### DimDate

A calendar dimension used for time-based analysis.

Typical attributes include:

- Date
- Month
- Month Name
- Quarter
- Year

### DimCategory

The category dimension used for grouping transactions into reporting categories such as housing, groceries, transport, and entertainment.

### Budget

A table containing planned budget values by category and period.

This allows comparison between:

- Actual spending
- Planned budget

## Relationships

The model relationships are designed as a star schema:

FactTransactions → DimDate  
FactTransactions → DimCategory  
Budget → DimDate  
Budget → DimCategory

This structure enables clean reporting and simplifies DAX calculations.

## Measure Organization

Measures are grouped into logical folders in Power BI.

### Base Metrics

Core financial measures used across the model.

### Budget

#### Annual

- Budget Amount
- Variance
- Variance %
- Budget Consumed %
- Budget Remaining
- Budget Pace %

#### Current Context

- Budget Amount Raw
- Variance Raw
- Variance % Raw

#### YTD Diagnostics

- Expenses YTD
- Budget YTD Correct
- Variance YTD
- Variance YTD %
- Forecast Year End
- Forecast vs Budget %