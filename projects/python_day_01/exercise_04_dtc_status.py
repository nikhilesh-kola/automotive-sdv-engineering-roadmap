ecu = str(input("Enter ECU name: "))
dtc_count = int(input("Enter DTC count: "))
dtc_present = bool(dtc_count > 0)

print(f"\nECU: {ecu}")
print(f"DTC Count: {dtc_count}")
print(f"DTC Present: {dtc_present}")