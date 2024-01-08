#Introducir cadena y caracter.Sustituir todos los caracteres digitos por el caracter

cadena="Hol4 com0 e5tas"
caracter='#'
nueva=""
for i in cadena:
    if i.isdigit():
        nueva+=caracter
    else:
        nueva+=i

print("Nueva cadena:"+nueva)