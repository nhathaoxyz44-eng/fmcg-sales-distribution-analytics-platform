# Data Issues Log

## Purpose

This document tracks data quality issues, business rule gaps, and technical risks discovered during the VietDist Analytics Engineering project.

The objective is to ensure all data issues are documented with impact assessment and resolution plans before production reporting.

---

## Issue Tracking Template

| Issue ID | Source | Issue Description | Impact | Resolution Status |
|---|---|---|---|---|
| DATA-001 | SRC01 Sales Transactions | Pending profiling | To be assessed | Open |

---

## Expected Issue Categories

### 1. Data Completeness

Examples:
- Missing mandatory business keys
- Missing transaction dates
- Missing employee/customer references

### 2. Data Consistency

Examples:
- Different naming conventions across sources
- Inconsistent region/team values
- Duplicate master records

### 3. Referential Integrity

Examples:
- Sales transaction references missing customer
- Distributor orders reference unknown distributor
- Product codes missing from product master

### 4. Business Rule Validation

Examples:
- Negative quantities
- Invalid revenue values
- Incorrect target periods

### 5. Historical Data Management

Examples:
- Employee attribute changes requiring SCD Type 2
- Distributor attribute changes requiring SCD Type 2
- Sales target version conflicts

---

## Current Known Risks

| Risk | Description | Treatment |
|---|---|---|
| Inventory source unavailable | BRD contains inventory requirements but no inventory dataset is provided | Excluded from MVP until source availability is confirmed |
| Customer churn definition unclear | Business definition has not been finalized | Pending business clarification |
| Distributor target source unclear | Target comparison requires confirmation of distributor target structure | Pending business clarification |
