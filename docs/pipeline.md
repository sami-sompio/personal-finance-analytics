# Python Pipeline

## Purpose

The Python pipeline prepares raw transaction exports for analysis by standardizing schemas, applying category rules, and producing a clean combined dataset.

## Responsibilities

The pipeline performs the following steps:

- ingest raw CSV exports
- standardize column names
- clean and normalize formats
- apply categorization rules
- support recategorization workflows
- export a combined transaction dataset

## Typical Flow

Raw CSV files  
→ schema alignment  
→ column cleaning  
→ category rule matching  
→ review and recategorization  
→ combined transactions dataset

## Expected Inputs

The pipeline expects:

- transaction CSV exports
- category rule definitions
- optional recategorization rules

## Expected Output

The main output is a clean dataset such as:

`combined_transactions.csv`

In the public repository this output should be generated using synthetic sample data.