import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import dfply
from dfply import *
import plotnine
from plotnine import *

path = os.path.join(os.getcwd(), 'Auto.csv')
auto = pd.read_csv(path)
auto2 = auto.drop(auto.index[9:84])




