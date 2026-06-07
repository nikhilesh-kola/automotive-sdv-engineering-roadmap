def calculate_stats(values):
    """Calculating min, max and avg values of a list"""
    minimum = min(values)
    maximum = max(values)
    average = sum(values) / len(values)
    return minimum, maximum, average
