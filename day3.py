### ============================================================================
### Advent of Code 
### ============================================================================
import pandas as pd
import numpy as np
### ============================================================================

# Part One

binary_df = pd.DataFrame(columns = range(12))

input_file = 'data_input/aoc_input3.txt'
row_ind = 0
with open(input_file) as f:
    contents = f.readlines()
    
for n,line in enumerate(contents):
    binary_list = list(line[:-1])   
    binary_df.loc[n] = binary_list

num_counts = binary_df.apply(pd.Series.value_counts)
gamma_count = num_counts.idxmax().values
epsilon_count = num_counts.idxmin().values

gamma_val = int(''.join(gamma_count),2)
epsilon_val = int(''.join(epsilon_count),2)

print('Submarine power product: {}'.format(gamma_val * epsilon_val))

# Part Two

gamma_df = binary_df.copy()
epsilon_df = binary_df.copy()
for col in binary_df.columns:
    # Test for equal max value
    if gamma_df[col].eq(gamma_df[col].value_counts().max()).sum() > 1:
        gamma_df = gamma_df[gamma_df[col] == '1']
        
    if epsilon_df[col].eq(epsilon_df[col].value_counts().max()).sum() > 1:
        epsilon_df = epsilon_df[epsilon_df[col] == '0']
        
    else:   
        most_common = gamma_df[col].value_counts().idxmax()
        least_common = epsilon_df[col].value_counts().idxmin()
        
        gamma_df = gamma_df[gamma_df[col] == most_common]
        epsilon_df = epsilon_df[epsilon_df[col] == least_common]


    if len(gamma_df) == 1:
        oxygen_gen_rating = int(''.join(gamma_df.values[0]),2)
    if len(epsilon_df) == 1:
        co2_scrub_rating = int(''.join(epsilon_df.values[0]),2)

print('Life suppoort rating: {}'.format(oxygen_gen_rating * co2_scrub_rating))

        
### ============================================================================
### END OF PROGRAM
### ============================================================================

