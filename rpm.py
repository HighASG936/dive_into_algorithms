import math
import pandas as pd

n1 = 274
n2 = 155

def rpm(n1, n2):
    """Russian Peasan Multiplication"""
    halving = [n1]
    doubling = [n2]
    msg = ""
    while(min(halving) > 1):
        halving.append(math.floor(min(halving)/2))

    while(len(doubling) < len(halving)):
        doubling.append(max(doubling)*2)

    half_double = pd.DataFrame(zip(halving, doubling))
    half_double = half_double.loc[half_double[0]%2 == 1,:]
    print (f"{half_double}\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    for number in half_double.loc[:,1]:
        msg += f" {number} +"

    answer = sum(half_double.loc[:,1])
    msg = f"{msg.strip('+')} = {answer}"
    print (msg)
    print (n1 * n2)

if __name__ == '__main__':
    rpm(n1, n2)

