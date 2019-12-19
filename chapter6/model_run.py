import statsmodels.api as sm


# Define the fitting process
def model_run(y, X):
	"""Run a linear regression and get RSS with R-squared"""
	regr = sm.OLS(y, sm.add_constant(X.values)).fit()
	RSS = regr.mse_resid * len(y)
	R_squared = regr.rsquared
	adj_R_squared = regr.rsquared_adj
	aic = regr.aic
	bic = regr.bic
	return RSS, R_squared, adj_R_squared, aic, bic
