import pytesseract as tesseract
from PIL import Image
tesseract.pytesseract.tesseract_cmd = r'C:\Users\gillian tuerah\AppData\Local\Tesseract-OCR\tesseract.exe'


def imgToMatrix(imgPath):
    # mengembalikan matriks 9x9 hasil extract image

    # matriks hasil yang akan di return
    mat = [[0 for i in range(9)]for j in range(9)]

    img = Image.open(imgPath)

    # get the img size
    w, h = img.size
    # crop img
    for i in range(9):
        for j in range(9):
            l = (w/9)*i + 4
            r = (w/9)*(i+1) - 2.5
            t = (h/9)*j + 4
            b = (h/9)*(j+1) - 2
            img1 = img.crop((l, t, r, b))
            # get number from each cropped image
            getNum = tesseract.image_to_string(img1, config='--psm 6')
            # masukkin ke matriks
            mat[j][i] = getNum
    # convert isi matriks into integer
    # convert "" into 0
    for i in range(9):
        for j in range(9):
            if(mat[i][j] == ""):
                mat[i][j] = 0
            else:
                mat[i][j] = int(mat[i][j])

    return mat
