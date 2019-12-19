from scipy import stats
import math


def CI_print(mean, se, n, interval=0.95, method='t'):
	if method == 't':
		test_stat = stats.t.ppf((interval + 1) / 2, n)
	elif method == 'z':
		test_stat = stats.norm.ppf((interval + 1) / 2)
	lower_bound = mean - test_stat * se / math.sqrt(n)
	upper_bound = mean + test_stat * se / math.sqrt(n)

	print(f'fit: {mean}\nlwr: {lower_bound}\nupr: {upper_bound}')
