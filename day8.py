### ============================================================================
### Advent of Code 
### ============================================================================
import pandas as pd
import numpy as np
import math
### ============================================================================

# Part One

# 1 = two segments
# 2 = five segments
# 3 = five segments
# 4 = four segments
# 5 = five segments
# 6 = six segments
# 7 = three segments
# 8 = seven segments
# 9 = six segments
# 0 = six segments

def parse_input_line(line):
    individual_code = line.replace(' |','').split(' ')
    individual_code = [''.join(sorted(s)) for s in individual_code]
    return individual_code
    
signal_df = pd.DataFrame(columns = ['IN_1','IN_2','IN_3','IN_4','IN_5','IN_6',
                                    'IN_7','IN_8','IN_9','IN_10',
                                    'OUT_1','OUT_2','OUT_3','OUT_4'])


in_cols = [col for col in signal_df.columns if 'IN_' in col]
out_cols = [col for col in signal_df.columns if 'OUT_' in col]

data_input = 'data_input/aoc_input8.txt'

with open(data_input) as f:
    content = f.readlines()

for n,line in enumerate(content):
    signal_df.loc[n] = parse_input_line(line.rstrip())

segment_len_df = signal_df.copy()

for col in signal_df.columns:
    segment_len_df[col] = signal_df[col].apply(len)


ones = 0
fours = 0
sevens = 0
eights = 0

for out_col in out_cols:
    col_count = segment_len_df[out_col].value_counts()
    ones += col_count.loc[2]
    fours += col_count.loc[4]
    sevens += col_count.loc[3]
    eights += col_count.loc[7]

print('Number of ones: {}'.format(ones))
print('Number of fours: {}'.format(fours))
print('Number of sevens: {}'.format(sevens))
print('Number of eights: {}'.format(eights))

print('Total of all those: {}'.format(sum([ones,fours,sevens,eights])))
# Part Two

# Seven segment display

#     xxxx
#    y    w
#    y    w
#     zzzz
#    q    m
#    q    m
#     pppp

# segments:
# top = used 8 times
# top_left = 6 times
# top_right = 8 times 
# mid = 7 times
# bottom_left = 4 times
# bottom_right = 9 times
# bottom = 7 times

class display:
    def __init__(self):
        self.top = None
        self.top_left = None
        self.top_right = None
        self.mid = None
        self.bottom_left = None
        self.bottom_right = None
        self.bottom = None    

def get_number_mapping(position):
    number_dict = {
        '0': position.top + position.top_left + position.top_right + position.bottom_left + position.bottom_right + position.bottom,
        '1': position.bottom_right + position.top_right,
        '2': position.top + position.top_right + position.mid + position.bottom_left + position.bottom,
        '3': position.top + position.top_right + position.mid + position.bottom_right + position.bottom,
        '4': position.top_left + position.top_right + position.mid + position.bottom_right,
        '5': position.top + position.top_left + position.mid + position.bottom_right + position.bottom,
        '6': position.top + position.top_left + position.mid + position.bottom_left + position.bottom_right + position.bottom,
        '7': position.top + position.top_right + position.bottom_right,
        '8': position.top + position.top_left + position.top_right + position.mid + position.bottom_left + position.bottom_right + position.bottom,
        '9': position.top + position.top_left + position.top_right + position.mid + position.bottom_right + position.bottom
        }

    for k in number_dict.keys():
        number_dict[k] = ''.join(sorted(number_dict[k]))
    return number_dict

answer_total = 0
            
for ind, row in signal_df.iterrows():
    full_display = display()
    
    # join all in strings into one
    all_in_wires = ''.join(row[in_cols].values)
    for position in ['a','b','c','d','e','f','g']:
        # Certain display position are used a unique amount of times
        if all_in_wires.count(position) == 6:
            full_display.top_left = position
        if all_in_wires.count(position) == 4:
            full_display.bottom_left = position
        if all_in_wires.count(position) == 9:
            full_display.bottom_right = position
    # now got 3/7 segments
    
    in_length_series = segment_len_df.loc[ind][in_cols]
    one_in = in_length_series[in_length_series == 2].index[0]
    four_in = in_length_series[in_length_series == 4].index[0]
    seven_in = in_length_series[in_length_series == 3].index[0]
    eight_in = in_length_series[in_length_series == 7].index[0]
    
    one_wires = row[one_in]
    seven_wires = row[seven_in]
    top_of_seven = list(set(seven_wires)- set(one_wires))[0]
    full_display.top = top_of_seven
    
    # 4/7 segments
    top_of_one = one_wires.replace(full_display.bottom_right,'')
    full_display.top_right = top_of_one
    # 5/7 segments
    four_wires = row[four_in]
    mid_of_four = list(set(four_wires) - set(full_display.bottom_right + 
                                      full_display.top_right + 
                                      full_display.top_left))[0]
    
    full_display.mid = mid_of_four
    # 6/7 segments
    eight_wires = row[eight_in]
    bottom_of_eight = list(set(eight_wires) - set(full_display.bottom_right + 
                                      full_display.top_right + 
                                      full_display.top_left + 
                                      full_display.top + 
                                      full_display.mid + 
                                      full_display.bottom_left))[0]
    full_display.bottom = bottom_of_eight
    # Got the 7/7 segments
    
    # Now to convert output into numbers....
    number_dict = get_number_mapping(full_display)
    out_number = ''
    for out_col in out_cols:
        out_str = row[out_col]
        out_number += list(number_dict.keys())[list(number_dict.values()).index(out_str)]
        
    answer_total += int(out_number)
        
print('The sum of all output values is: {}'.format(answer_total))
### ============================================================================
### END OF PROGRAM
### ============================================================================

