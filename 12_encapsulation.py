# Bab 12: Encapsulation
class RekeningBank:
    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Saldo tidak cukup")


rekening = RekeningBank("Karina", 100000)
rekening.setor(50000)
rekening.tarik(30000)
print("Saldo:", rekening.saldo)
