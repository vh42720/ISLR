import numpy as np
import statsmodels.api as sm


def get_mse(data, X_train, X_test, y_train, y_test):
	# Set up parameters
	models = data.features
	mse_list = []

	# Predict using test data on all 19models
	for i in range(0, 19):
		# Select the columns for each model in dataframe X_test
		X = X_train[models[i]]
		y = y_train

		# Run OLS for each model and save mse
		regr = sm.OLS(y, sm.add_constant(X)).fit()
		X_test_temp = sm.add_constant(X_test[models[i]])
		pred = regr.predict(X_test_temp)
		mse = np.mean(np.square(pred - y_test))
		mse_list.append(mse)

	return mse_list
