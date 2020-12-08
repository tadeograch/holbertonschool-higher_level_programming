#!/usr/bin/python3
print("00", end="")
for i in range(1, 100):
    if i / 10 > i % 10:
        continue
    print(", {:02d}".format(i), end="")
print("")