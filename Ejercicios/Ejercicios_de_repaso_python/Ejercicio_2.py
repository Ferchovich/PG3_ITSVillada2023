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

