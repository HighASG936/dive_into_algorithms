from BinarySearch import binarysearch as bs
import math

def inverse_sin(number):
    """Calculate arcsin through algebraic mainpulation"""
    domain = [x*math.pi/10000 - math.pi/2 for x in list(range(0,10000))]
    the_range = [math.sin(x) for x in domain]
    result = domain[bs.binarysearch(the_range, number)]


if __name__ == "__main__":
    inverse_sin(0.9)
