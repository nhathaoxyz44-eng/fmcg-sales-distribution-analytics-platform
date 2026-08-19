# SRC09 Return Transactions Profiling

## Dataset Overview

Business Purpose: Capture returned sales transactions for net revenue analysis.

## Warehouse Usage

Recommended target: `fact_returns`

Business Rule:

Net Revenue = Sales Amount - Return Amount

## Silver Transformation Considerations

- Validate original transaction references
- Standardize return reasons
- Reconcile with sales transactions
