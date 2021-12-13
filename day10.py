### ============================================================================
### Advent of Code 
### ============================================================================
import pandas as pd
import numpy as np
import math
from skimage.segmentation import flood_fill
### ============================================================================

# Part One, copied from Sam

data_input = 'data_input/aoc_input10.txt'

with open(data_input) as f:
    contents = f.readlines()
    
points = {')': 3,
          ']': 57,
          '}': 1197,
          '>': 25137}

sum_of_points = 0

opening = ['(','[','{','<']
closing = [')',']','}','>']

closed_to_open = {'}':'{', ']':'[', '>':'<', ')':'('}
open_to_closed = {'{':'}', '[':']', '<':'>', '(':')'}

failed_lines = []
failed_characters = []
point_total = []
success_lines = []

for n,line in enumerate(contents):
    navi_line = line.strip()

    last_opened = []
    for i in navi_line:
        if i in opening:
          last_opened.append(i)
        elif i in closing:
          if last_opened[-1] != closed_to_open[i]:
            failed_lines.append(n)
            failed_characters.append(i)
            point_total.append(points[i])
            break
          else:
            last_opened.pop() # successfully closed
    if n not in failed_lines: success_lines.append(n)

print('Total syntax error score: {}'.format(sum(point_total)))
# Part Two

points = {')':1,
          ']':2,
          '}':3,
          '>':4}

score_list = []

contents = np.asarray(contents)

for line in contents[success_lines]:
    incomplete_line = line.strip()
    last_opened = []
    for i in incomplete_line:
        if i in opening:
            last_opened.append(i)
        elif i in closing:
            last_opened.pop() # successfully closed
    # Looking at the remainder
    
    score = 0
    for i in last_opened[::-1]:
        score = (score * 5) + points[open_to_closed[i]]
    score_list.append(score)

score_list = sorted(score_list)

print('Middle score:', score_list[int((len(score_list)/2) - 0.5)])

### ============================================================================
### END OF PROGRAM
### ============================================================================

