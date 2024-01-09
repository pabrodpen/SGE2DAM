#5. Escribir un programa python que dado una palabra diga si es un palíndromo. Un palídromo 
#Un palíndromo es una palabra, número o frase que se lee igual hacia adelante que hacia atrás. Ejemplo: reconocer

cadena="recronocer"

alReves=cadena[::-1]

if cadena==alReves:
    print(cadena+" es un palindromo")
else:
    print(cadena+" no es palindromo") 