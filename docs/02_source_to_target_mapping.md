# Source To Target Mapping

## Source Systems

The project integrates 10 operational datasets:

| Source | Dataset | Format | Business Domain |
|---|---|---|---|
| SRC01 | sales_transactions | CSV | Sales |
| SRC02 | sales_target_plan | XLSX | Sales Planning |
| SRC03 | customer_master | CSV | Customer |
| SRC04 | product_master | XLSX/XLSM | Product |
| SRC05 | distributor_orders | XLSX/XLSB | Distribution |
| SRC06 | distributor_master | CSV | Distribution |
| SRC07 | employee_master | XLSX | HR |
| SRC08 | territory_mapping | XLSX | Sales Organization |
| SRC09 | return_transactions | CSV | Sales |
| SRC10 | promotion_program | XLSX | Marketing |

## Layer Mapping

Source data will flow through:

SOURCE → BRONZE → SILVER → GOLD → DATA MART → POWER BI

Detailed column-level mapping will be added after source profiling.
