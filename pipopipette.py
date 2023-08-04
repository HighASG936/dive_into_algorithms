import matplotlib.pyplot as plt
from matplotlib import collections as mc

def drawlattice(name):
    """
    Draw a grid of points and save picture into variable 'name'
    """
    global n

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            plt.plot(i, j, 'o', c='black')
    plt.savefig(name)

def drawgame(name, game):
    """
    
    """
    global n

    colors2 = []

    for k in range(0, len(game)):
        if k % 2 == 0:
            colors2.append('red')
        else:
            colors2.append('blue')
    
    lc = mc.LineCollection(game, colors=colors2, linewidths=2)
    fig, ax = plt.subplots()

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            plt.plot(i, j, 'o', c='black')
    
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    plt.savefig(name)

def squarefinder(game):
    """
    
    """
    countofsquares = 0

    for line in game:
        parallel = False
        left = False
        right = False        
        if line[0][1] == line[1][1]:                        
            if [
                (line[0][0], line[0][1] -1), 
                (line[1][0], line[1][1] -1)
               ] in game:
                parallel = True        
            if [
                (line[0][0], line[0][1]), 
                (line[1][0] -1, line[1][1] -1)
               ] in game:
                left = True
            if [
                (line[0][0] +1, line[0][1]), 
                (line[1][0], line[1][1] -1)
               ] in game:
                right = True
            if parallel and left and right:
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
    print(score(game))
    

    