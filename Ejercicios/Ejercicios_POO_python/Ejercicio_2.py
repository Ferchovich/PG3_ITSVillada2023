class Alumno:
    def __init__(self, nombre: str, nota: int):
        self.nombre = nombre
        self.nota = nota
    
    def mostrarAtributos(self):
        print(f"{self.nombre} tiene un {self.nota}")
    

    def regularizar(self):
        return self.nota >= 6
    
alumno1 = Alumno("Gustavo", 10)

alumno1.mostrarAtributos()

if alumno1.regularizar():
    print(alumno1.nombre, "esta regularizado")
else:
    print(alumno1.nombre, "no esta regularizado")

alumno1 = Alumno("Gabriel", 5)

alumno1.mostrarAtributos()

if alumno1.regularizar():
    print(alumno1.nombre, "esta regularizado")
else:
    print(alumno1.nombre, "no esta regularizado")