# Architecture

## End-to-End Flow

The project follows this analytics workflow:

Raw CSV exports  
→ Python ingestion and schema standardization  
→ rule-based categorization  
→ combined transactions dataset  
→ Power BI star schema model  
→ budget analytics dashboards

## Layer Description

### Raw Input Layer

Transaction exports are received as CSV files from source systems.

### Transformation Layer

Python scripts standardize column names, normalize formats, and align schemas across sources.

### Categorization Layer

Rule-based logic assigns reporting categories to transactions.

A recategorization layer allows manual corrections and improvements.

### Analytical Dataset Layer

The processed output is stored as a clean transaction dataset used by the reporting model.

### Semantic Model Layer

Power BI implements a star schema built around:

- transaction facts
- date dimension
- category dimension
- budget table

### Reporting Layer

Dashboards provide:

- financial overview
- category calibration
- budget vs actual comparison
- budget diagnostics