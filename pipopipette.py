import matplotlib.pyplot as plt
from matplotlib import collections as mc
from functools import reduce

def drawlattice(name):
    """
    Draw a grid of points and save picture into variable 'name'
    """
    global n

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            plt.plot(i, j, 'o', c='black')
    plt.savefig(name)

def define_player_traces_colors(game):
    """
    
    """
    colors2 = []

    for k in range(0, len(game)):
        if k % 2 == 0:
            colors2.append('red')
        else:
            colors2.append('blue')
    return colors2

def draw_grid():
    """

    """
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            plt.plot(i, j, 'o', c='black')

def drawgame(name, game):
    """
    
    """
    global n

    colors2 = define_player_traces_colors(game)
    lc = mc.LineCollection(game, colors=colors2, linewidths=2)
    fig, ax = plt.subplots()
    draw_grid()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    plt.savefig(name)

def is_parallel(game):
    """
    
    """
    global start_line1, end_line1, start_line2, end_line2
    return ([(start_line1, end_line1 -1), (start_line2, end_line2 -1)] in game)

def is_left(game):
    """
    
    """
    global start_line1, end_line1, start_line2, end_line2
    return ([(start_line1, end_line1), (start_line2 -1, end_line2 -1)] in game)

def is_right(game):
    """
    
    """
    global start_line1, end_line1, start_line2, end_line2
    return ([(start_line1 +1, end_line1), (start_line2, end_line2 -1)] in game)            

def logical_and(x, y):
    return x and y

def is_a_square(game):
    """
    
    """
    global start_line1, end_line1, start_line2, end_line2
    
    parallel = is_parallel(game)
    left = is_left(game)
    right = is_right(game)

    results = [parallel, left, right]
    return reduce(logical_and, results)

def squarefinder(game):
    """
    
    """
    global start_line1, end_line1, start_line2, end_line2

    countofsquares = 0

    for line in game:  
        
        start_line1 = line[0][0]
        end_line1 = line[0][1]
        
        start_line2 = line[1][0]
        end_line2 = line[1][1]

        if end_line1 == end_line2 and is_a_square(game): 
            countofsquares += 1

        return countofsquares

def score(game):
    """
    
    """
    score = [0,0]
    progress = []
    squares = 0

    for line in game:
        progress.append(line)
        newsquares = squarefinder(progress)
        if newsquares > squares:
            if len(progress) % 2  == 0:
                score[1] = score[1] + 1
            else:
                score[0] = score[0] + 1
        squares = newsquares
    return score


def get_vertical_movements(gamesize):
    """
    
    """
    vertical_movements = []
    
    for i in range(1, gamesize +1):
        for j in range(2, gamesize +1):
            vertical_movements.append([(i,j), (i,j-1)])
    return vertical_movements

def get_horizontal_movements(gamesize):
    """
    
    """
    horizontal_movements = []
    
    for i in range(1, gamesize):
        for j in range(1, gamesize +1):
            horizontal_movements.append([(i,j), (i+1,j)])
    return horizontal_movements

def remove_actions_taken(game, allposible):
    """
    
    """       
    no_taken_moves = [move for move in allposible if move not in game]
    return no_taken_moves

def get_all_posible_movements(game):
    """
    
    """
    global n

    allposible = get_vertical_movements(n)
    allposible.extend(get_horizontal_movements(n))
    allposible = remove_actions_taken(game, allposible)
    return allposible

if __name__ == '__main__':
    n = 5
    game = [ 
                [(1,2), (1,1)], 
                [(3,3), (4,3)], 
                [(1,5), (2,5)], 
                [(1,2), (2,2)], 
                [(2,2), (2,1)], 
                [(1,1), (2,1)], 
                [(3,4), (3,3)], 
                [(3,4), (4,4)], 
           ]
    
    #Drawing the board
    drawlattice('lattice.png')
    
    #Representing Games
    drawgame('gameinprogress.png', game)

    #Scoring Games
    print(f"{score(game)}\n")

    #Build out tree
    allposible = get_all_posible_movements(game)
    print(*allposible, sep='\n')
    print(f"{len(allposible)}\n")

    