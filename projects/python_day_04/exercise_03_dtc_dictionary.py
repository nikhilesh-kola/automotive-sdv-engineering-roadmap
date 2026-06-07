dtc_info = {
    "P0300": "Random misfire detected",
    "P0420": "Catalyst efficiency below threshold",
    "U0100": "Lost communication with ECM"
}

for dtc_code, dtc_description in dtc_info.items():
    print(f"{dtc_code}: {dtc_description}")