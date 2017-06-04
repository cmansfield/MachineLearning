

# Use trained data to make a prediction
from sklearn.externals import joblib

model = joblib.load('trained_poker.pkl')

# Here is the data set we want to make a prediction on
hand_to_value = [
    4,
    12,
    3,
    12,
    4,
    1,
    1,
    12,
    1,
    10,
]

# scikit-learn is expecting a list of data sets
hands_to_value = [
    hand_to_value
]

# Run the model and make a prediction
predicted_hand_values = model.predict(hands_to_value)

predicted_value = predicted_hand_values[0]

print('This poker hand has an estimated value of {:.2f}'.format(predicted_value))

# Expected value of 3