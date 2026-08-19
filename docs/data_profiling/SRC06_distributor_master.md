# SRC06 Distributor Master Profiling

## Dataset Overview

Business Purpose: Maintain distributor information for distribution analytics.

## Warehouse Usage

Recommended target: `dim_distributor`

Key attributes:
- distributor_id
- distributor_name
- region
- tier

## Silver Transformation Considerations

- Validate distributor identifiers
- Standardize geographic attributes
- Preserve distributor history when changes occur
