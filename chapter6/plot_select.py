from operator import itemgetter
import matplotlib.pyplot as plt
import numpy as np
from dfply import *


def plot_select(data):
	"""
	:param data: dataframe return by best_select/forward_select
	:return:
	"""

	# set up variables for plotting
	bics = data.bic
	aics = data.aic
	adj_R_squared = data.adj_R_squared
	min_bic_index, min_bic = min(enumerate(bics), key=itemgetter(1))
	min_aic_index, min_aic = min(enumerate(aics), key=itemgetter(1))
	max_adjR_index, max_adjR = max(enumerate(adj_R_squared), key=itemgetter(1))

	# Set up plots
	fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 4))

	# Left plot
	ax1.plot(data.num_features, bics, color='b', label='BIC', marker='o')
	ax1.plot(data.num_features, aics, color='r', label='AIC', marker='o')
	ax1.plot(3, min_bic, color='g', marker='x', markersize=20)
	ax1.plot(3, min_aic, color='g', marker='x', markersize=20)
	ax1.set_ylabel('BIC/AIC')
	ax1.set_xlabel('Number of features')
	ax1.set_xticks(np.arange(0, len(data.num_features), step=1))
	ax1.legend()

	# Right plot
	ax2.plot(data.num_features, adj_R_squared, color='k', marker='o')
	ax2.plot(max_adjR_index+1, max_adjR, color='g', marker='x', markersize=20)
	ax2.set_ylabel('Adjusted R-squared')
	ax2.set_xlabel('Number of Features')
	ax1.set_xticks(np.arange(0, len(data.num_features), step=1))
	ax2.vlines(max_adjR_index+1, ymin=0.3, ymax=max_adjR, linestyles='--', color='g')

	return fig
