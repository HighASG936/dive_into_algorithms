import math

class BinarySearch:

    def __init__(self):
        """Initialization of BinarySearch class"""
        pass

    def binarysearch(self, sorted_cabinet, looking_for):
        """Binary search algorithm"""
        guess = math.floor(len(sorted_cabinet)/2)
        upperbound = len(sorted_cabinet)
        lowerbound = 0
        while abs(sorted_cabinet[guess] - looking_for) > 0.0001:
            if sorted_cabinet[guess] > looking_for:
                upperbound = guess
                guess = math.floor((guess + lowerbound)/2)
            if sorted_cabinet[guess] < looking_for:
                lowerbound = guess
                guess = math.floor((guess + upperbound)/2)
        return guess

if __name__ == "__main__":
    sorted_cabinet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    search = BinarySearch()

    print(search.binarysearch(sorted_cabinet, 8))
