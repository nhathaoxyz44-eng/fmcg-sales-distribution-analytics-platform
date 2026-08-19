# SRC01 Sales Transactions Profiling

## Dataset Overview

Business Purpose: Capture FMCG sales transaction records for revenue and performance analysis.

Expected Usage:
- Sales performance analysis
- Revenue calculation
- Employee and product performance

## Profiling Scope

The dataset is assessed for:
- Structure and metadata
- Completeness
- Uniqueness
- Validity
- Relationship readiness

## Warehouse Usage

Recommended target: `fact_sales`

Key relationships:
- customer_id -> dim_customer
- product_id -> dim_product
- employee_id -> dim_employee

## Silver Transformation Considerations

- Standardize date formats
- Validate business keys
- Apply revenue calculation rules
- Handle return transactions separately
