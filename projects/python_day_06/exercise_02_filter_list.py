records = [
    {"timestamp": "0.000", "can_id": "0x100", "dlc": "8"},
    {"timestamp": "0.010", "can_id": "0x200", "dlc": "8"},
    {"timestamp": "0.020", "can_id": "0x100", "dlc": "8"},
    {"timestamp": "0.030", "can_id": "0x300", "dlc": "4"},
]

target_can_id = "0x100"
filtered_records = []

for record in records:
    if record["can_id"] == target_can_id:
        filtered_records.append(record)

print("Filtered Records")
print("----------------")

for record in filtered_records:
    print(record)