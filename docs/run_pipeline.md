# Running the Data Pipeline

This repository includes a minimal Python pipeline that processes synthetic financial data and produces analytics-ready outputs.

The pipeline demonstrates a simplified version of the workflow used in the full personal finance analytics project.

## Prerequisites

Python 3.10 or newer.

## Install dependencies

From the project root directory run:

pip install -r requirements.txt

## Run the pipeline

Execute the pipeline with:

python src/main.py

## Pipeline steps

The pipeline performs the following operations:

1. Loads synthetic transaction and budget datasets
2. Cleans and prepares the transaction data
3. Adds a month field derived from transaction date
4. Creates a monthly category summary dataset
5. Writes clean output files to the output directory

## Output files

Running the pipeline generates the following files:

output/transactions_enriched.csv  
output/monthly_category_summary.csv  
output/budget_clean.csv

These files are designed to simulate the cleaned data layer that would normally feed a BI model.