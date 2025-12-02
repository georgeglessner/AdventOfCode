import re 
import math

finalSum = 0

# f = open("input.txt", "r").readlines()
f = [line.rstrip() for line in open('input.txt')]
# f = [line.rstrip() for line in open('example.txt')]

numZeros = 0
current = 50
skip = False

for x in f:
    dir = x[0].upper()
    num = int(x[1:])

    if dir == "L":
        prev = current
        current -= num
        if current < 0:
            skip = True
            if current > -100 and prev != 0:
                numZeros+=1
            elif prev != 0:
                numZeros += int(abs(current)/100) + 1
            else:
                numZeros += int(abs(current)/100)
            current = (100+current)%100
    elif dir == "R":
        prev = current
        current += num
        if current > 99:
            skip = True
            if current < 200 and prev != 0:
                numZeros += 1
            else:
                numZeros+=int(current/100)
            current = (current-100)%100

    if current == 0 and not skip:
        numZeros+=1

    skip = False

print(numZeros)