import csv


def read_can_log(csv_file_path):
    """Read a CAN log CSV file and return a list of records."""
    records = []

    with open(csv_file_path, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            records.append(row)

    return records


def count_messages_by_can_id(records):
    """Count how many messages appear for each CAN ID."""
    message_counts = {}

    for record in records:
        can_id = record["can_id"]

        if can_id not in message_counts:
            message_counts[can_id] = 0

        message_counts[can_id] = message_counts[can_id] + 1

    return message_counts


csv_file_path = "projects/python_day_06/can_log.csv"

records = read_can_log(csv_file_path)
message_counts = count_messages_by_can_id(records)

print("Bug-Fix Message Counts")
print("----------------------")

for can_id, count in message_counts.items():
    print(f"{can_id}: {count} messages")