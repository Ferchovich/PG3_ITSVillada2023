
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
