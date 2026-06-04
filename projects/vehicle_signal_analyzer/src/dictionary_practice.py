signals = {
    "speed_kmh": [0, 10, 25, 40],
    "battery_voltage": [12.4, 12.3, 12.2, 12.1]
}

speed_values = signals["speed_kmh"]
battery_values = signals["battery_voltage"]

speed_avg = sum(speed_values) / len(speed_values)
battery_avg = sum(battery_values) / len(battery_values)

print("Dictionary Practice")
print("-------------------")
print(f"Speed average: {speed_avg:.2f} km/h")
print(f"Battery voltage average: {battery_avg:.2f} V")