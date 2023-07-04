import pylab as pl
from matplotlib import collections as mc

pythagorean = lambda a, b: math.sqrt(a**2 + b**2)

def points_to_triangule(point1, point2, point3):
    """Set points coordinates and put on a list"""
    triangule = [list(point1), list(point2), list(point3)]
    return triangule

def genlines(cities, itinerary):
    """Get lines between two consecutively points"""
    lines = []
    for j in range(0, len(itinerary) -1):
        lines.append((cities[itinerary[j]], cities[itinerary[j+1]]))
    return lines

def get_distance(point1, point2):
    """Get distance among two points (x,y) by Pythagorean teorem"""
    a = abs(point1[0] - point2[0])
    b = abs(point1[1] - point2[1])
    distance = pythagorean(a, b)
    return distance

def plot_triangule_simple(triangule, thename):
    """Plot a simple triangule and its vertices"""
    fig, ax = pl.subplots()
    xs = [triangule[0][0], triangule[1][0], triangule[2][0]]
    ys = [triangule[0][1], triangule[1][1], triangule[2][1]]
    itin = [0,1, 2, 0]
    thelines = genlines(triangule, itin)
    lc = mc.LineCollection(genlines(triangule, itin), linewidths=2)
    
    ax.add_collection(lc)
    
    ax.margins(0.1)
    pl.scatter(xs, ys)
    pl.savefig(str(thename)+'.png')
    pl.close()

if __name__ == '__main__':
    a = (0.2, 0.8)
    b = (0.5, 0.2)
    c = (0.8, 0.7)
    plot_triangule_simple(points_to_triangule(a, b, c), 'tri')
    
    