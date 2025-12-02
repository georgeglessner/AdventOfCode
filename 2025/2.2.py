import re 
import math

finalSum = 0

PATTERN_ALL_SAME = re.compile(r'^(\d)\1*$')
PATTERN_TWO_DIGIT_REPEAT = re.compile(r'^(\d{2})\1+$')
PATTERN_THREE_DIGIT_REPEAT = re.compile(r'^(\d{3})\1+$')

with open("input.txt", "r") as f:
    ranges = [x.split("-") for x in f.read().split(",")]

'''
odd
  - all same
  - broke up in 3

even 
  - half and half
  - broke up in 2
'''
for x in ranges:
  for y in range(int(x[0]), int(x[1])+1):
    rangeStr = str(y)
    strLen = len(rangeStr)
    if strLen < 2: continue
    if (strLen % 2 == 0):
      half = strLen // 2
      if (rangeStr[:half] == rangeStr[half:]):
        finalSum += y
        continue
      elif half > 1:
        if PATTERN_TWO_DIGIT_REPEAT.match(rangeStr):
          finalSum += y
          continue
    else:
      chunk = strLen // 3
      if PATTERN_ALL_SAME.match(rangeStr):
        finalSum += y
        continue
      elif chunk > 2:
        if PATTERN_THREE_DIGIT_REPEAT.match(rangeStr):
          finalSum += y
          continue

print(finalSum)
