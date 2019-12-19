import numpy as np
import pandas as pd
import scipy as sp
from itertools import combinations

import sklearn.linear_model as skl_lm
from sklearn.metrics import mean_squared_error
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import LeaveOneOut, KFold, cross_val_score, train_test_split
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA

import statsmodels.formula.api as smf
import statsmodels.api as sm

import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
# plt.style.use('seaborn-white')
