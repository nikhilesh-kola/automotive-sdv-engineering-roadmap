def calculate_stats(values):
    """Calculating min, max and avg values of a list"""
    minimum = min(values)
    maximum = max(values)
    average = sum(values) / len(values)
    return minimum, maximum, average

engine_temp_values = [70, 75, 82, 90, 96, 105]

temp_min, temp_max, temp_avg = calculate_stats(engine_temp_values)

print("Engine Temperature Stats")
print("------------------------")
print(f"Min: {temp_min:.2f} °C")
print(f"Max: {temp_max:.2f} °C")
print(f"Avg: {temp_avg:.2f} °C")