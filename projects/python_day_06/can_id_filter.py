import csv


def filter_records_by_can_id(input_file_path, target_can_id):
    """Return all CSV records that match the target CAN ID."""
    filtered_records = []

    with open(input_file_path, "r") as input_file:
        reader = csv.DictReader(input_file)

        for row in reader:
            if row["can_id"] == target_can_id:
                filtered_records.append(row)

    return filtered_records


def write_records_to_csv(output_file_path, records):
    """Write filtered CAN records to a new CSV file."""
    fieldnames = ["timestamp", "can_id", "dlc", "payload"]

    with open(output_file_path, "w", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)

        writer.writeheader()

        for record in records:
            writer.writerow(record)


input_file_path = "projects/python_day_06/can_log.csv"
output_file_path = "projects/python_day_06/can_log_0x300.csv"
target_can_id = "0x300"

filtered_records = filter_records_by_can_id(input_file_path, target_can_id)

write_records_to_csv(output_file_path, filtered_records)

print("CAN ID Filter Report")
print("--------------------")
print(f"Input file: {input_file_path}")
print(f"Target CAN ID: {target_can_id}")
print(f"Filtered records: {len(filtered_records)}")
print(f"Output file: {output_file_path}")