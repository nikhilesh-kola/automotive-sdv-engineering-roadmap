import csv
import sys


def calculate_stats(values):
    minimum = min(values)
    maximum = max(values)
    average = sum(values) / len(values)
    return minimum, maximum, average


def print_stats(signal_name, unit, values):
    minimum, maximum, average = calculate_stats(values)

    print(f"\n{signal_name}")
    print("-" * len(signal_name))
    print(f"Min: {minimum:.2f} {unit}")
    print(f"Max: {maximum:.2f} {unit}")
    print(f"Avg: {average:.2f} {unit}")


if len(sys.argv) != 2:
    print("Usage: python csv_signal_analyzer_v2.py <csv_file_path>")
    sys.exit(1)

csv_file_path = sys.argv[1]

speed_values = []
battery_voltage_values = []
engine_temp_values = []

try:
    with open(csv_file_path, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            speed_values.append(float(row["speed_kmh"]))
            battery_voltage_values.append(float(row["battery_voltage"]))
            engine_temp_values.append(float(row["engine_temp"]))

    if len(speed_values) == 0:
        print("Error: CSV file contains no data rows.")
        sys.exit(1)

    print("Vehicle Signal Analysis")
    print("-----------------------")

    print_stats("Speed", "km/h", speed_values)
    print_stats("Battery Voltage", "V", battery_voltage_values)
    print_stats("Engine Temperature", "°C", engine_temp_values)

except FileNotFoundError:
    print(f"Error: File not found: {csv_file_path}")
    print("Please check the CSV file path and try again.")

except KeyError as error:
    print(f"Error: Missing expected column: {error}")
    print("Required columns: speed_kmh, battery_voltage, engine_temp")

except ValueError:
    print("Error: One or more CSV values could not be converted to a number.")
    print("Please check that signal values are numeric.")