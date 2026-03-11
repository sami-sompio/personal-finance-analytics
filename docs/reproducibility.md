# Reproducibility

## Goal

The public version of this project should be reproducible using synthetic example data and example rule files.

The repository demonstrates the structure and workflow of the analytics pipeline without exposing private financial data.

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd personal-finance-analytics
```

### 2. Create a Python environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the pipeline

```bash
python src/main.py
```

### 7. Open the Power BI report

7. Open the Power BI report

Load the processed dataset into Power BI Desktop and recreate the report using the model structure and example screenshots provided in the repository.

## Important

The public repository is designed so the project structure can be reproduced without requiring real personal financial data.