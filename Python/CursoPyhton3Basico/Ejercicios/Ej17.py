#lee una caden y muestra:iniciales, la cadena con las iniciales en mayus y las palabras que empiecen por a

cadena="hola como astas"

iniciales,mayus,palabrasA="","",""

arr=cadena.split(" ")
for i in arr:
    iniciales+=i[0]
    mayus += i[0].upper() + i[1:] + " "#IMP EL 1:
    if i.startswith('A') | i.startswith('a'):
        palabrasA+=i+","

print("Iniciales:"+iniciales)
print("Palabras con mayusculas en las iniciales:"+mayus)
print("Palabras que empiezan por a:"+palabrasA)