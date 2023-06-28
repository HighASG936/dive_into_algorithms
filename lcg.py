import matplotlib.pyplot as plt
import numpy as np
import math


def next_random(previous, n1, n2, n3):
	"""Generate random number by a linear congruential generator"""
	the_next = (previous * n1 + n2) % n3
	return the_next

def list_random(n1, n2, n3):	
	"""Generate a random number list"""
	output = [1]
	while len(output) <= n3:
		output.append(next_random( output[-1], n1, n2, n3) )
	return output

def overlapping_sums(the_list, sum_length):
	"""The Diehard test for randomness"""
	lenght_of_list = len(the_list)
	the_list.extend(the_list)
	output = []

	for n in range(0, lenght_of_list):
		output.append(sum(the_list[n:(n + sum_length)]))
	return output

def average(data):
	""" """
	return sum(overlap) / len(overlap)

def gauss_bell(xs, data):
	""" """
	mu = average(data)  # Media
	sigma = mu/4  # Desviación estándar

	y_gauss = [max(data)*28/(math.sqrt(2*math.pi*sigma)) * math.exp( -0.5 * ((x-mu)/sigma)**2 ) for x in xs ]
	return y_gauss

def plot_overlapping_sums(x, overlap):
	""" """
	fig, ax = plt.subplots()
	y = gauss_bell(x, overlap)

	xs_media = [average(overlap) for _ in range(0, 2)]
	ys_media = [0, max(y)] 
	
	plt.title('Results of the overlapping sum test')
	plt.xlabel('Sum of Elements of overlapping consecutive sections of list')
	plt.ylabel('Frequency of Sum')
	
	ax.plot(x, y, xs_media, ys_media)
	ax.hist(overlap, 20, facecolor = 'blue', alpha = 0.5)

	plt.show()


if __name__ == "__main__":
	overlap = overlapping_sums(list_random(211111, 111112, 300007), 12)
	#overlap = overlapping_sums(list_random(29, 23, 32), 32)
	xs = np.linspace(min(overlap), max(overlap), 100)
	plot_overlapping_sums(xs, overlap)
