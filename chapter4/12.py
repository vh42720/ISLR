# Applied - Question 12
import seaborn as sns
import matplotlib.pyplot as plt


def power(x=2):
	print(x**3)


def power2(x, a):
	print(x**a)


num_dict = {10: 3, 8: 17, 131: 3}
for x, a in num_dict.items():
	power2(x,a)


def power3(x, a):
	return x**a


x = range(0,11)
y = [power3(i,2) for i in x]

sns.scatterplot(x=x, y=y)
plt.show()


def PlotPower(x=None, a=2):
	if x is None:
		x = [1, 2, 3, 4, 5, 6]
	y = []
	for i in x:
		y.append(i**a)
	return sns.scatterplot(x=x, y=y)


fig = PlotPower(range(0, 10), 3)
plt.show()
