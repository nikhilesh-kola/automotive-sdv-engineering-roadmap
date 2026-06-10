can_ids = ["0x100", "0x200", "0x100", "0x300", "0x200", "0x100"]

message_counts = {}

for can_id in can_ids:
    if can_id not in message_counts:
        message_counts[can_id] = 0

    message_counts[can_id] = message_counts[can_id] + 1

print("CAN Message Counts")
print("------------------")

for can_id, count in message_counts.items():
    print(f"{can_id}: {count} messages")