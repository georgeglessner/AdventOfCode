import re 
import math

finalSum = 0

# f = open("input.txt", "r").readlines()
# f = [line.rstrip() for line in open('input.txt')]
f = [line.rstrip() for line in open('example.txt')]

numZeros = 0
current = 50

for x in f:
    dir = x[0].upper()
    num = int(x[1:])

    if dir == "L":
        current -= num
        if current < 0:
            current = (100+current)%100
    elif dir == "R":
        current += num
        if current > 99:
            current = (current-100)%100        
    
    if current == 0:
        numZeros+=1

print(numZeros)