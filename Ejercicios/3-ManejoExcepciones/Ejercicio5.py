
while True:
    palabra = input("Ingrese una palabra:")
    try:
        if palabra.isnumeric():
            raise TypeError("Se pueden ingresar solo numeros al archivo")
    except TypeError as e:
        print(f"Error: {e}")

    with open("archivo.txt", "a") as f:
        f.write(palabra)
        f.write("\n")

