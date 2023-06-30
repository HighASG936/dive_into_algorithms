import math
import matplotlib.collections as mc
import matplotlib.pylab as pl
import numpy as np


def genlines(cities, itinerary):
	"""Get lines between two consecutively points"""
	lines = []
	for j in range(0, len(itinerary) -1):
		lines.append((cities[itinerary[j]], cities[itinerary[j+1]]))
	return lines

def get_distance(point1, point2):
		#Pythagorean teorem
		a = abs(point1[0] - point2[0])
		b = abs(point1[1] - point2[1])
		distance = math.sqrt(a**2 + b**2)
		return distance

def howfar(lines):
	""" """
	distance = 0
	for j in range(0, len(lines)):
		distance += get_distance(lines[j][1], lines[j][0])
	return distance


def plotitinerary(cities, itin, plottitle, thename):
	"""Plot the itinerary of our salesman"""
	lc = mc.LineCollection(genlines(cities, itin), linewidths=2)
	fig, ax = pl.subplots()
	ax.add_collection(lc)
	ax.autoscale()
	ax.margins(0.1)
	pl.scatter(x, y)
	pl.title(plottitle)
	pl.xlabel('X coordinate')
	pl.ylabel('Y coordinate')
	pl.savefig(str(thename) + '.png')
	pl.close()

def findnearest(cities, idx,nnitinerary):
	"""Nearest Neighbor Algorithm"""
	point = cities[idx]
	mindistance = float('inf')
	minidx = -1

	for j in range(0, len(cities)):
		distance = get_distance(point, cities[j])
		if 0 < distance < mindistance and j not in nnitinerary:
			mindistance = distance 
			minidx = j
	return minidx

def donn(cities, N):
	"""Do nearest neighbor"""
	nnitinerary = [0]
	for j in range(0, N -1):
		next = findnearest(cities, nnitinerary[len(nnitinerary) -1], nnitinerary)
		nnitinerary.append(next)
	return nnitinerary


if __name__ == "__main__":
	random_seed = 1729
	np.random.seed(random_seed)
	N = 40
	x = np.random.rand(N)
	y = np.random.rand(N)

	points = zip(x, y)
	cities = list(points)

	itinerary = list(range(0, N))
	lines = genlines(cities, itinerary)
	total_distance = howfar(lines)
	print(f"Random Itinerary:\t{total_distance:.2f} km")
	plotitinerary(cities, itinerary, 'TSP - Random Itinerary', 'figure2')
	
	itinerary = donn(cities, N)
	lines = genlines(cities, itinerary)
	total_distance = howfar(lines)
	print(f"Nearest Neighbor:\t{total_distance:.2f} km")	
	plotitinerary(cities, itinerary, 'TSP - Nearest Neighbor', 'figure3')

