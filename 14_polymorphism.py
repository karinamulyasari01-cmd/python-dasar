# Bab 14: Polymorphism
class Burung:
    def bergerak(self):
        return "Terbang"


class Ikan:
    def bergerak(self):
        return "Berenang"


class Kucing:
    def bergerak(self):
        return "Berjalan"


for hewan in [Burung(), Ikan(), Kucing()]:
    print(type(hewan).__name__, "->", hewan.bergerak())
