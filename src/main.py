from pathlib import Path
from fileMatrix import readFile, writeFile
from solve import solve, isAnyZero
from matrix import getKoordinat, allKoorToStr, matrixToStr
from imgToMatrix import imgToMatrix
import os
import time
# path file
data_folder = Path("../test/")


def menuAwalSudoku():
    # clear screen
    os.system('cls')
    # menu
    # 1. image
    # 2. file txt
    print(" ! SUDOKU SOLVER !")
    print(" Pilih Menu :")
    print(" 1. Gambar")
    print(" 2. File")
    menu = input(" --> ")
    # jika inputan menu tidak valid
    while (menu != "1") and (menu != "2"):
        # pesan error
        print(" Masukkan menu yang valid !..")
        time.sleep(0.5)
        os.system('cls')
        print(" Pilih Menu :")
        print(" 1. Gambar")
        print(" 2. File")
        menu = input(" --> ")
    # matriks unsolved
    unsolved = None
    # aksi sesuai pilihan menu
    while unsolved is None:
        try:
            if menu == "1":
                # input nama file
                namaFile = input(" Masukkan Nama File Gambar : ")
                # read image
                unsolved = imgToMatrix(data_folder/namaFile)

            elif menu == "2":
                # input nama file
                namaFile = input(" Masukkan Nama File : ")
                # read file
                unsolved = readFile(data_folder/namaFile)

        except:
            # pesan error jika namaFile tidak valid
            print(" Masukkan Nama File yang Valid..")
            time.sleep(0.5)
            os.system('cls')
            pass

    return unsolved, namaFile


def mainSolveSudoku(unsolved, namaFile):

    # method untuk melakukan :
    # 1. print unsolved sudoku
    print(" ! SUDOKU SOLVER !")
    print(matrixToStr(unsolved))

    # 2. print solved sudoku
    print(" HASILLLL...")
    solved = solve(unsolved)
    print(matrixToStr(solved))

    # 3. print koordinat dengan angka lima
    print(" KOORDINAT ANGKA LIMA")
    lima = getKoordinat(5, unsolved)
    print(allKoorToStr(lima))

    # 4. write file to file eksternal dengan nama file : ans_[nama_file_tc].txt
    fileAns = "ans_"+namaFile
    stringToFile = " Solved Sudoku :\n" + \
        matrixToStr(solved)+" Koordinat Area Nomor 5 :\n"+allKoorToStr(lima)
    writeFile(data_folder/fileAns, stringToFile)


# main program
unsolved, namaFile = menuAwalSudoku()
print()
mainSolveSudoku(unsolved, namaFile)
