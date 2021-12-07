### ============================================================================
### Advent of Code 
### ============================================================================
import pandas as pd
import numpy as np
from skimage.draw import line as intecept_line
### ============================================================================

# Part One

def process_input_line(line):
    half1, half2 = line.split('->')
    x1 = int(half1.split(',')[0])
    y1 = int(half1.split(',')[1])
    x2 = int(half2.split(',')[0])
    y2 = int(half2.split(',')[1])

    return x1,y1,x2,y2

data_input = 'data_input/aoc_input5.txt'

with open(data_input) as f:
    file_contents = f.readlines()

vent_lines = pd.DataFrame(columns = ['x1','y1','x2','y2'])

for n, line in enumerate(file_contents):
    x1,y1,x2,y2 = process_input_line(line.rstrip())
    vent_lines.loc[n] = x1,y1,x2,y2

    
straight_lines = vent_lines[(vent_lines.x1 == vent_lines.x2) | (vent_lines.y1 == vent_lines.y2)]

xmax = straight_lines[['x1','x2']].max().max()
ymax = straight_lines[['y1','y2']].max().max()

sea_floor_grid = np.zeros([xmax,ymax])

for ind,row in straight_lines.iterrows():
    if row.x1 == row.x2:
        x_ind = row.x1
        y_line = [row.y1,row.y2]
        y_line.sort()
        
        sea_floor_grid[x_ind,y_line[0]:y_line[1]+1] +=1
        
    else:
        y_ind = row.y1
        x_line = [row.x1,row.x2]
        x_line.sort()
        sea_floor_grid[x_line[0]:x_line[1]+1, y_ind] +=1


number_of_overlaps = len(np.where(sea_floor_grid > 1)[0])
print('Number of overlapping vent lines: {}'.format(number_of_overlaps))
# Part Two

xmax = vent_lines[['x1','x2']].max().max()
ymax = vent_lines[['y1','y2']].max().max()
new_sea_floor_grid = np.zeros([xmax+1,ymax+1])

for ind,row in vent_lines.iterrows():
    intercepts_x, intercepts_y = intecept_line(row.x1, row.y1,row.x2, row.y2)
    for coord in range(len(intercepts_x)):
        new_sea_floor_grid[intercepts_x[coord],intercepts_y[coord]] += 1

number_of_overlaps = len(np.where(new_sea_floor_grid > 1)[0])
print('Number of overlapping vent lines (with diagonal): {}'.format(number_of_overlaps))      

### ============================================================================
### END OF PROGRAM
### ============================================================================

