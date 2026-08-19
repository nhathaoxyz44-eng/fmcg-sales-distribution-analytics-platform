# SRC05 Distributor Orders Profiling

## Dataset Overview

Business Purpose: Capture distributor order activities.

## Warehouse Usage

Recommended target: `fact_distributor_orders`

Key relationships:
- distributor_id -> dim_distributor
- product_id -> dim_product

## Silver Transformation Considerations

- Validate distributor references
- Standardize order status
- Prepare distributor performance metrics
