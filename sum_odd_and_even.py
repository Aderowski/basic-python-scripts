# https://edabit.com/challenge/5XXXppAdfcGaootD9

def sum_odd_and_even(lst):
	return [sum(e for e in lst if e%2==i) for i in [0,1]]

print(sum_odd_and_even([1, 2, 3, 4, 5, 6]))