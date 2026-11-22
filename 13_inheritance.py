# Bab 13: Inheritance
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        return "..."


class Kucing(Hewan):
    def suara(self):
        return "Meong"


class Anjing(Hewan):
    def __init__(self, nama, ras):
        super().__init__(nama)
        self.ras = ras

    def suara(self):
        return "Guk guk"


kucing = Kucing("Mimi")
anjing = Anjing("Doggo", "Labrador")
print(kucing.nama, kucing.suara())
print(anjing.nama, anjing.ras, anjing.suara())
