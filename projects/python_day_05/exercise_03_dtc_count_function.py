def count_dtcs(dtc_codes):
    """Count the number of DTC codes."""
    count = len(dtc_codes)
    return count

dtc_codes = ["P0300", "P0420", "U0100"]

dtc_count = count_dtcs(dtc_codes)

print(f"DTC Count: {dtc_count}")