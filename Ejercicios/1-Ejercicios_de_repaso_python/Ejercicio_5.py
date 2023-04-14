
def esPalindromo(frase: str):
    return frase == frase[::-1]

palabra = input("Ingrese una frase para saber si es palindromo\n:")

if esPalindromo(palabra):
    print(palabra, "es palindromo")
else:
    print(palabra, "no es palindromo")