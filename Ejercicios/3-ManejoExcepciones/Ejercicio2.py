
try:
    numero1 = int(input("Ingrese un numero: "))
    numero2 = int(input("Ingrese otro numero: "))
    print(f"División: {str(numero1 / numero2)}")

except ZeroDivisionError:
    print("No se puede dividir por cero")