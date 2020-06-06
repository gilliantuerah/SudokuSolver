
def readFile(pathfile):
    # mengembalikan matriks 9x9
    # atau ditulis dengan array of array di setiap baris

    # matriks hasil yang akan di return
    mat = []

    # membaca tiap line ke array line
    with open(pathfile) as f:
        line = f.read().splitlines()

    for l in line:
        # split dengan spasi tiap line menjadi sebuah array
        arr = l.split()
        # convert isi arr into integer
        # convert '#' into 0
        for i in range(len(arr)):
            if arr[i] == '#':
                arr[i] = 0
            else:
                arr[i] = int(arr[i])
        # masukkan arr ke dalam matriks hasil
        mat.append(arr.copy())

    return mat


def writeFile(pathfile, string):
    f = open(pathfile, "w")
    f.write(string)
    f.close()
