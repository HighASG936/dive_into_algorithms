
def feedback_shift(bits):
	""" """
	xor_result = (bits[1] + bits[2]) % 2
	output = bits.pop()
	bits.insert(0, xor_result)
	return bits, output

def feedback_shift_list(bits_this):
	""" """
	bits_output = [bits_this.copy()]
	random_output = []
	bits_next = bits_this.copy()

	while len(bits_output) < 2**len(bits_this):
		bits_next, next = feedback_shift(bits_next)
		bits_output.append(bits_next.copy())
		random_output.append(next)
	return bits_output, random_output


if __name__ == "__main__":
	fsl = feedback_shift_list([1,1,1])
	bitslist = fsl[0]
	pseudorandom_bits = fsl[1]

	print(bitslist)
	print(pseudorandom_bits)

