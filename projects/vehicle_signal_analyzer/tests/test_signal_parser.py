import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"
sys.path.append(str(SRC_PATH))

from signal_parser import calculate_stats


values = [10, 20, 30]

minimum, maximum, average = calculate_stats(values)

print("Testing calculate_stats()")
print("-------------------------")
print(f"Expected min: 10, Actual min: {minimum}")
print(f"Expected max: 30, Actual max: {maximum}")
print(f"Expected avg: 20, Actual avg: {average}")

if minimum == 10 and maximum == 30 and average == 20:
    print("Test result: PASS")
else:
    print("Test result: FAIL")