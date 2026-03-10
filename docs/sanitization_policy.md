# Sanitization Policy

## Purpose

This repository is a public portfolio project. It must not expose any real personal financial data or any information that could identify a real person, institution, account, or life event.

## Core Rule

If there is uncertainty about whether something is safe to publish, it should be treated as private and excluded until it has been fully reviewed.

## Never Publish

The following must never appear in the public repository:

- real bank names
- real counterparties
- real account numbers
- real transaction descriptions
- real file paths that reveal personal information
- real dates tied to identifiable life events
- personal names, IDs, addresses, or other identifiers
- screenshots containing raw unsanitized records
- Power BI files containing real imported data
- rule files built from real merchant patterns unless rewritten with fictional examples

## Public Safe Standards

All public materials must follow these standards:

1. Replace bank names with generic placeholders such as `Bank A` or `SourceAccount1`
2. Replace counterparties with fictional labels such as `Merchant Alpha` or `Utility Provider`
3. Remove all account and reference numbers
4. Replace transaction descriptions with generic category aligned examples
5. Shift or randomize dates so they cannot be linked to real life events
6. Review report filters, tooltips, hidden pages, hidden columns, and drillthrough pages before publishing
7. Review Power Query source steps for local paths or file names
8. Prefer synthetic data whenever possible

## Preferred Public Data Strategy

The safest strategy is to use **fully synthetic sample data** that preserves the analytical logic of the project without exposing any real financial history.

## Review Requirement

Nothing should be published until it has been manually reviewed.

This includes:

- CSV sample files
- screenshots
- rule files
- Power BI files
- documentation examples