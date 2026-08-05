import smbus2
import bme280
import json
from datetime import datetime, timezone
import os

port = 1
address = 0x77
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)

def get_sensor_data():
	try:
		data = bme280.sample(bus, address, calibration_params)
		
		reading = {
			"timestamp": datetime.now(timezone.utc).isoformat(),
			"temperature_c": round(data.temperature, 2),
			"humidity_percent": round(data.humidity, 2),
			"pressure_hpa": round(data.pressure, 2)
		}
		return reading
	except Exception as e:
		print(f"Error reading sensor : {e}")
		return None

if __name__ == "__main__":
	os.makedirs("raw_data", exist_ok=True)

	date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
	filename = f"raw_data/{date_str}_readings.jsonl"

	reading=get_sensor_data()

	if reading:
		with open(filename, 'a') as f:
			f.write(json.dumps(reading) + '\n')
		
		print("Success! Logged the following:")
		print(json.dumps(reading, indent=2))

