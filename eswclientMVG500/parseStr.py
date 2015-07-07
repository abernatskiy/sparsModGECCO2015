import numpy as np

def parse1d(string):
	return np.array(map(int, string.split(' ')))

def parse2d(string):
	arr = parse1d(string)
	size = np.sqrt(len(arr))
	if not size.is_integer():
		raise ValueError('String parsing failed: the string does not encode a square matrix')
	size = int(size)
	return arr.reshape(size, size)
