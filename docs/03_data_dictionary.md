# VietDist Data Dictionary

## Purpose

This document defines the data dictionary framework for the VietDist Sales & Distribution Analytics Platform.

The data dictionary will be continuously updated during the source profiling and data modeling phases.

---

# Data Dictionary Structure

| Source/Table | Column | Data Type | Business Meaning | Key Type | Transformation Rule |
|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD | TBD |

---

# Planned Data Domains

## 1. Sales Transactions (SRC01)

Business Purpose:

Capture detailed sales transactions used for revenue analysis, sales performance tracking and target comparison.

Expected Attributes:

- Transaction identifier
- Transaction date
- Customer information
- Product information
- Sales quantity
- Revenue value
- Employee ownership

---

## 2. Sales Target Planning (SRC02)

Business Purpose:

Store sales target plans and support historical target version comparison.

Expected Attributes:

- Target period
- Employee/territory assignment
- Target amount
- Target version
- Effective period

---

## 3. Customer Master (SRC03)

Business Purpose:

Maintain customer master information for customer performance analytics.

Expected Attributes:

- Customer identifier
- Customer name
- Customer segment
- Location

---

## 4. Product Master (SRC04)

Business Purpose:

Provide product hierarchy and product attributes for sales analysis.

Expected Attributes:

- Product identifier
- Product category
- Brand
- Unit price

---

## 5. Distributor Domain (SRC05, SRC06)

Business Purpose:

Support distributor order analysis and distributor performance reporting.

Expected Attributes:

- Distributor identifier
- Distributor level
- Region
- Order information

---

## 6. Employee Domain (SRC07, SRC08)

Business Purpose:

Support sales representative performance analysis and historical organizational tracking.

Expected Attributes:

- Employee identifier
- Sales team
- Territory
- Effective date

---

## 7. Return Transactions (SRC09)

Business Purpose:

Capture returned products for net sales calculation.

Expected Attributes:

- Return identifier
- Original transaction reference
- Return quantity
- Return value

---

## 8. Promotion Program (SRC10)

Business Purpose:

Analyze promotion effectiveness and sales impact.

Expected Attributes:

- Promotion identifier
- Promotion period
- Promotion type
- Product coverage

---

# Update Strategy

This document will be enhanced after Phase 2 Data Profiling with:

- Actual column names
- Data types
- Primary keys
- Foreign keys
- Nullability
- Data quality rules
- Source-to-target mappings
