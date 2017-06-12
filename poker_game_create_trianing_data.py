
'''
    This script creates training data for
    playing a poker game
'''

from sklearn.externals import joblib
from poker_lib import *


n_test_data = 2500


with open('poker_game_training.data', 'w') as f:
    f.write('suit_1,rank_1,suit_2,rank_2,suit_3,rank_3,suit_4,rank_4,suit_5,rank_5,class\n')

    for j in range(0, n_test_data):
        hands = [Hand(),Hand(),Hand()]

        # Each player at the poker table gets
        # three cards each
        for x in range(0, 3):
            for i in range(0, len(hands) - 1):
                hands[i].add_card(draw_card(hands))

        for x in range(0, 2):
            hands[-1].add_card(draw_card(hands))

        # for hand in hands:
        #     print(hand)

        model = joblib.load('trained_poker.pkl')

        # scikit-learn is expecting a list of data sets
        hands_to_value = [
            (hands[0].stringify() + ',' + hands[-1].stringify()).split(','),
            (hands[1].stringify() + ',' + hands[-1].stringify()).split(',')
        ]

        # Run the model and make a prediction
        predicted_hand_values = model.predict(hands_to_value)

        player_hand_predicted_value = int(round(predicted_hand_values[0]))
        opponent_hand_predicted_value = int(round(predicted_hand_values[1]))

        outcome = 0
        # print('Your poker hand has an estimated value of {:.2f}'.format(predicted_hand_values[0]))
        # print('Opponent poker hand has an estimated value of {:.2f}'.format(predicted_hand_values[1]))

        if(player_hand_predicted_value > opponent_hand_predicted_value):
            # print('You Won!')
            outcome = 1
        # elif(player_hand_predicted_value < opponent_hand_predicted_value):
        #     print('You lost...')
        else:
            hand_values = tie_breaker(hands)
            # print(hand_values)
            if (hand_values[0] == 1):
                # print('You Won!')
                outcome = 1
            # elif (hand_values[0] == 0):
            #     print('You lost...')
            # else:
            #     print('Looks like you tied')

        f.write(hands[0].stringify()
                + ','
                + hands[-1].stringify()
                + ','
                + str(outcome)
                + '\n')