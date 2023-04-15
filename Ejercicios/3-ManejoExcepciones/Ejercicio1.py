terminado = False

while not terminado:
    print("1.Ingresar un numero")
    print("2.Salir")
    try:
        opcion = int(input(":"))
        match opcion:
            case 1:
                numero1 = int(input("numero 1:"))
                numero2 = int(input("numero 2:"))
                print(f"Suma: {str(numero1 + numero2)}")
            case 2:
                terminado = True
    except ValueError as e:
        print("Ingreso de datos no válido")
    
