### ============================================================================
### Advent of Code 
### ============================================================================
import pandas as pd
import numpy as np
import math
### ============================================================================

# Part One

data_input = 'data_input/aoc_input12.txt'

with open(data_input) as f:
    content = f.readlines()
    
cave_connections = []

for line in content:
    start,end = line.strip().split('-')
    cave_connections.append({start,end})

cave_loc = ['start']
end = False
while not end:
    for path_pair in cave_connections:
        if cave_loc[-1] in path_pair:
            cave_loc.append((path_pair - {cave_loc[-1]}).pop())
            if cave_loc[-1] == 'end':
                end = True
            if cave_loc[-1] == 'start':
                break
            if cave_loc[-1].islower() and cave_loc[-1] in cave_loc[:-1]:
                break
            print(cave_loc)

        
       
# Part Two



### ============================================================================
### END OF PROGRAM
### ============================================================================

