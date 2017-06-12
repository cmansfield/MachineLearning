
# Deep learning - Build a network
# train a network to predict the value of
# new poker hands given to the network
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import ensemble
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import GridSearchCV
from sklearn.externals import joblib


def run():
    df = pd.read_csv('poker-hand-training.data', header=0)

    # Remove the sale price as a feature
    features_df = df.drop('class', axis=1)

    # Create input and output arrays
    x = features_df.as_matrix()
    y = df['class'].as_matrix()

    # Split the data set into a training set (100%) and a test set (0%)
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.0)

    # Fit regression model
    model = ensemble.GradientBoostingRegressor(
        n_estimators=7000,   # Number of decision trees to build
        learning_rate=0.5,   # Impact of each decision tree
        max_depth=4,         # How many layers deep a decision tree can be
        min_samples_leaf=29, # How many times a value of a feature must show up inorder to build a decision tree around it
        max_features=0.75,   # % of features to randomly consider in creating a branch in our tree
        loss='huber'         # calculate the error rate
    )

    model.fit(x_train, y_train)

    # Save the trained model to a file so we can use it in other programs
    joblib.dump(model, 'trained-poker-hand.pkl')

    # Find the error rate on the training set
    mse = mean_absolute_error(y_train, model.predict(x_train))
    print('Trainig set mean absolute error: %.4f' % mse)

    if(len(x_test)):
        # Find the error rate on the test set
        mse = mean_absolute_error(y_test, gs_cv.predict(x_test))
        print('Test set mean absolute error: %.4f' % mse)


if __name__ == '__main__': run()