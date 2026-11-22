# Bab 8: Function
def sapa(nama):
    return "Halo, " + nama


def tambah(a, b=0):
    return a + b


def jumlahkan(*angka):
    return sum(angka)


print(sapa("Karina"))
print(tambah(5, 3))
print(tambah(5))
print(jumlahkan(1, 2, 3, 4))
