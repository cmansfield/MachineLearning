
'''
    This script creates training data for
    playing n_test_data number of poker games
'''

from sklearn.externals import joblib
from poker_lib import *


n_test_data = 2500


with open('poker-game-training.data', 'w') as f:
    f.write('suit_1,rank_1,suit_2,rank_2,suit_3,rank_3,suit_4,rank_4,suit_5,rank_5,class\n')

    for j in range(0, n_test_data):
        players = [Hand(),Hand()]
        table = Hand()

        # Each player at the poker table gets
        # two cards each
        draw_hole_cards(players)

        # Draw the flop cards that all players get
        draw_flop(players, table)

        model = joblib.load('trained-poker-hand.pkl')

        # scikit-learn is expecting a list of data sets
        players_to_value = \
            [(player.stringify() + ',' + table.stringify()).split(',')
             for player in players]

        # Run the model and make a prediction
        predicted_hand_values = model.predict(players_to_value)

        player_hand_predicted_value = int(round(predicted_hand_values[0]))
        opponent_hand_predicted_value = int(round(predicted_hand_values[1]))

        outcome = 0

        if(player_hand_predicted_value > opponent_hand_predicted_value):
            outcome = 1
        else:
            hand_values = tie_breaker(players,table)
            if (hand_values[0] == 1): outcome = 1

        f.write(hands[0].stringify()
                + ','
                + table.stringify()
                + ','
                + str(outcome)
                + '\n')