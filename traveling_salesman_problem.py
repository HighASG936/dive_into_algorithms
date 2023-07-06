import math
import matplotlib.collections as mc
import matplotlib.pylab as pl
import numpy as np


pythagorean = lambda a, b: math.sqrt(a**2 + b**2)

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


def howfar(lines):
    """Calculate and return distance covered by salesman"""
    distance = 0
    for j in range(0, len(lines)):
        distance += get_distance(lines[j][1], lines[j][0])
    return distance


def plotitinerary(cities, itin, plottitle, thename):
    """Plot the itinerary of our salesman"""
    lc = mc.LineCollection(genlines(cities, itin), linewidths=2)
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    pl.scatter(x, y)
    pl.title(plottitle)
    pl.xlabel('X coordinate')
    pl.ylabel('Y coordinate')
    pl.savefig(thename + '.png')
    pl.close()


def findnearest(cities, idx,nnitinerary):
    """Find Nearest Neighbor"""
    point = cities[idx]
    mindistance = float('inf')
    minidx = -1

    for j in range(0, len(cities)):
        distance = get_distance(point, cities[j])
        if 0 < distance < mindistance and j not in nnitinerary:
            mindistance = distance 
            minidx = j
    return minidx


def donn(cities, N):
    """Do nearest neighbor algorithm"""
    nnitinerary = [0]
    for j in range(0, N -1):
        next = findnearest(cities, nnitinerary[len(nnitinerary) -1], nnitinerary)
        nnitinerary.append(next)
    return nnitinerary


def display_results(cities, itinerary, N,title_plot,name_picture):
    """Display plot and distance covered"""
    lines = genlines(cities, itinerary)
    total_distance = howfar(lines)
    print(f"{title_plot}:\t{total_distance:.2f} km")
    plotitinerary(cities, itinerary, f"'TSP - '{title_plot}", name_picture)


def generate_cities(random_seed, N):
    """Randomly generated the coordinates of each city"""
    np.random.seed(random_seed)
    x = np.random.rand(N)
    y = np.random.rand(N)    
    points = zip(x, y)
    cities = list(points)
    return x, y, cities


def perturb(cities, itinerary):
    """ """
    neighbors1 = math.floor(np.random.rand() * len(itinerary))
    neighbors2 = math.floor(np.random.rand() * len(itinerary))

    itinerary2 = itinerary.copy()

    itinerary2[neighbors1] = itinerary[neighbors2]
    itinerary2[neighbors2] = itinerary[neighbors1]

    distance1 = howfar(genlines(cities, itinerary))
    distance2 = howfar(genlines(cities, itinerary2))

    itinerarytoreturn = itinerary.copy()

    if distance1 > distance2:
        itinerarytoreturn = itinerary2.copy()

    return itinerarytoreturn.copy()


def perturb_sa1(cities, itinerary, time):
    """ """
    neighbors1 = math.floor(np.random.rand() * len(itinerary))
    neighbors2 = math.floor(np.random.rand() * len(itinerary))

    itinerary2 = itinerary.copy()

    itinerary2[neighbors1] = itinerary[neighbors2]
    itinerary2[neighbors2] = itinerary[neighbors1]

    distance1 = howfar(genlines(cities, itinerary))
    distance2 = howfar(genlines(cities, itinerary2))

    itinerarytoreturn = itinerary.copy()

    randomdraw = np.random.rand()
    temperature = 1/((time/1000)+1)

    if ((distance2 > distance1 and randomdraw < temperature) or 
        distance1 > distance2
        ):
        itinerarytoreturn = itinerary2.copy()

    return itinerarytoreturn.copy()

def perturb_sa2(cities, itinerary, time):
    """ """
    neighbors1 = math.floor(np.random.rand() * len(itinerary))
    neighbors2 = math.floor(np.random.rand() * len(itinerary))

    itinerary2 = itinerary.copy()

    randomdraw2 = np.random.rand()
    small = min(neighbors1, neighbors2)
    big = max(neighbors1, neighbors2)

    if randomdraw2 >= 0.55:
        itinerary2[small:big] = itinerary2[small:big][::-1]
    elif randomdraw2 < 0.45:
        tempitin = itinerary[small:big]
        del(itinerary2[small:big])
        neighbors3 = math.floor(np.random.rand() * len(itinerary))
        for j in range(0, len(tempitin)):
            itinerary2.insert(neighbors3 + j, tempitin[j])
    else:
        itinerary2[neighbors1] = itinerary[neighbors2]
        itinerary2[neighbors2] = itinerary[neighbors1]

    distance1 = howfar(genlines(cities, itinerary))
    distance2 = howfar(genlines(cities, itinerary2))

    itinerarytoreturn = itinerary.copy()

    randomdraw = np.random.rand()
    temperature = 1/((time/1000)+1)

    if ((distance2 > distance1 and randomdraw < temperature) or 
        distance1 > distance2
        ):
        itinerarytoreturn = itinerary2.copy()
    return itinerarytoreturn.copy()

