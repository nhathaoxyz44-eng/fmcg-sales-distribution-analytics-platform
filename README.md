# VietDist Sales & Distribution Analytics Platform

## Project Overview

An end-to-end FMCG Analytics Engineering project designed for VietDist Corporation, a consumer goods distribution company operating across multiple regions.

The project builds a complete data pipeline that integrates multi-source business data into analytics-ready data marts using Python, PostgreSQL, Medallion Architecture, dimensional modeling, and Power BI.

---

## Business Problem

VietDist currently manages business data across multiple disconnected sources, including Excel files, CSV exports, ERP reports, and department-level storage systems.

Business stakeholders require:

- A centralized analytics platform
- Automated data ingestion and transformation
- Consistent sales and distribution performance reporting
- Historical tracking of business changes
- Reliable metrics for decision making

---

## Solution Overview

The solution follows an Analytics Engineering approach:

```text
Source Files
(CSV / XLSX / XLSB)
        |
        v
Python Data Ingestion
        |
        v
PostgreSQL Data Warehouse
        |
        v
Bronze Layer
        |
        v
Silver Layer
        |
        v
Gold Dimensional Warehouse
        |
        v
Business Data Marts
        |
        v
Power BI Analytics
```

---

## Architecture Principles

### Medallion Architecture

| Layer | Purpose |
|---|---|
| Bronze | Preserve raw source data and ingestion metadata |
| Silver | Clean, standardize, validate business data |
| Gold | Build analytical dimensions, facts, and marts |

### Data Modeling

The project applies:

- Star Schema
- Fact and Dimension modeling
- Slowly Changing Dimension Type 2
- Temporal data modeling for sales target versions
- Data quality validation

---

## Key Engineering Challenges

### 1. Multi-source Data Integration

The pipeline handles multiple business datasets including:

- Sales transactions
- Sales targets
- Customers
- Products
- Employees
- Distributors
- Returns
- Promotions

### 2. Sales Target Version Management

The system preserves historical target versions and supports comparison between actual performance and different target plans.

### 3. Historical Dimension Tracking

Employee and distributor changes are managed using SCD Type 2 to maintain accurate historical reporting.

---

## Technology Stack

- Python
- Pandas
- PostgreSQL
- SQL
- Power BI
- GitHub

---

## Project Status

| Phase | Status |
|---|---|
| Requirement Analysis | Completed |
| Project Bootstrap | In Progress |
| Source Profiling | Upcoming |
| Data Pipeline Development | Upcoming |
| Data Warehouse Modeling | Upcoming |
| Power BI Analytics | Upcoming |

---

## Repository Structure

```text
00_setup/
01_ingestion/
02_transformations/
03_data_warehouse/
04_analytics/
05_power_bi/
docs/
tests/
```

---

## Documentation

Detailed project documentation is maintained in the `/docs` folder:

- Business requirement matrix
- Source-to-target mapping
- Assumptions log
- Data issue tracking
- Architecture design

---

## Future Improvements

Potential future enhancements:

- Automated orchestration workflow
- Cloud deployment
- Advanced monitoring
- Additional business domains
