import matplotlib.pyplot as plt
from matplotlib import collections as mc
from functools import reduce
import numpy as np

def drawlattice(name):
    """
    Draw a grid of points and save picture into variable 'name'
    """
    global n

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            plt.plot(i, j, 'o', c='black')
    plt.savefig(name)

def define_player_traces_colors():
    """
    
    """
    global game
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

def drawgame(name):
    """
    
    """
    global n, game

    colors2 = define_player_traces_colors()
    lc = mc.LineCollection(game, colors=colors2, linewidths=2)
    fig, ax = plt.subplots()
    draw_grid()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    plt.savefig(name)

def is_parallel():
    """
    
    """
    global start_line1, end_line1, start_line2, end_line2, game
    return ([(start_line1, end_line1 -1), (start_line2, end_line2 -1)] in game)

def is_left():
    """
    
    """
    global start_line1, end_line1, start_line2, end_line2, game
    return ([(start_line1, end_line1), (start_line2 -1, end_line2 -1)] in game)

def is_right():
    """
    
    """
    global start_line1, end_line1, start_line2, end_line2, game
    return ([(start_line1 +1, end_line1), (start_line2, end_line2 -1)] in game)            

def is_a_square():
    """
    
    """
    global start_line1, end_line1, start_line2, end_line2, game
    
    parallel = is_parallel()
    left = is_left()
    right = is_right()

    results = [parallel, left, right]
    all_true = lambda boolean_asserts: reduce(lambda x, y: x and y, boolean_asserts)
    return all_true(results)

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

        if end_line1 == end_line2 and is_a_square(): 
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

def remove_actions_taken(allposible):
    """
    
    """       
    global game

    no_taken_moves = [move for move in allposible if move not in game]
    return no_taken_moves

def get_all_posible_movements():
    """
    
    """
    global n, game

    allposible = get_vertical_movements(n)
    allposible.extend(get_horizontal_movements(n))
    allposible = remove_actions_taken(allposible)
    return allposible

def generate_tree(posible_moves, depth, maxdepth, game_so_far):
    tree = []
    for move in posible_moves:
        move_profile = [move]
        game2 = game_so_far.copy()
        game2.append(move)
        move_profile.append(score(game2))
    
        if depth < maxdepth:
            posible_moves2 = posible_moves.copy()
            posible_moves2.remove(move)
            move_profile.append(generate_tree(posible_moves2, depth+1, maxdepth, game2))
        else:
            move_profile.append([])
        tree.append(move_profile)
    return tree

def minimax(max_or_min, tree):
    """
    
    """
    allscores = []

    for move_profile in tree:
        if move_profile[2] == []:
            allscores.append(move_profile[1][0] - move_profile[1][1])
        else:
            move, score = minimax(-1 * max_or_min, move_profile[2])
            allscores.append(score)
    
    newlist = [score * max_or_min for score in allscores]
    bestscore = max(newlist)
    bestmove = np.argmax(newlist)

    return bestmove, (max_or_min * bestscore)

def play_to_win(gamesize):
    """
    
    """
    global game

    allposible = []

    for i in range(1, gamesize + 1):
        for j in range(2, gamesize + 1):
            allposible.append([(i,j),(i,j-1)])

    for i in range(1, gamesize):
        for j in range(1, gamesize + 1):
            allposible.append([(i,j),(i+1,j)])
    
    for move in allposible:
        if move in game:
            allposible.remove(move)   
    
    thetree = generate_tree(allposible, 0,3,game)
    move, score = minimax(1, thetree)

    return thetree[move][0]


if __name__ == '__main__':
    global game
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
    drawgame('gameinprogress.png')

    #Scoring Games
    print(f"{score(game)}\n")

    #Building our tree
    allposible = get_all_posible_movements()
    print(*allposible, sep='\n')
    print(f"{len(allposible)}\n")
    allposible = [ 
                    [(4,4),(4,3)],
                    [(4,1),(5,1)],
                 ]
    thetree = generate_tree(allposible,0,1,[])
    print(thetree)

    #Winning a Game
    game = [
            [(1,2),(1,1)],
            [(3,3),(4,3)],
            [(1,5),(2,5)],
            [(1,2),(2,2)],
            [(2,2),(2,1)],
            [(1,1),(2,1)],
            [(3,4),(3,3)],
            [(3,4),(4,4)],
           ]

    gamesize = 5
    print(play_to_win(gamesize))
            