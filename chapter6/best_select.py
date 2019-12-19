from itertools import combinations
from model_run import model_run
import pandas as pd


def best_select(y, X_df):
	RSS_list, adj_R_squared_list, R_squared_list, \
	aic_list, bic_list, feature_list, num_features = [], [], [], [], [], [], []

	# Looping over k=1 to k=19 features in X:
	for k in range(1, len(X_df.columns) + 1):
		# Loop over all possible combinations: from 19 choose k
		for combo in combinations(X_df.columns, k):
			result = model_run(y, X_df[list(combo)])

			# store results
			RSS_list.append(result[0])
			R_squared_list.append(result[1])
			adj_R_squared_list.append(result[2])
			aic_list.append(result[3])
			bic_list.append(result[4])
			feature_list.append(combo)
			num_features.append(len(combo))

	# Store in dataframe
	df = pd.DataFrame({'num_features': num_features, 'RSS': RSS_list,
	                   'R_squared': R_squared_list, 'features': feature_list,
	                   'adj_R_squared': adj_R_squared_list,
	                   'aic': aic_list, 'bic': bic_list})

	# Sort best models by RSS
	df = df.loc[df.groupby('num_features')['RSS'].idxmin()]

	return df



