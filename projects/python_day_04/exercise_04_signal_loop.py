signals = {
    "speed_kmh": [0, 20, 40, 60],
    "battery_voltage": [12.5, 12.3, 12.1, 12.0],
    "engine_temp": [35, 45, 60, 80]
}

for signal_name, values in signals.items():
    minimum = min(values)
    maximum = max(values)
    average = sum(values) / len(values)
    print(f"\n{signal_name}")
    print("-" * len(signal_name))
    print(f"Min: {minimum:.2f}")
    print(f"Max: {maximum:.2f}")
    print(f"Avg: {average:.2f}")