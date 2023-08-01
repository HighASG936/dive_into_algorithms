import math
import random
import time
import os


def printsquare(square):
    """Print formated square"""
    # Print labels of columns
    labels = ['[' + str(x) + ']' for x in range(0, len(square))]
    format_row = "{:>6}" * (len(labels) + 1)
    print(format_row.format("", *labels))

    # Print labels of rows and values of square
    for label, row in zip(labels, square):
        print(format_row.format(label, *row))

def rule1(x, n, upright):
    """First rule to fill magic square"""
    return (x + (-1**upright * n)) % n**2


def rule2(x, n, upleft):
    """Second rule to fill magic square"""
    return (x+(-1**upleft)) % n**2


def rule3(x, n, upleft):
    """Third rule to fill magic square"""
    return (x + (-1**upleft * (-n + 1))) % n**2

def get_we_can_go_list(entry_i, entry_j):
    """ """
    where_we_can_go = []

    if entry_i < (n - 1) and entry_j < (n - 1):
        where_we_can_go.append('down_right')
    if entry_i < (n - 1) and entry_j > 0:
        where_we_can_go.append('down_left')
    if entry_i > 0 and entry_j < (n - 1):
        where_we_can_go.append('up_right')
    if entry_i > 0 and entry_j > 0:
        where_we_can_go.append('up_left')
    return where_we_can_go

def get_where_to_go(entry_i, entry_j):
    """ """
    where_we_can_go = get_we_can_go_list(entry_i, entry_j)
    return random.choice(where_we_can_go)

def fillsquare(square, entry_i, entry_j, howfull):
    """
    Fill whole magic square
    """
    while sum(math.isnan(i) for row in square for i in row) > howfull:
        where_to_go = get_where_to_go(entry_i, entry_j)
        
        #With rule 1
        if where_to_go == 'up_right':
            new_entry_i = entry_i - 1
            new_entry_j = entry_j + 1
            square[new_entry_i][new_entry_j] = rule1(square[entry_i][entry_j], n, True)

        if where_to_go == 'down_left':
            new_entry_i = entry_i + 1
            new_entry_j = entry_j - 1
            square[new_entry_i][new_entry_j] = rule1(square[entry_i][entry_j], n, False)

        #With rule 2
        sum_entries = entry_i + entry_j
        if where_to_go == 'up_left' and sum_entries != n:
            new_entry_i = entry_i - 1
            new_entry_j = entry_j - 1
            square[new_entry_i][new_entry_j] = rule2(square[entry_i][entry_j], n, True)

        if where_to_go == 'down_right' and sum_entries != (n-2):
            new_entry_i = entry_i + 1
            new_entry_j = entry_j + 1
            square[new_entry_i][new_entry_j] = rule2(square[entry_i][entry_j], n, False)

        #With rule 3
        if where_to_go == 'up_left' and sum_entries == n:
            new_entry_i = entry_i - 1
            new_entry_j = entry_j - 1
            square[new_entry_i][new_entry_j] = rule3(square[entry_i][entry_j], n, True)

        if where_to_go == 'down_right' and sum_entries == (n-2):
            new_entry_i = entry_i + 1
            new_entry_j = entry_j + 1
            square[new_entry_i][new_entry_j] = rule3(square[entry_i][entry_j], n, False)

        entry_i = new_entry_i
        entry_j = new_entry_j

        os.system('clear')
        printsquare(square)
        time.sleep(0.1)        
    
    return square


def verifysquare(square):
    """Verify whether a given matrix is a magic square"""
    sums = []

    # Sum of rows
    rowsums = [sum(square[i]) for i in range(0, len(square))]
    sums.append(rowsums)

    # Sum of columns
    colsums = [sum(row[i] for row in square) for i in range(0, len(square))]
    sums.append(colsums)

    # Sum of main diagonal
    maindiag = sum(square[i][i] for i in range(0, len(square)))
    sums.append([maindiag])

    # Sum of anti diagonal
    antidiag = sum([square[i][len(square) - 1 - i] for i in range(0, len(square))])
    sums.append([antidiag])

    # Join all items in one list
    flattened = [j for i in sums for j in i]

    # Verify whether flattened have just only one value
    return len(list(set(flattened))) == 1

def start_with_central(n, square):
    """ """
    center_i = math.floor(n/2)
    center_j = math.floor(n/2)

    square[center_i][center_j] = int((n**2 + 1) / 2)
    square[center_i + 1][center_j] = 1
    square[center_i - 1][center_j] = n**2
    square[center_i][center_j + 1] = n**2 + 1 - n
    square[center_i][center_j - 1] = n
    
    entry_i = center_i
    entry_j = center_j
    square = fillsquare(square, entry_i, entry_j, (n**2)/2 - 4)


def rest_of_square(n, square):
    """ """
    entry_i = math.floor(n/2) + 1
    entry_j = math.floor(n/2)
    square = fillsquare(square, entry_i, entry_j, 0)
    square = [[n**2 if x == 0 else x for x in row] for row in square]

if __name__ == '__main__':
    n = 6
    square = [[float('NaN') for i in range(0, n)] for j in range(0, n)]
    start_with_central(n, square)
    rest_of_square(n, square)
    print(verifysquare(square))

