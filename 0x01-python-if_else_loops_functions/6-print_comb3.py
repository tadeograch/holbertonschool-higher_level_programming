#!/usr/bin/python3
print("01", end="")
for i in range(2, 100):
    if i / 10 > i % 10:
        continue
    print(", {:02d}".format(i), end="")
print("")
