
'''
    This tests our trained data
    playing a poker game
'''

from sklearn.externals import joblib
from poker_lib import *


hands = [Hand(),Hand(),Hand()]

# Each player at the poker table gets
# three cards each
for x in range(0, 3):
    for i in range(0, len(hands) - 1):
        hands[i].add_card(draw_card(hands))

for x in range(0, 2):
    hands[-1].add_card(draw_card(hands))

for hand in hands:
    print(hand)

model = joblib.load('trained_poker_game.pkl')

# scikit-learn is expecting a list of data sets
hands_to_value = [
    (hands[0].stringify() + ',' + hands[-1].stringify()).split(','),
    (hands[1].stringify() + ',' + hands[-1].stringify()).split(',')
]

# Run the model and make a prediction
predicted_hand_values = model.predict(hands_to_value)

player_hand_predicted_value = int(round(predicted_hand_values[0]))
opponent_hand_predicted_value = int(round(predicted_hand_values[1]))

print('Your poker hand has an estimated value of {:.2f}'.format(predicted_hand_values[0]))
print('Opponent poker hand has an estimated value of {:.2f}'.format(predicted_hand_values[1]))

