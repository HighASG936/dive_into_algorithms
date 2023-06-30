import numpy as np
import math
import matplotlib.pyplot as plt

def average(data):
	""" """
	return sum(overlap) / len(overlap)

def gauss_bell(xs, data):
	""" """
	mu = average(data)  # Media
	sigma = mu/4  # Desviación estándar

	y_gauss = [max(data)*28/(math.sqrt(2*math.pi*sigma)) * math.exp( -0.5 * ((x-mu)/sigma)**2 ) for x in xs ]
	return y_gauss