import pandas as pd
from dfply import *
import os
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.graphics.gofplots import ProbPlot
import seaborn as sns

path = os.path.join(os.getcwd(), 'Boston.csv')
boston = pd.read_csv(path)

# X = boston >> select(~X.medv)
# Y = boston['medv']
#
# X = sm.add_constant(X)  # adding a constant
#
# model = sm.OLS(Y, X).fit()
# print(model.summary())

# all_columns = '+'.join(boston.columns.drop('medv'))
# my_formula = 'medv~' + all_columns
# mod = smf.ols(my_formula, data=boston).fit()
# print(mod.summary())

mod = smf.ols('medv ~ lstat + np.power(lstat, 2)', data=boston).fit()
print(mod.summary())
