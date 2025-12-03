import re 
import math

finalSum = 0

with open("input.txt", "r") as f:
    entries = [x.strip() for x in f.readlines()]

for x in entries:
    lineLengh = len(x)
    maxNum=0
    for y in range(lineLengh):
        for z in range(y+1, lineLengh):
            if int(x[y] + x[z]) > maxNum:
                maxNum = int(x[y] + x[z])
    finalSum+=maxNum

print(finalSum)
