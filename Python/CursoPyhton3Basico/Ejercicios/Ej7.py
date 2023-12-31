#decir si la suma de 2 numeros es +, - o 0

n1=int(input("Primer numero:"))
n2=int(input("Segundo numero:"))

suma=n1+n2

if suma>0:
    print("La suma es positiva")
elif suma<0:
    print("La suma es negativa")
else:
    print("La suma es 0")

