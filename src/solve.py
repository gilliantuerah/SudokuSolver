from cekCell import cekCell


def solve(matrix):
    # jika tidak ada angka nol di matriks maka sudoku solved
    if not isAnyZero(matrix):
        return matrix
    else:
        # iterasi di setiap cell sudoku
        for i in range(9):
            for j in range(9):
                # untuk cell kosong
                if matrix[i][j] == 0:
                    # iterasi dari angka 1 sampai 9
                    # panggil fungsi cekCell
                    for k in range(1, 10):
                        # jika ada angka yang possible
                        if(cekCell(i, j, k, matrix)):
                            # angka k me-replace matrix[i][j]
                            matrix[i][j] = k
                            # memanggil fungsi solve
                            if(solve(matrix)):
                                return matrix
                            # jika sudoku not solved maka kembalikan matrix[i][j] ke 0
                            matrix[i][j] = 0
                    # jika tidak ditemukan angka yang cocok, maka return none (sudoku belum solved)
                    return None


def isAnyZero(matrix):
    # fungsi mengembalikan true jika masih terdapat 0 di dalam matrix (sudoku)

    # melakukan iterasi di semua cell sudoku
    for i in range(9):
        for j in range(9):
            # jika ditemukan angka 0 return true
            if matrix[i][j] == 0:
                return True
    return False
