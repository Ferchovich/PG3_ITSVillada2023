meses = tuple(["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"])
terminado = False
while not terminado:
    try:
        numero = int(input("Ingrese un numero de mes del año: "))
        print(meses[numero-1])
    except ValueError:
        print("Ingreso no valido")
    except IndexError:
        print("El indice esta fuera de rango, el mes no existe")