def perturb_sa3(cities, itinerary, time, maxitin):
    """ """
    global mindistance
    global minitinerary
    global minidx    
    
    neighbors1 = math.floor(np.random.rand() * len(itinerary))
    neighbors2 = math.floor(np.random.rand() * len(itinerary))

    itinerary2 = itinerary.copy()
    randomdraw2 = np.random.rand()
    
    small = min(neighbors1, neighbors2)
    big = max(neighbors1, neighbors2)
    
    randomdraw = np.random.rand()

    if randomdraw2 >= 0.55:
        itinerary2[small:big] = itinerary2[small:big][::-1]
    elif randomdraw2 < 0.45:
        tempitin = itinerary[small:big]
        del(itinerary2[small:big])
        neighbors3 = math.floor(np.random.rand() * len(itinerary))
        for j in range(0, len(tempitin)):
            itinerary2.insert(neighbors3 + j, tempitin[j])
    else:
        itinerary2[neighbors1] = itinerary[neighbors2]
        itinerary2[neighbors2] = itinerary[neighbors1]

    distance1 = howfar(genlines(cities, itinerary))
    distance2 = howfar(genlines(cities, itinerary2))

    itinerarytoreturn = itinerary.copy()

    temperature = 1/((time/1000)+1)
    
    scale = 3.5
    if ((distance2 > distance1 and randomdraw < temperature) or 
        distance1 > distance2
        ):
        itinerarytoreturn = itinerary2.copy()

    reset = True
    resetthresh = 0.04
    if reset and (time - minidx) > (maxitin * resetthresh):
        itinerarytoreturn = minitinerary
        minidx = time
    
    if howfar(genlines(cities, itinerarytoreturn)) < mindistance:
        mindistance = howfar(genlines(cities, itinerary2))
        minitinerary = itinerarytoreturn
        minidx = time
    
    if abs(time - maxitin) <= 1:
        itinerarytoreturn = minitinerary.copy()

    return itinerarytoreturn.copy()


def siman(itinerary, cities):
    """ """
    global mindisance
    global minitinerary
    global minidx
    
    newitinerary = itinerary.copy()
    mindistance = howfar(genlines(cities, itinerary))
    minitinerary = itinerary
    minidx = 0
    
    maxitin = len(itinerary) * 50_000
    for t in range(0, maxitin):
        newitinerary = perturb_sa3(cities, newitinerary, t, maxitin)
    
    return newitinerary.copy()
    
    
def init_func():
    """ """
    global N
    global random_seed
    global time
    global mindistance
    global x, y
    global cities
    
    N = 40
    random_seed = 1729
    time = 500_000_000
    mindistance = float('inf')
    
    #Genetare hipotetical cities
    x, y, cities = generate_cities(random_seed, N)        
    
if __name__ == "__main__":

    #Initialize all variables
    init_func()

    #Itinerary secuentially generated 
    itinerary = list(range(0, N))
    display_results(cities, itinerary, N, 'Random Itinerary', 'figure2')

    #Itinerary generated by nearest neighbor algorithm
    itinerary = donn(cities, N)
    display_results(cities, itinerary, N, 'Nearest Neighbor', 'figure3')

    #Itinerary generated by perturb search
    itinerary = list(range(0, N))
    np.random.seed(random_seed)
    itinerary_ps = itinerary.copy()
    for n in range(0, len(itinerary)*50_000):
        itinerary_ps = perturb(cities, itinerary_ps)
    display_results(cities, itinerary_ps, N, 'Perturb search', 'figure4')    

    #Itinerary generated by simulated annealing
    itinerary = list(range(0, N))
    np.random.seed(random_seed)
    itinerary_ps = itinerary.copy()
    for n in range(0, len(itinerary)*50_000):
        itinerary_ps = perturb_sa1(cities, itinerary_ps, time)
    display_results(cities, itinerary_ps, N, 'Simulated Annealing', 'figure5')    

    #Itinerary generated by simulated annealing improved
    itinerary = list(range(0, N))
    np.random.seed(random_seed)
    itinerary_ps = itinerary.copy()
    for n in range(0, len(itinerary)*50_000):
        itinerary_ps = perturb_sa2(cities, itinerary_ps, time)
    display_results(cities, itinerary_ps, N, 'Tuned Simulated Annealing', 'figure6')

    #Itinerary generated by simulated annealing improved
    np.random.seed(random_seed)
    itinerary = list(range(N))
    nnitin = donn(cities, N)
    nnresult = howfar(genlines(cities, nnitin))
    simanitinerary = siman(itinerary, cities)
    simanresult = howfar(genlines(cities, simanitinerary))    
    print(f"Traveling Salesman Itinerary: {simanresult:.2f} km")
    plotitinerary(cities, simanitinerary, 'Traveling Salesman Itinerary - Simulated Annealing', 'figure7')
    print(f"{nnresult:.2}")
    print(f"{simanresult/nnresult:.2}%")
    
    
    