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
	"""Calculate the result of the continued fraction"""
	index = -1
	number = continued_fraction[index]

	while abs(index) < len(continued_fraction):
		next = continued_fraction[index -1]
		number = 1/number + next
		index -= 1
	return number

def continued_fraction_decimal(x, error_tolerance, length_tolerance):
	"""Algorithm for generation continued fractions from a decimal number"""
	output = []
	first_term = int(x)
	leftover = x - int(x)
	output.append(first_term)
	error = leftover

	while error > error_tolerance and len(output) < length_tolerance:
		next_term = math.floor(1/leftover)
		leftover = 1/leftover - next_term
		output.append(next_term)
		error = abs(get_number(output) - x)
	return output

if __name__ == "__main__":	
	#array = continued_fraction(229, 47, 10)
	array = continued_fraction_decimal(1.4142135623730951, 0.00001, 100)

	number = get_number(array)
	print(f"{array}\n{number}")