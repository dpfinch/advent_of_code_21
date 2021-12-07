### ============================================================================
### Advent of Code 
### ============================================================================
import pandas as pd
import numpy as np
import math
### ============================================================================

# Part One

data_input = 'data_input/aoc_input7.csv'

crab_arr = np.genfromtxt(data_input,delimiter = ',', dtype = int)

max_pos = max(crab_arr)

fuel_spent = max_pos * len(crab_arr)

for position in range(1,max_pos + 1):
    possible_answer = sum(abs(crab_arr - position))
    if possible_answer < fuel_spent:
        fuel_spent = possible_answer
    
print('Minimum possible fuel spent: {}'.format(fuel_spent))
# Part Two

distance_moved = abs(crab_arr - max_pos)
fuel_used = [sum(range(n+1)) for n in distance_moved]
fuel_spent = sum(fuel_used)

for position in range(1,max_pos + 1):
    distance_moved = abs(crab_arr - position)
    fuel_used = [sum(range(n+1)) for n in distance_moved]
    possible_answer = sum(fuel_used)
    if possible_answer < fuel_spent:
        fuel_spent = possible_answer

print('New minimum possible fuel spent: {}'.format(fuel_spent))   
### ============================================================================
### END OF PROGRAM
### ============================================================================

