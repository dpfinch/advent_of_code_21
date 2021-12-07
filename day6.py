### ============================================================================
### Advent of Code 
### ============================================================================
import pandas as pd
import numpy as np

### ============================================================================

# Part One

data_input = 'data_input/aoc_input6.csv'

fish_arr = np.genfromtxt(data_input,delimiter = ',')

days = 80

for day in range(days):
    new_fish = [8] * len(np.where(fish_arr == 0)[0])
    fish_arr = fish_arr - 1
    fish_arr = np.append(fish_arr,new_fish)

    fish_arr[np.where(fish_arr == -1)[0]] = 6
       
    
print('Number of fish after {} days = {}'.format(days,len(fish_arr)))

# Part Two
# Above method does not hold water with longer days
first_fish_arr = np.genfromtxt(data_input,delimiter = ',')
fish_ages = {-1:0,0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}

# Initialise fish ages
for fish in first_fish_arr:
    fish_ages[fish] += 1

days = 256

for day in range(days):
    fresh_fish =  fish_ages[0]
    
    fish_ages[0] = fish_ages[1]
    fish_ages[1] = fish_ages[2]
    fish_ages[2] = fish_ages[3]
    fish_ages[3] = fish_ages[4]
    fish_ages[4] = fish_ages[5]
    fish_ages[5] = fish_ages[6]
    fish_ages[6] = fish_ages[7]
    fish_ages[7] = fish_ages[8]
    fish_ages[8] = fresh_fish

    fish_ages[6] += fresh_fish
   
print('Number of fish after {} days = {}'.format(days,sum(fish_ages.values())))
    
### ============================================================================
### END OF PROGRAM
### ============================================================================

