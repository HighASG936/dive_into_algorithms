
def insert_cabinet(cabinet, to_insert):
	"""Insert an item on new cabinet"""
	check_location = len(cabinet) - 1
	insert_location = 0

	while check_location >= 0:
		if to_insert > cabinet[check_location]:
			insert_location = check_location + 1
			check_location = -1
		check_location -= 1
	
	cabinet.insert(insert_location, to_insert)
	return cabinet

def insertion_sort(cabinet):
	"""Performance of insertion sort algorithm"""
	newcabinet = []

	while len(cabinet) > 0:
		to_insert = cabinet.pop(0)
		newcabinet = insert_cabinet(newcabinet, to_insert)

	return newcabinet

if __name__ == '__main__':
	cabinet = [8,4,6,1,2,5,3,7,25,98,1,0,69]
	sortedcabinet = insertion_sort(cabinet)
	print(sortedcabinet)
