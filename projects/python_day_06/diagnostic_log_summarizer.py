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


def get_first_timestamp(records):
    """Return the first timestamp from the CAN log."""
    if len(records) == 0:
        return None

    return records[0]["timestamp"]


def get_last_timestamp(records):
    """Return the last timestamp from the CAN log."""
    if len(records) == 0:
        return None

    return records[-1]["timestamp"]


def get_top_active_ids(message_counts, limit):
    """Return the most active CAN IDs based on message count."""
    sorted_counts = sorted(
        message_counts.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return sorted_counts[:limit]


def print_summary(csv_file_path, records, message_counts):
    """Print a diagnostic log summary report."""
    total_messages = len(records)
    first_timestamp = get_first_timestamp(records)
    last_timestamp = get_last_timestamp(records)
    top_active_ids = get_top_active_ids(message_counts, 3)

    print("Diagnostic Log Summary")
    print("----------------------")
    print(f"Input file: {csv_file_path}")
    print(f"Total messages: {total_messages}")
    print(f"First timestamp: {first_timestamp}")
    print(f"Last timestamp: {last_timestamp}")

    print("\nMessage Counts per CAN ID")
    print("-------------------------")

    for can_id, count in message_counts.items():
        if count == 1:
            print(f"{can_id}: {count} message")
        else:
            print(f"{can_id}: {count} messages")

    print("\nTop Active CAN IDs")
    print("------------------")

    for index, item in enumerate(top_active_ids, start=1):
        can_id = item[0]
        count = item[1]

        if count == 1:
            print(f"{index}. {can_id} - {count} message")
        else:
            print(f"{index}. {can_id} - {count} messages")


csv_file_path = "projects/python_day_06/can_log.csv"

records = read_can_log(csv_file_path)
message_counts = count_messages_by_can_id(records)

print_summary(csv_file_path, records, message_counts)