import csv

csv_file_path = "projects/python_day_06/can_log.csv"

message_counts = {}

with open(csv_file_path, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        can_id = row["can_id"]

        if can_id not in message_counts:
            message_counts[can_id] = 0

        message_counts[can_id] = message_counts[can_id] + 1

print("CAN Message Count Report")
print("------------------------")

for can_id, count in message_counts.items():
    if count == 1:
        print(f"{can_id}: {count} message")
    else:
        print(f"{can_id}: {count} messages")