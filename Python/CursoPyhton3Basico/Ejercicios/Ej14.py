#di si una lista esta ordernada o no

lista=[1,3,5,2]
lista2=lista.copy()
lista.sort()
if lista==lista2:
    print("Esta ordenada")
else:
    print("No esta ordenada")