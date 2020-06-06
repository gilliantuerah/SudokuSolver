def cekCell(row, col, what, matrix):
    # fungsi yang mengembalikan boolean
    # mengembalikan True jika what bisa menempati matriks[row][col]
    # yakni memenuhi aturan sudoku
    # otherwise : False

    return(cekRow(row, what, matrix) and cekCol(col, what, matrix) and cekSquare(row, col, what, matrix))


def cekRow(row, what, matrix):
    # mengembalikan boolean
    # True jika what bisa menempati row tersebut
    # (jika dalam row belum terdapat what)

    acc = True  # boolean
    i = 0  # iterasi
    while(acc) and (i < 9):
        # jika isi cell adalah what
        if(matrix[row][i] == what):
            acc = False
        else:
            i += 1
    return acc


def cekCol(col, what, matrix):
    # mengembalikan boolean
    # True jika what bisa menempati column tersebut
    # (jika dalam col belum terdapat what)

    acc = True  # boolean
    i = 0  # iterasi
    while(acc) and (i < 9):
        # jika isi cell adalah what
        if(matrix[i][col] == what):
            acc = False
        else:
            i += 1
    return acc


def cekSquare(row, col, what, matrix):
    # mengembalikan boolean
    # True jika what bisa menempati square tersebut
    # (jika dalam square belum terdapat what)

    # boolean
    acc = True
    # starting index of col
    col0 = (col//3)*3
    # starting index of row
    row0 = (row//3)*3
    for i in range(row0, row0+3):
        for j in range(col0, col0+3):
            # jika isi cell adalah what
            if(matrix[i][j] == what):
                acc = False
                break
    return acc
