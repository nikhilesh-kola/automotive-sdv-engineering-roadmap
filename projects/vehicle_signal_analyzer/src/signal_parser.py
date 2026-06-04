import csv
import sys


def read_numeric_signals(csv_file_path):
    signals = {}

    with open(csv_file_path, "r") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            raise ValueError("CSV file has no header row.")

        for column_name in reader.fieldnames:
            signals[column_name] = []

        for row in reader:
            for column_name in reader.fieldnames:
                value = float(row[column_name])
                signals[column_name].append(value)

    return signals


def calculate_stats(values):
    minimum = min(values)
    maximum = max(values)
    average = sum(values) / len(values)
    return minimum, maximum, average


def print_signal_report(signals):
    print("Vehicle Signal Analyzer")
    print("-----------------------")

    for signal_name, values in signals.items():
        if len(values) == 0:
            continue

        minimum, maximum, average = calculate_stats(values)

        print(f"\n{signal_name}")
        print("-" * len(signal_name))
        print(f"Min: {minimum:.2f}")
        print(f"Max: {maximum:.2f}")
        print(f"Avg: {average:.2f}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python signal_parser.py <csv_file_path>")
        sys.exit(1)

    csv_file_path = sys.argv[1]

    try:
        signals = read_numeric_signals(csv_file_path)
        print_signal_report(signals)

    except FileNotFoundError:
        print(f"Error: File not found: {csv_file_path}")

    except ValueError as error:
        print(f"Error: {error}")

    except KeyError as error:
        print(f"Error: Missing CSV column: {error}")


if __name__ == "__main__":
    main()