class Triangulo:
    def __init__(self, lado1:int, lado2:int, lado3: int):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def ladoMayor(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            return "Los lados son iguales"
        lados = [self.lado1, self.lado2, self.lado3]
        return max(lados)
    
triagulo1 = Triangulo(12, 10, 10)
print(triagulo1.ladoMayor())