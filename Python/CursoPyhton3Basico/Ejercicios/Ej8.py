#ver si un año es bisiesto o no

año=int(input("Año:"))

if año%4==0:
    print(str(año)+" es bisiesto")
else:
    print(str(año)+" no es bisiesto")