{{ config (materialized='table') }}

SELECT
	CAST(timestamp AS TIMESTAMP) AS logged_at,
	temperature_c,
	humidity_percent,
	pressure_hpa
FROM read_json_auto('/home/earl123/climate_pipeline/raw_data/*.jsonl')
