battery_voltage_values = [12.4, 12.3, 12.2, 12.1, 12.0]

minimum_voltage = min(battery_voltage_values)
maximum_voltage = max(battery_voltage_values)
average_voltage = sum(battery_voltage_values) / len(battery_voltage_values)

print("Battery Voltage Analysis")
print("------------------------")
print(f"Minimum voltage: {minimum_voltage:.2f} V")
print(f"Maximum voltage: {maximum_voltage:.2f} V")
print(f"Average voltage: {average_voltage:.2f} V")