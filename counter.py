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
        text, counter = f.read().rsplit(" ", 1)
        counter = int(counter)

with open(filename, "w") as f:
    f.write(f"{text} {counter + 1}")
