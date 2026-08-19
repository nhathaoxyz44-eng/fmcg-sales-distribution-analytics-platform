# VietDist Analytics Architecture Design

## Overview

The platform follows a Medallion Architecture approach.

## Architecture Flow

Source Files (CSV/XLSX/XLSB)

↓

Python Data Ingestion Layer

↓

PostgreSQL

↓

Bronze Layer (raw)

↓

Silver Layer (staging)

↓

Gold Layer (dimensional warehouse)

↓

Analytical Marts

↓

Power BI Semantic Model

## Core Design Principles

- Preserve source data lineage
- Separate ingestion from transformation
- Maintain historical business changes
- Apply dimensional modeling for analytics
- Validate data quality before reporting

## Key Engineering Challenges

1. Multi-source FMCG data integration
2. Sales target version management
3. Employee SCD Type 2
4. Distributor SCD Type 2
5. Business metric consistency
