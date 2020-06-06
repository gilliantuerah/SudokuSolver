def getKoordinat(angka, matrix):
    # fungsi yang mengembalikan array of point

    # array of koordinat
    array = []

    # map koordinat
    koordinat = {
        "x": None,
        "y": None
    }

    # iterasi di seluruh cell sudoku
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == angka:
                # convert dari indeks matriks ke koordinat xy
                koordinat["x"] = j
                koordinat["y"] = 8-i
                # masukkan ke dalam array
                array.append(koordinat.copy())
    return array


def koordinatToStr(x, y):
    # fungsi untuk mengembalikan string penulisan koordinat yang rapih dan
    # siap diprint/dimasukkan ke file eksternal

    # string
    strRet = ""
    strRet += " [ "+str(x)+" , "+str(y)+" ]"
    return strRet


def allKoorToStr(array):
    # fungsi untuk mengembalikan string penulisan semua koordinat dalam array

    # string
    strRet = ""
    # iterasi di setiap elemen array
    for el in array:
        strRet += koordinatToStr(el["x"], el["y"])+"\n"
    return strRet


def matrixToStr(matrix):
    # fungsi yang mengembalikan string hasil convert dari matrix yang rapih dan
    # siap diprint/dimasukkan ke file eksternal

    # string
    strReturn = ""
    # iterasi di setiap cell sudoku
    for i in range(9):
        if (i % 3 == 0):
            strReturn += " -------------------------\n"

        for j in range(9):

            if (j+1) % 3 == 0:

                if j == 8:
                    if(matrix[i][j] != 0):
                        strReturn += str(matrix[i][j])+" | \n"
                    else:
                        strReturn += "."+" | \n"
                else:
                    if(matrix[i][j] != 0):
                        strReturn += str(matrix[i][j])+" | "
                    else:
                        strReturn += "."+" | "
            elif j == 0:
                if(matrix[i][j] != 0):
                    strReturn += " | "+str(matrix[i][j])+" "
                else:
                    strReturn += " | "+"."+" "
            else:
                if(matrix[i][j] != 0):
                    strReturn += str(matrix[i][j]) + " "
                else:
                    strReturn += "." + " "
    strReturn += " -------------------------\n"
    return strReturn
