def paint(width: int, height: int, char: str):
    painting = []
    for i in range(height):
        for j in range(width):
            print(char, end="")
        print()
    


ancho = int(input("Ingrese el ancho del dibujo\n:"))
altura = int(input("Ingrese la altura del dibujo\n:"))
caracter = input("Ingrese el caracter con es que se va a pintar\n:")

paint(ancho, altura, caracter)
