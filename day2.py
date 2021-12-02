### ============================================================================
### Advent of Code 
### ============================================================================
import pandas as pd
### ============================================================================

# Part One

df_direction = pd.read_csv('data_input/aoc_input2.csv', names = ['direction','distance'], delimiter = ' ')
totaled_dir = df_direction.groupby('direction').sum()

forward = totaled_dir.loc['forward']
up = totaled_dir.loc['up']
down = totaled_dir.loc['down']
level_sum = down - up

direction_product = level_sum * forward
print('Postion Product: {}'.format(direction_product.distance))

# Part Two

aim_tot = 0
hori_pos = 0
depth = 0
for i, r  in df_direction.iterrows():
    if r.direction == 'forward':
        hori_pos += r.distance
        depth += aim_tot * r.distance
    if r.direction == 'up':
        aim_tot -= r.distance
    if r.direction == 'down':
        aim_tot += r.distance

print('Aim position product: {}'.format(depth * hori_pos))
### ============================================================================
### END OF PROGRAM
### ============================================================================

