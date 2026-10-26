# BrasilAPI PySpark ETL Pipeline

[![Python](https://img.shields.io/badge/Python-3.12.3-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PySpark](https://img.shields.io/badge/PySpark-3.0+-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)](https://spark.apache.org/docs/latest/api/python/)
[![Architecture](https://img.shields.io/badge/Architecture-Medallion-0052CC?style=for-the-badge)](https://www.databricks.com/glossary/medallion-architecture)
[![Format](https://img.shields.io/badge/Format-Parquet-009688?style=for-the-badge)](https://parquet.apache.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

An end-to-end Data Engineering ETL project built with **Python** and **PySpark**, designed around the **Medallion Architecture** (Bronze, Silver, Gold). This pipeline ingests public financial and banking data from [BrasilAPI](https://brasilapi.com.br/), cleanses and standardizes schemas, and prepares aggregated data for business analytics.

---

## Architecture Overview

The project simulates a local **Data Lakehouse** divided into three distinct layers:

```text
  [ BrasilAPI ] ──(HTTP GET)──> 🟤 BRONZE (Raw JSON)
                                      │
                                  (PySpark)
                                      ▼
                                ⚪ SILVER (Cleaned Parquet)
                                      │
                                  (PySpark)
                                      ▼
                                🟡 GOLD (Aggregated Parquet)

```

1. **🟤 Bronze Layer (Raw):** Ingests raw JSON responses directly from REST endpoints without modifications.
2. **⚪ Silver Layer (Cleansed):** Uses PySpark to enforce schema types, clean string fields, normalize column names into standardized English (*snake_case*), deduplicate records, and export to **Parquet**.
3. **🟡 Gold Layer (Aggregated):** Performs analytical aggregations (e.g., banking code summaries, state-level financial metrics) ready for BI dashboards.

---

## Project Objectives & Roadmap

* [x] **Project Setup**: Establish modular directory structure (`src/ingestion`, `src/transformations`).
* [x] **Bronze Layer**: Ingest raw JSON datasets (`/banks`, `/corretoras`) using Python `requests`.
* [x] **Silver Layer (Banks)**:
* [x] Parse raw JSON with PySpark.
* [x] Filter out invalid records without ISPB identifiers.
* [x] Rename and normalize columns to standardized English (`ispb`, `compe_code`, `short_name`, `full_name`, `has_compe_code`).
* [x] Handle data types (`IntegerType` casting) and trim whitespace.
* [x] Deduplicate records based on primary key (`ispb`).
* [x] Save cleaned dataset in compressed **Parquet** format.


* [ ] **Silver Layer (Brokerages / CVM)**: Clean CNPJs, map states (UF), and format net worth variables.
* [ ] **Gold Layer**: Build business-level aggregate views and analytics.
* [ ] **Testing & Quality**: Implement unit tests with `pytest` and schema validation assertions.
* [ ] **Orchestration**: (Optional) Integrate with Apache Airflow or Prefect.

---

## Project Structure

```text
brasilapi-pyspark-etl/
├── data/
│   ├── bronze/                  # Raw JSON files
│   ├── silver/                  # Cleaned Parquet files
│   └── gold/                    # Aggregated analytics datasets
├── src/
│   ├── ingestion/
│   │   └── ingestion.py         # HTTP Fetcher & Bronze writer
│   └── transformations/
│       ├── silver.py            # PySpark Silver transformations
│       └── gold.py              # PySpark Gold aggregations
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation

```

---

## Getting Started

### Prerequisites

* Python 3.12.3
* Java OpenJDK 8 or 11 (required by PySpark)

### Installation

1. **Clone the repository:**
```bash
git clone [https://github.com/your-username/brasilapi-pyspark-etl.git](https://github.com/your-username/brasilapi-pyspark-etl.git)
cd brasilapi-pyspark-etl

```


2. **Create and activate a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```



---

## Running the Pipeline

1. **Run Ingestion (Bronze Layer):**
```bash
python src/ingestion/ingestion.py

```


2. **Run Transformations (Silver Layer):**
```bash
python src/transformations/silver.py

```



---

## License

Distributed under the MIT License. See `LICENSE` for more information.