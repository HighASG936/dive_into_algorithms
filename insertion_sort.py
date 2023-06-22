
from timeit import default_timer as timer
import random
import matplotlib.pyplot as plt
import math
import numpy as np

def insert_cabinet(cabinet, to_insert):
	"""Insert an item on new cabinet"""
	global stepcounter

	check_location = len(cabinet) - 1
	insert_location = 0

	while check_location >= 0:
		stepcounter += 1
		if to_insert > cabinet[check_location]:
			insert_location = check_location + 1
			check_location = -1
		check_location -= 1
	stepcounter += 1
	cabinet.insert(insert_location, to_insert)
	return cabinet

def insertion_sort(cabinet):
	"""Performance of insertion sort algorithm"""
	global stepcounter

	newcabinet = []

	while len(cabinet) > 0:
		stepcounter += 1
		to_insert = cabinet.pop(0)
		newcabinet = insert_cabinet(newcabinet, to_insert)
	return newcabinet

def check_steps(size_of_cabinet):
	"""Check quantity of steps"""
	global stepcounter

	cabinet = [int(1000 * random.random()) for i in range(size_of_cabinet)]
	stepcounte = 0
	sortedcabinet = insertion_sort(cabinet)
	return stepcounter


if __name__ == '__main__':
    stepcounter = 0
    start = timer()

    random.seed(5040)
    xs = list(range(1,100))
    ys = [check_steps(x) for x in xs]
    ys_exp = [math.exp(x) for x in xs]
    ys_squared = [x**2 for x in xs]
    ys_threehalves = [x**1.5 for x in xs]
    ys_cubed = [x**3 for x in xs]
    ys_more_acurrent = [ 18.7*((0.5*x**2)+(1.5*x))   for x in xs]

    plt.plot(xs, ys)
    axes = plt.gca()
    axes.set_ylim(np.min(ys), np.max(ys) + 140)
    plt.plot(xs, ys_exp)
    plt.plot(xs, ys_squared)
    plt.plot(xs, ys_threehalves)
    plt.plot(xs, ys_cubed)
    plt.plot(xs, ys_more_acurrent)
    plt.title('Comparing Insertion Sort to Other Growth Rates')
    plt.xlabel('Number of Files in Random Cabinet')
    plt.ylabel('Steps Required to Sort Cabinet by Insertion Sort')
    plt.show()

#	cabinet = [8,4,6,1,2,5,3,7]
#	sortedcabinet = insertion_sort(cabinet)
#	print(sortedcabinet)
#	end = timer()
#	print(end - start)
#	print(stepcounter)
