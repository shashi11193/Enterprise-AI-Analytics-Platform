# Enterprise AI Analytics Platform

Enterprise-grade analytics engineering platform built using Python, DuckDB, dbt, and FastAPI.

The platform demonstrates how raw enterprise operational data can be ingested, validated, transformed into analytics-ready models, and exposed through production-style REST APIs.

---

# Features

✔ Multi-format data ingestion

- JSON
- Markdown
- YAML
- PDF

✔ Automated ingestion pipeline

- Data normalization
- Validation
- Auditing
- Duplicate detection

✔ Enterprise Data Warehouse

- DuckDB Bronze Layer

✔ dbt Transformations

- Staging Models
- Mart Models
- Aggregate Models

✔ REST API

- FastAPI
- Analytics Endpoints
- Incident APIs
- Ticket APIs

---

# Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Warehouse | DuckDB |
| Transformations | dbt |
| API | FastAPI |
| Data Formats | JSON, YAML, Markdown, PDF |
| Version Control | Git |
| Documentation | Markdown |

---

# Project Architecture

<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/8d8acf4c-af78-4e4b-920b-5d6dde98e779" />



---

# Project Structure

```
enterprise_ai_platform/

├── ingestion/
├── api/
├── models/
│   ├── staging
│   └── marts
├── raw_sources/
├── macros/
├── snapshots/
├── seeds/
└── README.md
```

---

# Data Pipeline

The ingestion pipeline performs:

- Loading enterprise documents
- Schema normalization
- Duplicate detection
- Missing field validation
- Warehouse loading

---

# dbt Models

### Staging

- stg_incidents
- stg_tickets

### Mart

- mart_incident_kpis
- mart_ticket_kpis

### Aggregate

- agg_incident_daily
- agg_ticket_daily
- agg_department_performance

---

# API Endpoints

## Incidents

GET /incidents

GET /incidents/{incident_id}

---

## Tickets

GET /tickets

GET /tickets/{ticket_id}

---

## Analytics

GET /analytics/incidents

GET /analytics/tickets

---

# Running the Project

## Install

```bash
pip install -r requirements.txt
```

---

## Run ingestion

```bash
python -m ingestion.pipeline
```

---

## Run dbt

```bash
dbt run
dbt test
```

---

## Run API

```bash
uvicorn api.main:app --reload
```

---

# Highlights

- Enterprise Analytics Engineering
- Data Quality Validation
- Automated ETL
- DuckDB Warehouse
- dbt Data Modeling
- FastAPI Service Layer
- Production Repository Structure

---

# Future Enhancements

- CI/CD with GitHub Actions
- Docker Deployment
- Kubernetes Support
- Airflow Scheduling
- Snowflake Migration
- Great Expectations Data Validation

---

# Author

**Shashi Kumar Mantha**

Analytics Engineer | AI Solutions Engineer

GitHub:
https://github.com/shashi11193
