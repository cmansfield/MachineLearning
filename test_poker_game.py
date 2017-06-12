
'''
    This tests our trained data
    playing a poker game
'''

from sklearn.externals import joblib
from poker_lib import *


players = [Hand(),Hand()]
table = Hand()

# Each player at the poker table gets
# two cards each
draw_hole_cards(players)

# Draw the flop cards that all players get
draw_flop(players,table)

for hand in players: print(hand)
print(table)

model = joblib.load('trained-poker-game.pkl')

# scikit-learn is expecting a list of data sets
players_to_value = \
    [(player.stringify() + ',' + table.stringify()).split(',')
     for player in players]

# Run the model and make a prediction
predicted_hand_values = model.predict(players_to_value)

player_hand_predicted_value = int(round(predicted_hand_values[0]))
opponent_hand_predicted_value = int(round(predicted_hand_values[1]))

print('Your poker hand has an estimated value of {:.2f}'.format(predicted_hand_values[0]))
print('Opponent poker hand has an estimated value of {:.2f}'.format(predicted_hand_values[1]))

