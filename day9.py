### ============================================================================
### Advent of Code 
### ============================================================================
import pandas as pd
import numpy as np
import math
from skimage.segmentation import flood_fill
### ============================================================================

# Part One

data_input = 'data_input/aoc_input9.txt'

def input_to_array(input_filename):
    with open(input_filename) as f:
        content = f.readlines()
    all_lines = []
    for line in content:
        list_of_line = list(line.strip())
        line_of_ints = list(map(int,list_of_line))
        all_lines.append(line_of_ints)
    floor_arr = np.array(all_lines)
    return floor_arr

floor_map = input_to_array(data_input)

risk_factor = 0

diff_arr = np.zeros([4,floor_map.shape[0],floor_map.shape[1]])
diff_arr[:] = np.nan

# Difference up
diff_up = np.diff(floor_map, axis = 0) < 0
diff_arr[0,1:,:] = diff_up
# Difference down
diff_down = np.diff(floor_map[::-1,:], axis = 0)[::-1,:] < 0
diff_arr[1,:floor_map.shape[0]-1,:] = diff_down
# Difference left
diff_left = np.diff(floor_map,axis = 1) < 0
diff_arr[2,:,1:] = diff_left
# Difference right
diff_right = np.diff(floor_map[:,::-1], axis = 1)[:,::-1] < 0
diff_arr[3,:,:floor_map.shape[0]-1] = diff_right

lowest_point = np.nanprod(diff_arr,axis =0)
risky_points = floor_map[lowest_point == 1]

risk_factor = sum(risky_points + 1)
print('Risk factor: {}'.format(risk_factor))

# Part Two

basin_sizes = []

floor_map[floor_map<9] = 0

for x in range(floor_map.shape[0]):
    for y in range(floor_map.shape[1]):
        if floor_map[x,y] == 9:
            continue
        filled_basin = flood_fill(floor_map,(x,y),1,connectivity = 1)
        basin_size = sum(filled_basin[filled_basin  == 1])
        basin_sizes.append(basin_size)
three_biggest = list(set(basin_sizes))[-3:]

print('Sum of three largerst basin sizes: {}'.format(np.product(three_biggest)))

### ============================================================================
### END OF PROGRAM
### ============================================================================

