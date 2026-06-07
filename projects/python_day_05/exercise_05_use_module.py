from signal_utils import calculate_stats

speed_values = [0, 20, 40, 60]

speed_min, speed_max, speed_avg = calculate_stats(speed_values)

print("Speed Stats")
print("-----------")
print(f"Min Speed: {speed_min:.2f} km/h")
print(f"Max Speed: {speed_max:.2f} km/h")
print(f"Avg Speed: {speed_avg:.2f} km/h")