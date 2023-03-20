
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