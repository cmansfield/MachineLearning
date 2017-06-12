
from random import randint
from cards import *


def tie_breaker(hands):
    value = lambda x: 14 if x==1 else x
    total_values = []
    max_hand_index = 0
    max_val = 0

    # don't include the last hand, that's
    # the table's cards
    for i in range(0, len(hands) - 1):
        total_values.append(0)
        card_values = {}
        for card in set(hands[i].cards).union(hands[-1].cards):
            if card.value in card_values:
                card_values[card.value] += value(card.value) * 1000
            else:
                card_values[card.value] = value(card.value)
        for key, val in card_values.items():
            if(val > max_val):
                max_val = val
                max_hand_index = i
    total_values[max_hand_index] = 1
    return total_values

def check_hands(hands,card):
    for hand in hands:
        if hand.has_card(card): return True
    return False

def draw_card(hands):
    draw_new_card = lambda : Card(
        randint(1, len(suits)),
        randint(1, len(value_names)))
    top_card = draw_new_card()
    while(check_hands(hands,top_card)):
        top_card = draw_new_card()
    return top_card