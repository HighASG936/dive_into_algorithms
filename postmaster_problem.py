import pylab as pl
from matplotlib import collections as mc
import numpy as np
import math

pythagorean = lambda a, b: math.sqrt(a**2 + b**2)

def points_to_triangle(point1, point2, point3):
    """Set points coordinates and put on a list"""
    triangle = [list(point1), list(point2), list(point3)]
    return triangle

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

def plot_triangle_simple(triangle, thename):
    """Plot a simple triangle and its vertices"""
    fig, ax = pl.subplots()
    xs = [triangle[0][0], triangle[1][0], triangle[2][0]]
    ys = [triangle[0][1], triangle[1][1], triangle[2][1]]
    itin = [0,1, 2, 0]
    thelines = genlines(triangle, itin)
    lc = mc.LineCollection(genlines(triangle, itin), linewidths=2)
    
    ax.add_collection(lc)
    
    ax.margins(0.1)
    pl.scatter(xs, ys)
    pl.savefig(str(thename)+'.png')
    pl.close()

def triangle_to_circumcenter(triangle):
    """Find the circumcenter and circumradius"""
    x, y, z = complex(triangle[0][0], triangle[0][1]), \
              complex(triangle[1][0], triangle[1][1]), \
              complex(triangle[2][0], triangle[2][1])      
    #w = z - x
    #w /=y - x
    w = (z - x)/(y - x)    
    
    c = (x-y) * (w-abs(w)**2)  /2j/w.imag - x
    radius = abs(c+x)
    return (-c.real, -c.imag), radius

def plot_triangle(triangles, centers, radii, thename):
    """ """
    fig, ax = pl.subplots()
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    
    for i in range(0, len(triangles)):
        triangle = triangles[i]
        center = centers[i]
        radius = radii[i]
        itin = [0,1, 2, 0]
        thelines = genlines(triangle, itin)
        xs = [triangle[0][0], triangle[1][0], triangle[2][0]]
        ys = [triangle[0][1], triangle[1][1], triangle[2][1]]
        lc = mc.LineCollection(genlines(triangle, itin), linewidths=2)
        ax.add_collection(lc)
        ax.margins(0.1)
        pl.scatter(xs, ys)
        pl.scatter(center[0], center[1])
        circle = pl.Circle(center, radius, color='b', fill=False)
        ax.add_artist(circle)
    pl.savefig(str(thename)+'.png')
    pl.close()    


def plot_triangle_circum(triangles, centers, plotcircles=False, plotpoints=True, \
                         plottriangles=False, plotvoronoi=True, \
                         plotvpoints=False, thename=''):
    """ """
    fig, ax = pl.subplots()
    ax.set_xlim([-0.1, 1.1])
    ax.set_ylim([-0.1, 1.1])
    
    lines = []
    
    for i in range(0, len(triangles)):
        triangle = triangles[i]
        center = centers[i][0]
        radius = centers[i][1]
        itin = [0,1, 2, 0]
        thelines = genlines(triangle, itin)
        xs = [triangle[0][0], triangle[1][0], triangle[2][0]]
        ys = [triangle[0][1], triangle[1][1], triangle[2][1]]
        
        lc = mc.LineCollection(genlines(triangle, itin), linewidths=2)
        
        if plottriangles:        
            ax.add_collection(lc)
        if plotpoints:
            pl.scatter(xs, ys)
        ax.margins(0.1)
        
        if plotvpoints:        
            pl.scatter(center[0], center[1])
        
        circle = pl.Circle(center, radius, color='b', fill=False)
        
        if plotcircles:        
            ax.add_artist(circle)
        if plotvoronoi:
            for j in range(0, len(triangles)):
                commonpoints = 0
                for k in range(0, len(triangles[i])):
                    for n in range(0, len(triangles[j])):
                        if triangles[i][k] == triangles[j][n]:
                            commonpoints += 1
                if commonpoints == 2:
                    lines.append([list(centers[i][0]), list(centers[j][0])])
        
        lc = mc.LineCollection(lines, linewidths=1)
        ax.add_collection(lc)        
    pl.savefig(str(thename)+'.png')
    pl.close()    


def gen_delaunay(points):
    """ """
    delaunay = [points_to_triangle([-5, -5], [-5, 10], [10, -5])]
    number_of_points = 0
    
    while number_of_points < len(points):
        point_to_add = points[number_of_points]
        delaunay_index = 0
        invalid_triangles =[]
        
        while delaunay_index < len(delaunay):        
            circumcenter, radius = triangle_to_circumcenter(delaunay[delaunay_index])
            new_distance = get_distance(circumcenter, point_to_add)        
            if new_distance < radius:
                invalid_triangles.append(delaunay[delaunay_index])
            delaunay_index += 1
    
        points_in_invalid = []
        for i in range(0, len(invalid_triangles)):
            delaunay.remove(invalid_triangles[i])        
            for j in range(0, len(invalid_triangles[i])):
                points_in_invalid.append(invalid_triangles[i][j])
        points_in_invalid = [list(x) for x in set(tuple(x) for x in points_in_invalid)]
    
        for i in range(0, len(points_in_invalid)):
            for j in range(i + 1, len(points_in_invalid)):
                #count the number of times both of these are in the bad triangles
                count_ocurrences = 0
                for k in range(0, len(invalid_triangles)):
                    count_ocurrences += 1* (points_in_invalid[i] in invalid_triangles[k])* \
                                        (points_in_invalid[j] in invalid_triangles[k])
                if count_ocurrences == 1:
                    delaunay.append(points_to_triangle(points_in_invalid[i], \
                                    points_in_invalid[j], point_to_add))
        number_of_points += 1
    return delaunay

if __name__ == '__main__':
    
    #Plot a simple triangle
    a = (0.2, 0.8)
    b = (0.5, 0.2)
    c = (0.8, 0.7)
    center, radius = triangle_to_circumcenter(points_to_triangle(a, b, c))
    print(f"center: {center}")
    print(f"radius: {radius:.2f}")
    plot_triangle_simple(points_to_triangle(a, b, c), 'tri')

    #Plot circumscribed triangles
    a = (0.1, 0.1)
    b = (0.3, 0.6)
    c = (0.5, 0.2)
    triangle1 = points_to_triangle(a, b, c)
    center1, radius1 = triangle_to_circumcenter(triangle1) 
    
    a = (0.8, 0.1)
    b = (0.7, 0.5)
    c = (0.8, 0.9)
    triangle2 = points_to_triangle(a, b, c)
    center2, radius2 = triangle_to_circumcenter(triangle2)
    
    plot_triangle([triangle1, triangle2], [center1, center2], [radius1, radius2],'two')
    
    #Delaunay triangulation
    a = (0.2, 0.8)
    b = (0.5, 0.2)
    c = (0.8, 0.7)
    delaunay = [points_to_triangle(a, b, c)]
    point_to_add = [0.5, 0.5]
    N = 15
    np.random.seed(5201314)
    xs = np.random.rand(N)
    ys = np.random.rand(N)
    
    points = zip(xs, ys)
    listpoints = list(points)
    the_delaunay = gen_delaunay(listpoints)
    
    #Voronoi Diagram
    circumcenters = []
    for i in range(0, len(the_delaunay)):
        circumcenters.append(triangle_to_circumcenter(the_delaunay[i]))
    plot_triangle_circum(the_delaunay, circumcenters, thename='final')
    
    