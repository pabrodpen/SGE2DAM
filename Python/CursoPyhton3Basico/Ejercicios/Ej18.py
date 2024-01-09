#4. Escribir funciones que dadas dos cadenas de caracteres:

#Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, cadena es una subcadena de subcadena.
#Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe kde y gnome debe devolver gnome.

cadena1="aola"
cadena2="hola que tal"

if cadena1 in cadena2:
    print("Es una subcadena")
else:
    print("No es una subcadena")

if cadena1<cadena2:
    print(cadena1)
else:
    print(cadena2)