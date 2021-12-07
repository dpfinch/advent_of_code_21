### ============================================================================
### Advent of Code 
### ============================================================================
import pandas as pd
import numpy as np
### ============================================================================

# Part One

def create_bingo_card(flat_card):
    bingo_card = np.zeros([5,5])
    for n,line in enumerate(flat_card):
        int_line = [int(x) for x in line.rstrip().split()]
        bingo_card[n,:] = int_line
    return bingo_card

data_input = 'data_input/aoc_input4.txt'

with open(data_input) as f:
    first_line_string = f.readline().rstrip()

drawn_nums = first_line_string.split(',')
drawn_nums = [int(x) for x in drawn_nums]

with open(data_input) as f:
    bingo_input = f.readlines()[2:]

# Five lines for each card, plus one space line
num_cards = int(np.ceil(len(bingo_input)/6))

bingo_card_deck = np.zeros([num_cards,5,5])

for n,x in enumerate(range(len(bingo_input))[::6]):
    flat_card = bingo_input[x:x+5]
    bingo_card = create_bingo_card(flat_card)
    bingo_card_deck[n,:,:] = bingo_card


def check_for_win(filled_bingo_cards):
    for card_num, card in enumerate(filled_bingo_cards):
        if 0 in card.sum(axis = 0) or 0 in card.sum(axis = 1):
            return True,card_num

    else:
        return False, 0


bingo_filled = bingo_card_deck.copy()
for drawn_num in drawn_nums:
    bingo_filled[np.where(bingo_filled == drawn_num)] = 0

    win_bool,card_num = check_for_win(bingo_filled)
    if win_bool:
        print('Bingo!')
        break

sum_of_remaining = bingo_filled[card_num].sum()
print('Product of remaining numbers and drawn number = {}'.format(sum_of_remaining * drawn_num))

# Part Two

def remove_winning_cards(bingo_filled,cards_in_play):
    for card_num in cards_in_play:
        card = bingo_filled[card_num]
        if 0 in card.sum(axis = 0) or 0 in card.sum(axis = 1):
            cards_in_play.remove(card_num)
    return cards_in_play

cards_in_play = list(range(num_cards))
bingo_filled = bingo_card_deck.copy()
looser_bool = False
for drawn_num in drawn_nums:
    bingo_filled[np.where(bingo_filled == drawn_num)] = 0

    cards_in_play = remove_winning_cards(bingo_filled,cards_in_play)
    if looser_bool:
        loosing_card[np.where(loosing_card == drawn_num)] = 0
        break
    if len(cards_in_play) == 1:
        loosing_card = bingo_filled[cards_in_play][0]
        print('Loosing card!')
        looser_bool = True
    
    
sum_of_remaining_looser = loosing_card.sum()
print('Product of remaining numbers and drawn number = {}'.format(sum_of_remaining_looser
                                                                  * drawn_num))

### ============================================================================
### END OF PROGRAM
### ============================================================================

