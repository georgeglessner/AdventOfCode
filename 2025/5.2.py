import re 
import math

finalSum = 0
entriesRemoved = False

PATTERN_RANGE = re.compile(r'(\d+)-(\d+)')

ranges = []
final_ranges = []

with open("input.txt", "r") as f:
    for x in f.readlines():
        if PATTERN_RANGE.match(x):
            start, end = map(int, x.strip().split("-"))
            ranges.append([start, end])

ranges.sort()

for range in ranges:
    if len(final_ranges) == 0:
        final_ranges.append(range)
        continue
    merged = False
    for index, f_range in enumerate(final_ranges):
        if not (range[1] < f_range[0] or range[0] > f_range[1]):
            final_ranges[index] = [min(range[0], f_range[0]), max(range[1], f_range[1])]
            merged = True
            break
    if not merged:
        final_ranges.append(range)

for final in final_ranges:
    finalSum += final[1] - final[0] + 1 # inclusive
print(finalSum)
