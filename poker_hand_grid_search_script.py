
# Deep learning - Grid Search
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

    # Split the data set into a training set (70%) and a test set (30%)
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)

    model = ensemble.GradientBoostingRegressor()

    # A list of parameters we want to try to find the best fit
    param_grid = {
        'n_estimators': [3000, 5000, 7000],				# Number of decision trees to build
        'learning_rate': [0.5],                   		# Impact of each decision tree
        'max_depth': [2, 4],							# How many layers deep a decision tree can be
        'min_samples_leaf': [17, 23, 29],				# How many times a value of a feature must show up inorder to build a decision tree around it
        'max_features': [1.0, 0.75, 0.5],				# % of features to randomly consider in creating a branch in our tree
        'loss': ['huber']	            				# calculate the error rate
    }

    # Define the grid search we want to run. Run it with four cpus in parallel
    gs_cv = GridSearchCV(model, param_grid, n_jobs=4)

    # Run the grid search - on only the training data
    gs_cv.fit(x_train, y_train)

    # Print the parameters that gave us the best result
    print(gs_cv.best_params_)

    # Save the trained model to a file so we can use it in other programs
    # joblib.dump(model, 'trained_house_model.pkl')

    # Find the error rate on the training set
    mse = mean_absolute_error(y_train, gs_cv.predict(x_train))
    print('Trainig set mean absolute error: %.4f' % mse)

    # Find the error rate on the test set
    mse = mean_absolute_error(y_test, gs_cv.predict(x_test))
    print('Test set mean absolute error: %.4f' % mse)


if __name__ == '__main__': run()