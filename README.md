# Edge IoT Data Pipeline: Raspberry Pi 5

An end-to-end local data engineering pipeline running entirely on a Raspberry Pi 5. This project captures physical environment data, transforms it using modern analytics tools, and serves it to an enterprise-grade dashboard without relying on cloud infrastructure.

## Architecture

1. **Hardware Ingestion:** A BME280 sensor wired via I2C captures room temperature, humidity, and pressure. A scheduled Python script extracts this data and logs it as raw JSON lines.
2. **Data Transformation (dbt + DuckDB):** dbt is used to execute SQL models directly against the raw JSON files. It casts types, runs tests, and materialises aggregated hourly metrics into a local DuckDB analytical database.
3. **Visualisation (Grafana):** A Dockerised Grafana instance reads directly from the DuckDB file to serve a live time-series dashboard.

## Tech Stack
* **Hardware:** Raspberry Pi 5, BME280 Environmental Sensor
* **Languages:** Python, SQL
* **Data Core:** DuckDB, dbt (Data Build Tool)
* **Infrastructure:** Docker, Linux `cron`
* **Visualisation:** Grafana

## Why this architecture?
By processing the data locally on the edge device using DuckDB, we eliminate the network latency and cloud compute costs associated with streaming raw IoT data directly to a cloud data warehouse. Only aggregated, analytical-ready data is stored and visualised.
<img width="4080" height="3072" alt="PXL_20260805_184648902" src="https://github.com/user-attachments/assets/88791041-ab50-4164-9dc9-58024365f115" />
