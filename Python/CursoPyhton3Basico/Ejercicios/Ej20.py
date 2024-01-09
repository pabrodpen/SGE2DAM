#1. Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de 
#apariciones de cada palabra en la cadena. Por ejemplo, si recibe “Qué lindo día que hace hoy” debe devolver: 
#‘que’: 2, ‘lindo’: 1, ‘día’: 1, ‘hace’: 1, ‘hoy’: 1
from unidecode import unidecode

cadena="Qué lindo dia hace hoy"
dic={}

for i in cadena:
    i=i.lower
    i=unidecode(i)
    dic[i]=cadena.count(i)

print(dic)
