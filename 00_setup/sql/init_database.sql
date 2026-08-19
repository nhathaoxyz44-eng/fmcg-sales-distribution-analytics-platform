-- VietDist Analytics Engineering Platform
-- Database schemas

CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS dwh;
CREATE SCHEMA IF NOT EXISTS mart;

COMMENT ON SCHEMA raw IS 'Bronze layer - raw ingested data';
COMMENT ON SCHEMA staging IS 'Silver layer - cleaned and standardized data';
COMMENT ON SCHEMA dwh IS 'Gold layer - dimensional warehouse';
COMMENT ON SCHEMA mart IS 'Business analytical marts';
