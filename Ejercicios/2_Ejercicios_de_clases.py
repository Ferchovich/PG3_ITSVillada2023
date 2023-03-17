print("--Ejercicio 1--")

class Persona:
    def __init__(self, name: str, edad: int):
        self.name = name
        self.edad = edad
    
    def saludar(self):
        return f"Hola mi nombre es: {self.name}"

    def mayorDeEdad(self):
        return self.edad > 18

persona1 = Persona("Gustavo", 19)
print(persona1.saludar())
if persona1.mayorDeEdad():
    print(persona1.name, "es mayor de edad")
else:
    print(persona1.name, "es mayor de edad")
persona2 = Persona("Gabriel", 14)
print(persona2.saludar())
if persona2.mayorDeEdad():
    print(persona2.name, "es mayor de edad")
else: 
    print(persona2.name, "es menor de edad")

print("--Ejercicio 2--")

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

print("--Ejercicio 3--")

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

print("--Ejercicio 4--")

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

print("--Ejercicio 5--")

class Persona:
    def __init__(self, nombre:str, edad:int):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola mi nombre es: {self.nombre}"
class Empleado(Persona):
    def __init__(self, nombre: str, edad: int, sueldo:int):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
    def pagaImpuestos(self):
        if self.sueldo > 3000:
            return f"{self.nombre} tiene que pagar impuesto"
        return f"{self.nombre} no tiene que pagar impuesto"
persona = Persona("Gustavo", 19)
print(persona.saludar())

empleado = Empleado("Gabril", 22, 2500)
print(empleado.saludar())
print(empleado.pagaImpuestos())

print("-Ejercicio 6--")

class Familia:
    def __init__(self, padre:str, madre:str, hijos:list):
        self.padre = padre
        self.madre = madre 
        self.hijos = hijos
    def __str__(self):
        return f"""
        Padre: {self.padre}
        Madre: {self.madre}
        Hijos: {",".join(self.hijos)}
        """

flia = Familia("santiago", "andrea", ["Joaquin, Octavio"])

print(flia)