# SRC03 Customer Master Profiling

## Dataset Overview

Business Purpose: Maintain customer master data for sales and customer analytics.

## Warehouse Usage

Recommended target: `dim_customer`

Key attributes:
- customer_id
- customer_type
- channel
- location
- status

## Data Quality Focus

- Validate customer_id uniqueness
- Monitor missing descriptive attributes
- Standardize customer classifications

## Silver Transformation Considerations

- Clean master attributes
- Preserve customer history when required
