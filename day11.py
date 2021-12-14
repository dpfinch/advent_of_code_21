### ============================================================================
### Advent of Code 
### ============================================================================
import pandas as pd
import numpy as np
import math
### ============================================================================

# Part One

data_input = 'data_input/aoc_input11.txt'

with open(data_input) as f:
    contents = f.readlines()


octo_grid = np.zeros([10,10], dtype = int)

for n,line in enumerate(contents):
    octo_grid[n,:] = [int(x) for x in line.strip()]

pad_grid = np.pad(octo_grid,(1,1))

total_flashes = 0    
for step in range(100):
    pad_grid += 1
    flashed = flash_grid = np.zeros(pad_grid.shape)
    while sum(sum(pad_grid[1:11,1:11] >= 10)) > 0:
        
        for x in  range(1,11):
            for y in range(1,11):
                if pad_grid[x,y] >= 10:
                    total_flashes += 1
                    flashed[x,y] = 1
                    pad_grid[x-1:x+2,y-1:y+2] += 1
                      
        pad_grid[flashed == 1] = 0 
                        
print('Total number of flashes in 100 steps: {}'.format(total_flashes))
# Part Two

pad_grid = np.pad(octo_grid,(1,1))

total_flashes = 0
not_syncro = True
step_counter = 1
while not_syncro:
    pad_grid += 1
    flashed = flash_grid = np.zeros(pad_grid.shape)
    while sum(sum(pad_grid[1:11,1:11] >= 10)) > 0:
        
        for x in  range(1,11):
            for y in range(1,11):
                if pad_grid[x,y] >= 10:
                    total_flashes += 1
                    flashed[x,y] = 1
                    pad_grid[x-1:x+2,y-1:y+2] += 1
                 
        pad_grid[flashed == 1] = 0
    if sum(sum(pad_grid[1:11,1:11])) == 0:
        not_syncro = False
        print('All flashes in sync on step: {}'.format(step_counter))
    step_counter += 1



### ============================================================================
### END OF PROGRAM
### ============================================================================

