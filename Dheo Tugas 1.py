from msilib.schema import BBControl
"""Nama : Dheo Ariansyah
   Nim  : 222410102016"""

print("Tugas Algoritma Mencari Nilai Ganjil & Genap")
nilai_bb = int(input("Masukkan Angka"))
nilaiGG = nilai_bb
if nilai_bb %2==0:
    nilaiGG = "Genap"
    (nilaiGG)
else :
    nilaiGG = "Ganjil"
    (nilaiGG)
if nilai_bb <10 :
    print("Bilangan ini adalah bilangan",nilaiGG,"Dan juga termasuk dalam nilai yang kecil")
if 10 <=nilai_bb<=50 :
    print("Bilangan ini adalah bilangan",nilaiGG,"Dan juga termasuk dalam nilai yang sedang")
if nilai_bb >50:
    print("Bilangan ini adalah bilangan",nilaiGG,"Dan juga termasuk dalam bilangan yang besar")
print("Ini adalah sebuah tugas dari ALgoritma")