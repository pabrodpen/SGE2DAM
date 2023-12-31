#dados minutos, convertir en horas y min

minutos=int(input("Minutos:"))

h=(int)(minutos/60)
min=minutos%60

print("Horas: "+str(h)+" , Minutos: "+str(min))