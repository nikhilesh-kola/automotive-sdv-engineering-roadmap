import csv

speed_values = []
battery_voltage_values = []
engine_temp_values = []

with open("projects/python_day_02/vehicle_signals.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        speed_values.append(float(row["speed_kmh"]))
        battery_voltage_values.append(float(row["battery_voltage"]))
        engine_temp_values.append(float(row["engine_temp"]))

speed_min = min(speed_values)
speed_max = max(speed_values)
speed_avg = sum(speed_values) / len(speed_values)

battery_min = min(battery_voltage_values)
battery_max = max(battery_voltage_values)
battery_avg = sum(battery_voltage_values) / len(battery_voltage_values)

temp_min = min(engine_temp_values)
temp_max = max(engine_temp_values)
temp_avg = sum(engine_temp_values) / len(engine_temp_values)

print("Vehicle Signal Analysis")
print("-----------------------")

print("\nSpeed")
print("-----")
print(f"Min: {speed_min:.2f} km/h")
print(f"Max: {speed_max:.2f} km/h")
print(f"Avg: {speed_avg:.2f} km/h")

print("\nBattery Voltage")
print("---------------")
print(f"Min: {battery_min:.2f} V")
print(f"Max: {battery_max:.2f} V")
print(f"Avg: {battery_avg:.2f} V")

print("\nEngine Temperature")
print("------------------")
print(f"Min: {temp_min:.2f} °C")
print(f"Max: {temp_max:.2f} °C")
print(f"Avg: {temp_avg:.2f} °C")