def is_over_limit(value, limit):
    """Return True if value is greater than limit."""
    result = value > limit
    return result

engine_temp = 105
temperature_limit = 100

threshold_limit = is_over_limit(engine_temp, temperature_limit)

print(f"Over limit: {threshold_limit}")