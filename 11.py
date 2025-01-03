import sys

# Check if exactly 2 arguments are passed
if len(sys.argv) != 3:
    print("Usage: python script.py <arg1> <arg2>")
    sys.exit(1)

# Get the command-line arguments
arg1 = sys.argv[1]
arg2 = sys.argv[2]

# Print each argument 10 times
for _ in range(10):
    print(arg1)
    print(arg2)
