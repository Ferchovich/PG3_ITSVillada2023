def cantidadDeVocales(frase: str):
    cant = 0
    for letra in frase:
        if letra in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            cant += 1
    return cant

print(cantidadDeVocales("hola mi nombre es Octavio"))



