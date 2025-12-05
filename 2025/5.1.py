import re 
import math

finalSum = 0
entriesRemoved = False

PATTERN_RANGE = re.compile(r'(\d+)-(\d+)')
PATTERN_ID = re.compile(r'(\d+)')

ranges = []
ids = []

with open("input.txt", "r") as f:
    for x in f.readlines():
        if PATTERN_RANGE.match(x):
            start, end = map(int, x.strip().split("-"))
            ranges.append([start, end])
        elif PATTERN_ID.match(x):
            ids.append(int(x.strip()))

for id in ids:
    for range in ranges:
        if id >= range[0] and id <= range[1]:
            finalSum += 1
            break

print(finalSum)

