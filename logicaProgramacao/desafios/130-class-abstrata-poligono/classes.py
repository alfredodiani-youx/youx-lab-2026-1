from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, lados):
        self.lados = lados

    @classmethod
    def perimetro(self):
        pass
class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(lado)
        self.lado = lado

    def perimetro(self):
        return self.lado * 4
    def area(self):
        return self.lado * self.lado
