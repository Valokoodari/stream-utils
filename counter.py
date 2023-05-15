import sys
import os.path

if len(sys.argv) < 2:
    print("Please include a file name")
    sys.exit()

counter = 0
text = "Deaths:"
filename = sys.argv[1]

if os.path.isfile(filename):
    with open(filename, "r") as f:
        text, counter = f.read().strip().rsplit(" ", 1)
        counter = int(counter) + 1

with open(filename, "w") as f:
    f.write(f"{' ' if counter < 10 else ''}{text} {counter}")
