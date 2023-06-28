

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

if __name__ == "__main__":
	print(list_random(29, 23, 32))
