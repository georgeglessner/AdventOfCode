'''
https://www.reddit.com/r/adventofcode/comments/1peyw7w/2025_day_5_part_3_superfresh_ingredients/

The Elves are very happy and insist that you enjoy a hot drink in their warm and cosy cafeteria. 
Of course, you accept their generous offer and you start relaxing. 
You are at the exact moment before falling asleep, when the mind wanders. 
You see escalators filled with rolls of paper, ingredients dancing with an open safe. 
You even imagine super-fresh ingredients!

A super-fresh ingredient is an ingredient that appears in two or more ranges.

Consider the example:

3-5
10-14
16-20
12-18

The ingredients 12, 13 and 14 appear in the ranges 10-14 and 12-18. 
The ingredients 16, 17, 18 appear in the ranges 16-20 and 12-18. 
So there are 6 super-fresh ingredients in this example.

How many super-fresh ingredients do you count in your input file?
'''
import re 

finalSum = 0
entriesRemoved = False

PATTERN_RANGE = re.compile(r'(\d+)-(\d+)')

ranges = []

with open("input.txt", "r") as f:
    for x in f.readlines():
        if PATTERN_RANGE.match(x):
            start, end = map(int, x.strip().split("-"))
            ranges.append([start, end])

ranges.sort()

for index, range in enumerate(ranges):
    if index == len(ranges)-1:
        break
    
    if ranges[index+1][0] >= range[0] and ranges[index+1][0] <= range[1]:
        finalSum+=range[1]-ranges[index+1][0]+1

print(finalSum)

