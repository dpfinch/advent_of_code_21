### ============================================================================
### Advent of Code 
### ============================================================================
import pandas as pd
### ============================================================================

# Part One

input_1 = "data_input/aoc_input1.csv"

df = pd.read_csv(input_1, names =['depth'])
df['depth_change'] = df.diff()
df['increase'] = df.depth_change > 0

num_increases = df.increase.sum()

# Part Two

df['roll_sum'] = df.depth.rolling(3).sum()
df['roll_change'] = df.roll_sum.diff()
df['roll_increase'] = df.roll_change > 0

num_roll_increase = df.roll_increase.sum()

### ============================================================================
### END OF PROGRAM
### ============================================================================

