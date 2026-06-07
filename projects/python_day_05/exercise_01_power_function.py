def calculate_power(voltage, current):
    """Calculate power in watts."""
    power = voltage * current
    return power

battery_voltage = 12.5
battery_current = 4.0

power_result = calculate_power(battery_voltage, battery_current)

print(f"Power: {power_result:.2f} W")