#crea una cadena y ve si esta en la lista y cuantas veces aparece. 
#Lee otra cadena y sustituyela por la otra. Borra esa cadena de la lista

lista=["hola","que","hola","estas"]
cadena=input("Cadena:")

if cadena in lista:
    print("Esta en la cadena")
    nVeces=lista.count(cadena)
    print("Aparece "+str(nVeces)+" veces")
    nueva=input("Nueva cadena:")
    for i in range(0,len(lista)-1):
        if lista[i]==cadena:
            lista[i]=nueva

    print(lista)
else:
    print("No esta en la lista")





