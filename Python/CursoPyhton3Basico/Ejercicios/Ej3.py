#calcular area y perimetro de un circulo dado el radio

import math

radio=float(input("Radio:"))

perimetro=2*math.pi*radio
area=2*math.pi*math.pow(radio,2)

print("Perimetro: "+str(perimetro)+"\n")
print("Area:" +str(area))