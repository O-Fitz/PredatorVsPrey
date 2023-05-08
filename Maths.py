import numpy as np


def mag(x):
	return np.sqrt(np.dot(x, x))


def normalise(x):
	return x/mag(x)
