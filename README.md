# Sudoku Solver
## Deskripsi
Program yang di desain untuk dapat memecahkan persoalan sudoku melalui gambar dan file txt.
<br/>
Program dibuat dengan menggunakan bahasa pemrograman **Python** dan kakas **Tesseract** yang digunakan untuk mengekstrak gambar.

## Pembuat
Name : Felicia Gillian Tekad Tuerah
<br/>
NIM : 13518070

## Instalasi
### Kebutuhan
Beberapa Hal yang Dibutuhkan:
1. [Python 3.0 or above](https://www.python.org/)
2. [Tesseract](https://pypi.org/project/pytesseract/). Ubah path tesseract.exe pada file imgToMatrix.py dalam directory src.

### Cara Kompilasi Program ?
1. Membuka CMD / terminal , pastikan anda sudah berada di directory src
2. Jalankan program
```
python main.py
```
**Notes : Program mampu menampilkan pesan error jika ada command yang kurang sesuai**
## Strategi Pencarian Solusi
Pencarian solusi dilakukan dengan memanfaatkan algoritma **Backtracking**. Pemilihan algoritma ini karena dirasa paling cocok dan sistematis dalam menyelesaikan permasalahan sudoku. Hal ini karena algoritma ini bekerja mirip dengan algoritma brute-force tapi dengan versi yang lebih baik sehingga mampu menghasilkan solusi yang optimal dengan waktu yang efisien. Algoritma backtracking bekerja dengan mengambil kemungkinan solusi yang ada dan menelusurinya menuju cell terakhir. Jika ternyata tidak ditemukan solusi, maka algoritma ini akan kembali ke posisi sebelumnya dan mengambil solusi yang mungkin selanjutnya.
<br/>
Kompleksitas Waktu = O(n³)

## Library
Pada pembuatan program ini, saya menggunakan library **Tesseract** untuk mengekstrak gambar menjadi data yang bisa diolah. Menurut saya, library ini memiliki kelebihan yaitu sangat teliti dalam mengenali goresan/tulisan pada gambar. Kelemahan dari library ini yakni dikarenakan pendeteksi yang terlalu teliti sehingga beberapa noise ataupun kotoran pada gambar sulit untuk diabaikan.

## Referensi
Thanks To :
1. StackOverflow
2. [Analisis Penyelesaian Sudoku dengan Algoritma Backtracking](http://stmikasia.ac.id/laravel-filemanager/files/shares/5976b38e60cb2.pdf)