
'''
    This script creates training data for
    playing a poker game
'''

from sklearn.externals import joblib
from random import randint


n_test_data = 100000

suits = ['\u2665','\u2660','\u2666','\u2663']
suit_names = ['Hearts','Spades','Diamonds','Clubs']
value_names = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']


class Card:
    def __init__(self, suit, value):
        if(suit < 1 or suit > 4): raise ValueError('The suit must be a value 1 through 4')
        if(value < 1 or value > 13): raise ValueError('The card value must be value 1 through 13')
        self.__suit = suit
        self.__value = value

    @property
    def suit(self): return self.__suit

    @property
    def value(self): return self.__value

    def __eq__(self, other):
        return self.__value == other.value \
               and other.suit == self.__suit

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__str__())

    def __str__(self):
        return '{} {} of {} {}'.format(
            suits[self.__suit - 1],
            value_names[self.__value - 1],
            suit_names[self.__suit - 1],
            suits[self.__suit - 1]
        )

class Hand:
    def __init__(self):
        self.__cards = set()

    def add_card(self, card):
        if not isinstance(card, Card): raise ValueError('Only Cards can be added to a hand')
        self.__cards.add(card)

    def reset_hand(self):
        self.__cards = set()

    def has_card(self,card):
        return card in self.__cards

    def stringify(self):
        str_simple = ''
        for card in self.__cards:
            str_simple += str(card.suit) + ',' + str(card.value) + ','
        return str_simple[:-1]

    def __str__(self):
        str_complex = ''
        for card in self.__cards:
            str_complex += card.__str__() + '\n'
        return str_complex

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

# with open('poker_game_training.data', 'w') as f:
#     for i in range(0, n_test_data):
game = ''
hands = [Hand(),Hand(),Hand()]

for x in range(0, 3):
    hands[0].add_card(draw_card(hands))
    hands[1].add_card(draw_card(hands))

for x in range(0, 2):
    hands[2].add_card(draw_card(hands))

for hand in hands:
    print(hand)

model = joblib.load('trained_poker.pkl')

# scikit-learn is expecting a list of data sets
hands_to_value = [
    (hands[0].stringify() + ',' + hands[2].stringify()).split(','),
    (hands[1].stringify() + ',' + hands[2].stringify()).split(',')
]

# Run the model and make a prediction
predicted_hand_values = model.predict(hands_to_value)

player_hand_predicted_value = int(round(predicted_hand_values[0]))
opponent_hand_predicted_value = int(round(predicted_hand_values[1]))

print('Your poker hand has an estimated value of {:.2f}'.format(predicted_hand_values[0]))
print('Opponent poker hand has an estimated value of {:.2f}'.format(predicted_hand_values[1]))

if(player_hand_predicted_value > opponent_hand_predicted_value):
    print('You Won!')
elif(player_hand_predicted_value < opponent_hand_predicted_value):
    print('You lost...')
else: print('Looks like you tied')
