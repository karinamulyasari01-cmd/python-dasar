# Bab 16: Exception Handling
def bagi(a, b):
    try:
        hasil = a / b
    except ZeroDivisionError:
        print("Tidak bisa membagi dengan nol")
    except TypeError:
        print("Tipe data tidak sesuai")
    else:
        print("Hasil:", hasil)
    finally:
        print("Selesai")


bagi(10, 2)
bagi(10, 0)
bagi(10, "a")

try:
    angka = int("abc")
except ValueError:
    print("Input bukan angka")
