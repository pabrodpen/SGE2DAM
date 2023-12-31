#ver si una letra es mayus o minus

letra=str(input("Letra:"))

if letra>="A" and letra <="Z":
    print(letra+" es mayuscula")
elif letra>="a" and letra<="z":
    print(letra+" es minuscula")