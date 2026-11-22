# Bab 15: Abstraction
from abc import ABC, abstractmethod
import math


class BangunDatar(ABC):
    @abstractmethod
    def luas(self):
        pass


class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2


class Lingkaran(BangunDatar):
    def __init__(self, jari):
        self.jari = jari

    def luas(self):
        return round(math.pi * self.jari ** 2, 2)


for bangun in [Persegi(4), Lingkaran(7)]:
    print(type(bangun).__name__, "luas:", bangun.luas())
