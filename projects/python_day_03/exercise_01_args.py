import sys

if len(sys.argv) != 2:
    print("Usage: python exercise_01_args.py <name>")
else:
    name = sys.argv[1]
    print(f"Hello, {name}")