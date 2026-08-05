{{ config(materialized='table') }}

SELECT 
    date_trunc('hour', logged_at) AS hour_bucket,
    ROUND(AVG(temperature_c), 2) AS avg_temperature,
    ROUND(AVG(humidity_percent), 2) AS avg_humidity,
    ROUND(AVG(pressure_hpa), 2) AS avg_pressure,
    COUNT(*) AS total_readings
FROM {{ ref('stg_climate_data') }}
GROUP BY 1
ORDER BY 1 DESC
