# SRC02 Sales Target Plan Profiling

## Dataset Overview

Business Purpose: Store sales target planning versions for employee performance comparison.

## Key Business Concepts

- Plan versioning
- Effective period management
- Historical target comparison

## Warehouse Usage

Recommended target: `fact_sales_target`

Important attributes:
- employee_id
- plan_version
- effective_from
- effective_to
- target_value

## Silver Transformation Considerations

- Preserve historical versions
- Do not overwrite previous plans
- Validate effective date ranges
