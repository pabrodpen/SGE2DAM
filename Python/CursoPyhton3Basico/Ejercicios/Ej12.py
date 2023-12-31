#introducir numeros en una lista hasta un numero negativo. Muestra los pares, mx y min

n=int(input("Dime un numero:"))
suma,max,min=0,n,n

while(n>=0):
    suma+=n
    if max<=n:
        max=n
    elif min>=n:
        min=n
    n=int(input("Dime un numero:"))

print("Suma:"+str(suma))
print("Maximo:"+str(max))
print("Minimo:"+str(min))