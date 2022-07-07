# Kalkulator.py

import os,sys,time

os.system ("clear")
print ("\033[1;34mUsername = AGHX Dan Password = AGNG")
time.sleep (2)

x = "AGHX"
y = "AGNG"

def login():
          user = input("Masukkan Username : ")
          pasw = input("Masukkan Password : ")
          if user == x and pasw == y:
              print ("Acces granted")
              time.sleep(2)
          else:
              print ("Acces danied")
              time.sleep(2)
              os.system("python mtk.py")

if __name__ == "__main__":
       login()

load = '-'
count = 0

for t in range(100):
      time.sleep(0.1)
      print(f'\rLOADING {t}℅ |{load}', end='', flush=True)
      count += 1
      if count == 3:
            count = 0
            load = '-'

os.system("clear")
time.sleep (5)
banner = """
<------------------------------------------------------>
Author    : AGHXZ
Github    : https://github.com/mrx231107
Instagram : agngx14
<------------------------------------------------------>
"""

os.system("clear")

banner = """
\033[1;33m<------------------------------------------------------>
Author    : AGNG
Github    : https://github.com/mrx231107
Instagram : agngx14
<------------------------------------------------------>
"""

print (banner)
print ("\033[1;33m<------------------------------------------------------>")
print ("1. Pertambahan")
print ("2. Pengurangan")
print ("3. Perkalian")
print ("4. Pembagian")
print ("<------------------------------------------------------>")
pilih = input("Masukkan Pilihan Anda : ")
if pilih == "1":
        angka_1 = int(input("Masukkan Angka Pertama : "))
        angka_2 = int(input("Masukkan Angka KeDua : "))
        total = angka_1 + angka_2
        print(f"Hasil Pertambahan={total}")

if pilih == "2":
        angka_1 = int(input("Masukkan Angka Pertama : "))
        angka_2 = int(input("Masukkan Angka Kedua : "))
        total = angka_1 - angka_2
        print(f"Hasil Pengurangan={total}")

if pilih == "3":
        angka_1 = int(input("Masukkan Angka Pertama : "))
        angka_2 = int(input("Masukkan Angka Kedua : "))
        total = angka_1 * angka_2
        print(f"Hasil Perkalian={total}")

if pilih == "4":
        angka_1 = int(input("Masukkan Angka Pertama : "))
        angka_2 = int(input("Masukkan Angka Kedua : "))
        total = angka_1 / angka_2
        print(f"Hasil Pembagian={total}")
