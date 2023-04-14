class Operacion:
    def __init__(self, num1: int, num2: int) -> None:
        self.num1 = num1
        self.num2 = num2
    def suma(self):
        print(self.num1 + self.num2)
    def resta(self):
        print(self.num1 - self.num2)
    def multiplicacion(self):
        print(self.num1 * self.num2)
    def division(self):
        if self.num2 != 0:
            print(self.num1 / self.num2)
        else:
            raise Exception("No puedes dividir un numero por 0")

op = Operacion(10, 20)

op.suma()
op.resta()
op.multiplicacion()
op.division()