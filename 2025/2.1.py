import re 
import math

finalSum = 0

with open("input.txt", "r") as f:
    ranges = [x.split("-") for x in f.read().split(",")]

for x in ranges:
  for y in range(int(x[0]), int(x[1])+1):
    strLen = len(str(y))
    rangeStr = str(y)
    if (strLen % 2 == 0):
      half = strLen // 2
      if (rangeStr[:half] == rangeStr[half:]):
        finalSum += y

print(finalSum)
