
'''
    This script tests the value of two poker
    hands against each other
'''

from sklearn.externals import joblib
from cards import *
import poker_lib


players = [Hand(),Hand()]
table = Hand()

# Each player at the poker table gets
# two cards each
poker_lib.draw_hole_cards(players)

# Draw the flop cards that all players get
poker_lib.draw_flop(players, table)

for player in players: print(player)
print(table)

model = joblib.load('trained-poker-hand.pkl')

# scikit-learn is expecting a list of data sets
players_to_value = \
    [(player.stringify() + ',' + table.stringify()).split(',')
     for player in players]

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
else:
    hand_values = poker_lib.tie_breaker(hands)
    print(hand_values)
    if (hand_values[0] == 1):
        print('You Won!')
    elif (hand_values[0] == 0):
        print('You lost...')
    else:
        print('Looks like you tied')
