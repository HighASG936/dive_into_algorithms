
luoshu = [[4,9,2],[3,5,7],[8,1,6]]

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
    print(verifysquare(luoshu))
