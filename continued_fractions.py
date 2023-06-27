import math

def continued_fraction(x, y, length_tolerance):
	"""Algorithm for generation continued fractions"""
	output = []
	big = max(x, y)
	small = min(x, y)

	while small > 0 and len(output) < length_tolerance:
		quotient = math.floor(big/small)
		output.append(quotient)
		new_small = big % small
		big = small
		small = new_small
	return output

def get_number(continued_fraction):
	""" """
	index = -1
	number = continued_fraction[index]

	while abs(index) < len(continued_fraction):
		next = continued_fraction[index -1]
		number = 1/number + next
		index -= 1
	return number


if __name__ == "__main__":	
	array = continued_fraction(229, 47, 10)
	number = get_number(array)
	print(f"{array}\n{number}")