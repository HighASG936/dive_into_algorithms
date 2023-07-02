import numpy as np
import math
import matplotlib.pyplot as plt

class bell:
	""" """
	def __init__(self, xs, data):
		self.xs = xs
		self.data = data
		self.mu = sum(data) / len(data)  # Media
		self.sigma = self.mu/4  # Desviación estándar

	def values(self):
		""" """
		y = [max(self.data)*28/(math.sqrt(2*math.pi*self.sigma)) * \
		     math.exp( -0.5 * ((x-self.mu)/self.sigma)**2 ) \
		    for x in self.xs ]
		return y
