print("--Ejercicio 1--")

def findNumber(numberArray: list, number: int | float):
    for index, value in enumerate(numberArray):
        if value == number:
            return index
    return None


array = [1,12,16,23]

print(f"El elemento se encuenta en el índice: {findNumber(array, 1)}")

print("--Ejercicio 2--")

def esBisiesto(year: int):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


year = int(input("Ingrese el año para saber si es bisiesto\n:"))
if esBisiesto(year):
    print(year, "es bisiesto")
else:
    print(year, "no es bisiesto")

print("--Ejercicio 3--")

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

print("--Ejercicio--4")

#Bubble Sort 
def sort(array):
    for i in range(len(array),1,-1):
        for j in range(0,i-1):
            if array[j]<array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]

lista = [1,6,3,4,5]
sort(lista) # muta el array original

print(lista)

print("--Ejercicio 5--")

def esPalindromo(frase: str):
    return frase == frase[::-1]

palabra = input("Ingrese una frase para saber si es palindromo\n:")

if esPalindromo(palabra):
    print(palabra, "es palindromo")
else:
    print(palabra, "no es palindromo")

print("--Ejercicio 6--")

def cantidadDeVocales(frase: str):
    cant = 0
    for letra in frase:
        if letra in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            cant += 1
    return cant

print(cantidadDeVocales("hola mi nombre es Octavio"))

print("--Ejercicio 7--")


def esStep(number:int):
    numberToString = str(number)
    cant = 0
    for i in range(len(numberToString)):
        if i != (len(numberToString) - 1):
            if abs(int(numberToString[i]) - int(numberToString[i+1])) == 1:
                cant += 1

    return cant == len(numberToString) - 1 

print(esStep(12321))