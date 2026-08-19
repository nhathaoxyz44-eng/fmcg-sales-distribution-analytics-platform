# SRC10 Promotion Program Profiling

## Dataset Overview

Business Purpose: Maintain promotion programs for effectiveness analysis.

## Warehouse Usage

Recommended target: `dim_promotion` and promotion analytics mart.

Important attributes:
- promotion_id
- promotion_type
- target_channel
- target_region
- cost

## Silver Transformation Considerations

- Validate promotion periods
- Standardize promotion categories
- Link promotions with sales performance
