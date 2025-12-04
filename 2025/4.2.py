import re 
import math

finalSum = 0
entriesRemoved = False

with open("example.txt", "r") as f:
    entries = [x.strip() for x in f.readlines()]

def checkAdjacent(entries, y, index) -> bool:
    numAdjacent = 0
    # check above
    if index > 0:
        if entries[index-1][y] == "@":
            numAdjacent += 1
        if y > 0:
            if entries[index-1][y-1] == "@":
                numAdjacent += 1
        if y < len(entries[index-1])-1:
            if entries[index-1][y+1] == "@":
                numAdjacent += 1
    # check below
    if index < len(entries)-1:
        if entries[index+1][y] == "@":
            numAdjacent += 1
        if y > 0:
            if entries[index+1][y-1] == "@":
                numAdjacent += 1
        if y < len(entries[index+1])-1:
            if entries[index+1][y+1] == "@":
                numAdjacent += 1
    # check left
    if y > 0:
        if entries[index][y-1] == "@":
            numAdjacent += 1
    # check right
    if y < len(entries[index])-1:
        if entries[index][y+1] == "@":
            numAdjacent += 1
    
    
    return numAdjacent < 4 

def removeAdjacent(entries) -> bool:
    global finalSum
    global entriesRemoved
    for index, entry in enumerate(entries):
        for y in range(len(entry)):
            if entry[y] == "@":
                # can remove
                if checkAdjacent(entries, y, index):
                    finalSum += 1
                    entry_list = list(entries[index])
                    entry_list[y] = "."
                    entries[index] = ''.join(entry_list)
                    entriesRemoved = True
    if entriesRemoved:
        entriesRemoved = False
        removeAdjacent(entries)

removeAdjacent(entries)
print(finalSum)
