# Categorization Rules

## Purpose

The categorization system assigns transactions to reporting categories so that spending and income can be analyzed consistently.

## Rule-Based Categorization

Transactions are categorized using rule-based logic. Rules typically match patterns in transaction descriptions or other attributes and assign a reporting category.

Example rule types include:

- description contains a keyword
- standardized transaction label matches a pattern
- transaction type maps to a fixed category

## Recategorization

Sometimes automatic categorization needs manual correction.

A recategorization layer allows transactions to be reassigned to a different category after review.

## Public Repository Version

The public repository contains only **example rule files** with fictional values.

These can be found in:
```bash
rules/category_rules_example.csv
rules/recategorization_rules_example.csv
```
Real merchant names or transaction descriptions are never included in the public repository.

## Iterative Improvement

Categorization rules improve over time as more transactions are reviewed and patterns are identified.