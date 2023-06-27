import math

def square_root(x, y, error_tolerance):
	"""Babylonian Algorithm for square roots"""
	our_error = error_tolerance * 2

	while our_error > error_tolerance:
		z = x/y
		y = (y + z)/2
		our_error = y**2 - x
	return y

if __name__ == "__main__":
	print(square_root(5,1,0.0000000000001))
	print(math.sqrt(5))