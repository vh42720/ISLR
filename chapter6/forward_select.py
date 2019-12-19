import numpy as np
from itertools import combinations
from model_run import model_run
import pandas as pd


def forward_select(y, X, k):
	# Set up for forward selection
	remaining_features = list(X.columns.values)
	features = []
	RSS_list, adj_R_squared_list, R_squared_list, \
	aic_list, bic_list, num_features = [], [], [], [], [], []
	features_list = []

	# Forward selection loop
	for i in np.arange(1, k + 1):
		best_RSS = np.inf
		# best_R_squared, best_adj_R_squared, best_aic, best_bic
		# Main loop
		for combo in combinations(remaining_features, 1):
			result = model_run(y, X[list(combo) + features])

			# store results
			temp_RSS, temp_R_squared, temp_adj_R_squared, temp_aic, temp_bic = result

			# Get the best parameters
			if temp_RSS < best_RSS:
				best_RSS = temp_RSS
				best_R_squared = temp_R_squared
				best_adj_R_squared = temp_adj_R_squared
				best_aic = temp_aic
				best_bic = temp_bic
				best_feature = combo[0]

		# Updating variables for next loop
		features.append(best_feature)
		num_features.append(i)
		remaining_features.remove(best_feature)

		# Saving values in list
		RSS_list.append(best_RSS)
		R_squared_list.append(best_R_squared)

		adj_R_squared_list.append(best_adj_R_squared)
		aic_list.append(best_aic)
		bic_list.append(best_bic)

		features_list.append(features.copy())

	# Put info into a nice dataframe
	df = pd.DataFrame({'num_features': num_features, 'features': features_list,
	                   'R_squared': R_squared_list, 'RSS': RSS_list,
	                   'adj_R_squared': adj_R_squared_list,
	                   'aic': aic_list, 'bic': bic_list})

	df = df.loc[df.groupby('num_features')['RSS'].idxmin()]

	return df

