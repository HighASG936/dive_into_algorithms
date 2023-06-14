

x = 42
y = 48

def gcd(x, y):
    """ Euclid's algorithm """
    larger = max(x, y)
    smaller = min(x, y)

    remainder = larger % smaller

    if(remainder == 0):
        return(smaller)

    if(remainder != 0):
        return(gcd(smaller, remainder))

if __name__ == '__main__':
    print(gcd(x, y))
