
import math

def merging(left, right):
    """Merging two list to one list"""
    newcabinet = []

    while min(len(left), len(right)) > 0:
        if left[0] > right[0]:
            to_insert = right.pop(0)
        elif left[0] <= right[0]:
            to_insert = left.pop(0)
        newcabinet.append(to_insert)

    if len(left) > 0:
        for i in left:
            newcabinet.append(i)
    if len(right) > 0:
        for i in right:
            newcabinet.append(i)
    return newcabinet

def mergesort(cabinet):
    """Sort our list using merge sort"""
    newcabinet =[]

    if len(cabinet) == 1:
        newcabinet = cabinet
    else:
        left = mergesort(cabinet[:math.floor(len(cabinet)/2)])
        right = mergesort(cabinet[math.floor(len(cabinet)/2):])
        newcabinet = merging(left, right)
    return newcabinet

if __name__ == "__main__":

    #left = [1,2,3,4,4,5,7,8,9]
    #right = [2,4,9,7,8,8,10,12,13,14]
    #newcabinet =  merging(left, right)
    #print (newcabinet)

    cabinet = [4,1,3,2,6,3,18,2,9,7,3,1,2.5,-9]
    newcabinet = mergesort(cabinet)
    print (newcabinet)
    print ( len(cabinet) * math.log2( len(cabinet) ) )

