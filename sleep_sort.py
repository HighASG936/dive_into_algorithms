import threading 
from time import sleep
from timeit import default_timer as timer

def sleep_sort(i):
	"""Sleep Sort"""
	global sortedlist

	sleep(i)
	sortedlist.append(i)
	return i

if __name__ == "__main__":
	items = [2, 4, 5, 2, 1, 7, 9, 15]
	sortedlist = []

	start = timer()
	ignore_result = [threading.Thread(target=sleep_sort, args=(i,) ) for i in items]

	#Start all threads
	for x in ignore_result:
		x.start()
	
	#Wait until all threads finished
	for x in ignore_result:
		x.join()
	
	end = timer()
	print(sortedlist)
	print(f"{(end - start):.4f} seconds")	
