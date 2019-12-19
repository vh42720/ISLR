import os
import pandas as pd
import plotnine
from plotnine import *
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import PIL
import math

# loading files and create data frame
path_Advertising = os.path.join('D:\\PycharmProjects\\ISLR\\data', 'Advertising.csv')
Advertising = pd.read_csv(path_Advertising)

# Exploratory Analysis
Sales_and_TV = ggplot(Advertising, aes('TV', 'Sales')) \
               + geom_point(shape='o', alpha=0.4) \
               + stat_smooth()
Sales_and_Radio = ggplot(Advertising, aes('Radio', 'Sales')) + geom_point()
Sales_and_Newspaper = ggplot(Advertising, aes('Newspaper', 'Sales')) + geom_point()

# drawing random samples
sample = np.random.normal(0, 1, 10000)
data = {'cond': np.repeat(['A', 'B'], 5000), 'rating': sample}
df = pd.DataFrame(data)
normal = ggplot(df, aes('rating')) + geom_histogram()
normal.save('test.png')
print(normal)

# Contour graph testing
seq = np.linspace(1, 10, 50)
x = np.linspace(0, 10, 50)
y = np.linspace(0, 10, 60)


def f(x, y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)


X, Y = np.meshgrid(x, y)
Z = f(X, Y)
plt.contour(X, Y, Z, 20, cmap='RdGy')
