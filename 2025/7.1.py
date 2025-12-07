import re 
import math

finalSum = 0
  
with open("input.txt", "r") as f:
  lines = f.readlines()
  # Find "S" in the first line
  start = re.search("S", lines[0])
  start_pos = start.span(0)[0] if start else None

# beams = {start_pos}
currentBeams = set()
currentBeams.add(start_pos)

for x in lines:
    for y in currentBeams.copy():
      if x[y] == "^":
        finalSum+=1
        # the beam stops
        currentBeams.remove(y)
        # add right beam
        if y+1 <= len(x):
          currentBeams.add(y+1)
        # add left beam
        if y-1 >= 0:
          currentBeams.add(y-1)
print(finalSum)
