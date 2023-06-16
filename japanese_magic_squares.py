import math

#luoshu = [[4,9,2],[3,5,7],[8,1,6]]

n = 3
square = [[float('NaN') for i in range(0,n)] for j in range(0,n)]

def printsquare(square):
    """Print formated square"""
    # Print labels of columns
    labels = ['['+str(x)+']'  for x in range(0, len(square))]
    format_row = "{:>6}" * (len(labels) + 1)
    print (format_row.format("", *labels))

    #Print labels of rows and values of square
    for label, row in zip(labels, square):
        print (format_row.format(label, *row))

def fill_central_squares(square):
    """Fill central cells of magic square"""
    center_i = math.floor(n/2)
    center_j = math.floor(n/2)

    square[center_i][center_j] = int((n**2+1)/2)
    square[center_i + 1][center_j] = 1
    square[center_i -1][center_j] = n**2
    square[center_i][center_j +1] = n**2 + 1 - n
    square[center_i][center_j -1] = n

def rule1(x, n, upright):
    """First rule to fill magic square"""
    return((x + (-1**upright * n))%n**2)

def verifysquare(square):
    """Verify whether a given matrix is a magic square"""
    sums =[]

    # Sum of rows
    rowsums = [sum(square[i]) for i in range(0,len(square))]
    sums.append(rowsums)

    # Sum of columns
    colsums = [sum(row[i] for row in square) for i in range(0,len(square))]
    sums.append(colsums)

    # Sum of main diagonal
    maindiag = sum(square[i][i] for i in range(0,len(square)))
    sums.append([maindiag])

    # Sum of anti diagonal
    antidiag = sum([square[i][len(square) -1 -i] for i in range(0,len(square))])
    sums.append([antidiag])

    # Join all items in one list
    flattened = [j for i in sums for j in i]

    # Verify whether flattened have just only one value
    return(len(list(set(flattened))) == 1)

if __name__ == '__main__':
    print(rule1(1,3,True))
    #fill_central_squares(square)
    #printsquare(square)
