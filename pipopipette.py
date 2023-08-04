import matplotlib.pyplot as plt
from matplotlib import collections as mc

def drawlattice(n, name):
    """
    Draw a grid of points and save picture into variable 'name'
    """
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            plt.plot(i, j, 'o', c='black')
    plt.savefig(name)

if __name__ == '__main__':
    drawlattice(5, 'lattice.png')

    