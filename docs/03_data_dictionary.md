# VietDist Data Dictionary

## Purpose

This document defines the metadata dictionary for the VietDist Sales & Distribution Analytics Platform.

The dictionary connects business meaning, source attributes, analytical usage and future warehouse modeling decisions.

---

# Source Metadata Dictionary

| Source | Domain | Grain | Warehouse Usage |
|---|---|---|---|
| SRC01 Sales Transactions | Sales | One row per sales transaction | fact_sales |
| SRC02 Sales Target Plan | Planning | One row per employee/target version/period | fact_sales_target |
| SRC03 Customer Master | Customer | One row per customer | dim_customer |
| SRC04 Product Master | Product | One row per product | dim_product |
| SRC05 Distributor Orders | Distributor Sales | One row per distributor order | fact_distributor_order |
| SRC06 Distributor Master | Distributor | One row per distributor | dim_distributor |
| SRC07 Employee Master | Employee | One row per employee version | dim_employee |
| SRC08 Territory Mapping | Territory | One row per ownership mapping period | bridge_territory_assignment |
| SRC09 Return Transactions | Return | One row per return transaction | fact_return |
| SRC10 Promotion Program | Promotion | One row per promotion program | dim_promotion |

---

# Key Business Entities

## SRC01 Sales Transactions

Business Purpose:
Capture transactional sales activities for revenue, sales performance and target comparison.

Expected Key Fields:

| Column | Data Role | Description |
|---|---|---|
| order_id | Primary Key | Unique sales transaction identifier |
| customer_id | Foreign Key | Customer reference |
| product_id | Foreign Key | Product reference |
| employee_id | Foreign Key | Sales representative ownership |
| quantity | Measure | Sold quantity |
| sales_amount | Measure | Sales value |

---

## SRC02 Sales Target Plan

Business Purpose:
Support target achievement analysis and historical target comparison.

Key Concepts:

| Attribute | Description |
|---|---|
| plan_version | Target revision identifier |
| effective_from | Start date of validity |
| effective_to | End date of validity |
| target_amount | Planned sales target |

---

## SRC03 Customer Master

Business Purpose:
Provide customer attributes for segmentation and performance analysis.

Key Attributes:

- customer_id
- customer_name
- customer_type
- location
- channel

---

## SRC04 Product Master

Business Purpose:
Provide product hierarchy for sales analytics.

Key Attributes:

- product_id
- product_name
- category
- sub_category

---

# Data Quality Rules

| Rule | Description |
|---|---|
| Primary Key Integrity | Business keys must be unique |
| Referential Integrity | Foreign keys must exist in master data |
| Completeness | Mandatory analytical fields should not be missing |
| Validity | Dates, quantities and amounts must follow business rules |

---

# Update Strategy

Future phases will extend this dictionary with:

- Complete column-level metadata
- Actual data types
- Source-to-target mappings
- Silver transformation rules
- Gold warehouse definitions
