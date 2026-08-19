# VietDist Business Requirement Matrix

## Project Objective

Build an end-to-end analytics platform for VietDist FMCG distribution business by integrating multi-source operational data into PostgreSQL using Medallion Architecture and serving analytics through Power BI.

## Requirement Mapping

| Requirement Area | Business Need | Main Sources | Target Output |
|---|---|---|---|
| Sales Performance | Monitor revenue, achievement, growth | SRC01, SRC02, SRC09 | Sales Analytics Mart |
| Sales Target Versioning | Compare actual sales against different planning versions | SRC02 | Temporal Target Model |
| Product Performance | Analyze product contribution | SRC01, SRC04 | Product Analytics |
| Employee Performance | Historical sales ownership analysis | SRC01, SRC07, SRC08 | SCD2 Employee Dimension |
| Distributor Performance | Evaluate distributor effectiveness | SRC05, SRC06 | Distributor Analytics Mart |
| Promotion Analysis | Measure promotion effectiveness | SRC01, SRC10 | Promotion Analytics |

## Out of Scope / Pending

- Inventory analytics requires additional inventory source data.
- Customer churn requires business definition confirmation.
