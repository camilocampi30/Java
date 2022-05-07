class Operaciones:
    def __init__(self, valorA, valorB):
        self.valorA = valorA
        self.valorB = valorB

    def calcularSuma(self):
        resultado = self.valorA
        resultado += self.valorB
        return resultado
    def calcularResta(self):
        resultado = self.valorA - self.valorB
        return resultado
    def calcularmultiplicacion(self):
        resultado = self.valorA * self.valorB
        return resultado
    def calcularDivision(self):
        resultado = self.valorA / self.valorB
        return resultado
