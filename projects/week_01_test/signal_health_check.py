engine_temp_values = [70, 75, 82, 90, 96, 105]

minimum_temperature = min(engine_temp_values)
maximum_temperature = max(engine_temp_values)
average_temperature = sum(engine_temp_values) / len(engine_temp_values)

overheat_detected = maximum_temperature > 100

print("\nEngine Temperature Health Check")
print("---------------------------------")
print(f"Minimum temperature: {minimum_temperature:.2f} °C")
print(f"Maximum temperature: {maximum_temperature:.2f} °C")
print(f"Average temperature: {average_temperature:.2f} °C")
print(f"Overheat detected: {overheat_detected}")