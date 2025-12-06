import re 
import math

finalSum = 0


with open("input.txt", "r") as f:
    problems = [[p for p in x.strip().split(" ") if p != ""] for x in f.readlines()]

problemLength = len(problems)
rowLength = len(problems[0])

for index in range(rowLength):
    rowEval = ""
    for entry in range(0, len(problems)-1):
        if entry > 0:
            rowEval += problems[problemLength-1][index]
        rowEval += problems[entry][index]
    finalSum += eval(rowEval)

print(finalSum)

