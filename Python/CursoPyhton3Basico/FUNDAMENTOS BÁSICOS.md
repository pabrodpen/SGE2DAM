- [Operadores](#Operadores)
-  [Funciones básicas](#Funciones Básicas)
- [Sección 2](#sección-2)
- [Sección 2](#sección-2)
  - [Subsección A](#subsección-a)
  - [Subsección B](#subsección-b)
- [Sección 3](#sección-3)


![[cap1Python.png]]
## Operadores

![[cap3Python 1.png]]
![[cap6Pyhton.png]]
**Se pueden declarar varias variables a la vez
![[cap11Python.png]]
Así se pasa por teclado
## Funciones Básicas

#### Función para parsear
Simplemente se usa el tipo de dato y entre () el valor que se quiere parsear
~~~
a=(int)("2")
~~~
#### Función Type
devuelve el tipo de dato que se pasa
~~~
type(a)
~~~
![[cap4PythonFuncionType.png]]
#### Función insinstance
Devuelve true o false si el objeto es parte de la clase
~~~
isinstance(5,int)
~~~

#### Imprimir
![[cap8PythonImprimir.png]]![[cap9PythonImprimir.png]]
#### Operaciones Matemáticas
![[cap10PythonOperacionesMatematicas.png]]
Funciones a octal,hexadecimal y binario

La función round() en Python se utiliza para redondear un número a la cantidad especificada de dígitos decimales o al entero más cercano si no se proporciona ningún número de dígitos decimales.
~~~
round(numero[, ndigits])
~~~

## IF-ELSE
~~~
if n>0:
	print("positivo")
elif n<0:
	 print("negativo")
else:
	 print("es cero")
~~~

## WHILE
~~~
while año<=2017:
	print("Informe del año")
~~~

## FOR
![[cap3PyFor.png]]
**Recorriendo un array**
![[ForEnUnArray.png]]
**Recorriendo 2 arrays a la vez**
![[Recorrer2ForALaVez.png]]

## LISTAS

##### TRATO BÁSICO

**IMPRIMIR, VER SI UN ELEMENTO ESTÁ Y AÑADIR ELEMENTOS**
![[capListas.png]]

**OTRAS FUNCIONES**(len es la longitud)
![[capListas2.png]]
**ACCEDER A UN ELEMENTO, LISTAR UNA PARTE DE LA LISTA(:) Y REPETIR UNA LISTA(*2)**
![[capListas3.png]]

![[listarListas2.png]]
**MÉTODO LIST
Crea una lista a partir de una secuencia
![[Captura2.png]]

ORDENAR LISTA Y ENUMERARLA
![[cp3.png]]

FORMA EN LA QUE AL ASIGNAR UNA LISTA A OTRA, ESTA ES **DEPENDIENTE** DE ELLA
![[cp4.png]]
ASÍ SE CREA UNA LISTA A PARTIR DE OTRA SIENDO **INDEPENDIENTE** DE LA OTRA
![[CrearListaAPartirDeOtraPeroSinDependerDeElla.png]]
Se puede hacer con el metodo copy también

**LISTAS A PARTIR DE OTRAS LISTAS(MATRICES)**
![[Matrices.png]]

![[Matrices2.png]]

##### MÉTODOS DE LISTA

1. **`append(elemento)`**:
    
    - Agrega un elemento al final de la lista.
    
    `lista = [1, 2, 3] lista.append(4) print(lista)  # Salida: [1, 2, 3, 4]`
    
2. **`copy()`**:
    
    - Crea y devuelve una copia superficial (shallow copy) de la lista.
    
    `lista_original = [1, 2, 3] copia_lista = lista_original.copy()`
    
3. **`clear()`**:
    
    - Elimina todos los elementos de la lista.
        
    `lista = [1, 2, 3] lista.clear() print(lista)  # Salida: []`
    
4. **`count(elemento)`**:
    
    - Devuelve el número de veces que aparece un elemento en la lista.
    
    `lista = [1, 2, 2, 3, 4, 2] cuenta = lista.count(2) print(cuenta)  # Salida: 3`
    
5. **`extend(iterable)`**:
    
    - Agrega los elementos de un iterable (como otra lista) al final de la lista actual.
    
    `lista1 = [1, 2, 3] lista2 = [4, 5, 6] lista1.extend(lista2) print(lista1)  # Salida: [1, 2, 3, 4, 5, 6]`
    
6. **`index(elemento[, inicio[, fin]])`**:
    
    - Devuelve el índice del primer elemento igual al proporcionado. Puedes especificar opcionalmente los índices de inicio y fin.
    
    `lista = [1, 2, 3, 4, 3] indice = lista.index(3) print(indice)  # Salida: 2`
    
7. **`insert(posición, elemento)`**:
    
    - Inserta un elemento en la posición especificada.
        
    `lista = [1, 2, 3] lista.insert(1, 4) print(lista)  # Salida: [1, 4, 2, 3]`
    
8. **`pop([índice])`**:
    
    - Elimina y devuelve el elemento en la posición dada. Si no se proporciona un índice, se eliminará y devolverá el último elemento.
    
    `lista = [1, 2, 3] elemento = lista.pop(1) print(elemento)  # Salida: 2`
    
9. **`remove(elemento)`**:
    
    - Elimina la primera aparición del elemento especificado.
    
    `lista = [1, 2, 3, 2] lista.remove(2) print(lista)  # Salida: [1, 3, 2]`
    
10. **`reverse()`**:
    
    - Invierte el orden de los elementos en la lista.

    `lista = [1, 2, 3] lista.reverse() print(lista)  # Salida: [3, 2, 1]`
    
11. **`sort(key=None, reverse=False)`**:
    
    - Ordena los elementos de la lista. Puedes proporcionar una función `key` opcional para personalizar el ordenamiento y usar `reverse=True` para ordenar en orden descendente.
    
    `lista = [3, 1, 4, 1, 5, 9, 2] lista.sort() print(lista)  # Salida: [1, 1, 2, 3, 4, 5, 9]`

##### MÉTODO MAP

La función map() es una función incorporada que se utiliza para aplicar una función a todos los elementos de un iterable (por ejemplo, una lista) y devuelve un nuevo iterable con los resultados.
~~~
map(función, iterable)
~~~

![[metodoMap.png]]

##### MÉTODO FILTER

El método filter()  se utiliza para filtrar elementos de una secuencia (como una lista, tupla o conjunto) según una función que se proporciona como primer argumento. La función de filtro toma cada elemento de la secuencia y devuelve `True` o `False` según si el elemento debe incluirse o no en el resultado final.

~~~
filter(func, iterable)
~~~

![[metodoFilter.png]]

##### MÉTODO REDUCE

~~~
from functools import reduce

#Definir una función que multiplica dos números
def multiplicar(x, y):
    return x * y

 #Crear una lista de números
numeros = [1, 2, 3, 4, 5]

#Calcular el producto de la lista usando reduce
producto = reduce(multiplicar, numeros)

#Mostrar el resultado
print(producto)
~~~

##### LISTAS COMPRIMIDAS

Lista de cubos de cada elemento
~~~
[x ** 3 for x in [1,2,3,4,5]]
#-->[1,8,27,64,125]
~~~
Lista de pares del 0 al 10
~~~
[x for x in range(10) if x%2==0]
#-->[0,2,4,6,8]
~~~
Lista de las sumas de 2 listas(1 + 4, 1 + 5, 1 + 6, 2 + 4, y así sucesivamente.)
~~~
[x +y for x in [1,2,3] for y in [4,5,6]]
#-->[5,6,7,6,7,8,7,8,9]
~~~

## TUPLAS
Son listas inmutables(no se pueden cambiar)

![[Tuplas1.png]]

![[Tuplas2.png]]

##### MÉTODOS

count(valor)-->contar cuantas veces aparece un valor en la tupla
index(valor)-->obtiene el índice de la primera aparición de un valor en la tupla

## RANGOS

![[Rangos1.png]]

##### MÉTODOS

start-->devuelve el valor inicial del rango
stop-->devuelve el valor final del rango
step-->devuelve el intervalo del rango


## STRINGS

![[Strings.png]]

##### MÉTODOS


1. **`capitalize()` - Capitaliza la primera letra de una cadena:**

    `cadena = "hola mundo" resultado = cadena.capitalize() # resultado: "Hola mundo"`
    
2. **`casefold()` - Convierte la cadena a minúsculas y aplica reglas específicas para comparación de cadenas:**
    
    `cadena = "HOLA Mundo" resultado = cadena.casefold() # resultado: "hola mundo"`
    
3. **`center(width)` - Centra la cadena en un ancho especificado con espacios:**
    
    `cadena = "Python" resultado = cadena.center(10) # resultado: "  Python  "`
    
4. **`count(subcadena)` - Cuenta cuántas veces aparece una subcadena en la cadena:**
    
    `cadena = "python es poderoso, python es genial" resultado = cadena.count("python") # resultado: 2`
    
5. **`encode(encoding)` - Codifica la cadena utilizando la codificación especificada:**
    
    `cadena = "Hola" resultado = cadena.encode("utf-8") # resultado: b'Hola'`
    
6. **`endswith(suffix)` - Verifica si la cadena termina con la subcadena especificada:**
    
    `cadena = "Hola mundo" resultado = cadena.endswith("mundo") # resultado: True`
    
7. **`expandtabs(tabsize)` - Expande las tabulaciones en la cadena:**
        
    `cadena = "Python\tes\tgenial" resultado = cadena.expandtabs(4) # resultado: "Python  es  genial"`
    
8. **`find(subcadena)` - Encuentra la primera posición de una subcadena en la cadena:**
        
    `cadena = "Python es divertido" resultado = cadena.find("es") # resultado: 7`
    
9. **`format(*args, **kwargs)` - Formatea la cadena con valores proporcionados:**
        
    `nombre = "Juan" edad = 25 resultado = "Hola, me llamo {} y tengo {} años".format(nombre, edad) # resultado: "Hola, me llamo Juan y tengo 25 años"`
    
10. **`format_map(mapping)` - Similar a `format`, pero utiliza un diccionario como fuente de datos:**
    
	`datos = {'nombre': 'Maria', 'edad': 30} resultado = "Hola, me llamo {nombre} y tengo {edad} años".format_map(datos) # resultado: "Hola, me llamo Maria y tengo 30 años"`

11. **`index(subcadena)`**:
    
    - Retorna el índice de la primera aparición de la subcadena.
        
    `mensaje = "Hola, mundo" print(mensaje.index("m"))  # Salida: 2`
    
12. **`isalnum()`**:
    
    - Retorna `True` si todos los caracteres de la cadena son alfanuméricos.
        
    `texto = "abc123" print(texto.isalnum())  # Salida: True`
    
13. **`isalpha()`**:
    
    - Retorna `True` si todos los caracteres de la cadena son alfabéticos.
        
    `palabra = "Hola" print(palabra.isalpha())  # Salida: True`
    
14. **`isdecimal()`**:
    
    - Retorna `True` si todos los caracteres de la cadena son decimales.
        
    `numero = "123" print(numero.isdecimal())  # Salida: True`
    
15. **`isdigit()`**:
    
    - Retorna `True` si todos los caracteres de la cadena son dígitos.
        
    `digito = "42" print(digito.isdigit())  # Salida: True`
    
16. **`islower()`**:
    
    - Retorna `True` si todos los caracteres de la cadena están en minúsculas.
        
    `texto = "hola" print(texto.islower())  # Salida: True`
    
17. **`isnumeric()`**:
    
    - Retorna `True` si todos los caracteres de la cadena son numéricos.
        
    `num = "123" print(num.isnumeric())  # Salida: True`
    
18. **`isprintable()`**:
    
    - Retorna `True` si todos los caracteres de la cadena son imprimibles.
        
    `cadena = "Hola\nMundo" print(cadena.isprintable())  # Salida: False`
    
19. **`isspace()`**:
    
    - Retorna `True` si todos los caracteres de la cadena son espacios en blanco.
        
    `espacio = "   " print(espacio.isspace())  # Salida: True`
    
20. **`istitle()`**:
    

- Retorna `True` si la cadena sigue el formato de título (cada palabra comienza con mayúscula).

`titulo = "Hola Mundo" print(titulo.istitle())  # Salida: True`

21. **`isupper()`**:

- Retorna `True` si todos los caracteres de la cadena están en mayúsculas.

`mayusculas = "HOLA" print(mayusculas.isupper())  # Salida: True`

22. **`join(iterable)`**:

- Combina los elementos del iterable con la cadena como separador.

`lista = ["Hola", "Mundo"] resultado = "-".join(lista) print(resultado)  # Salida: "Hola-Mundo"`

23. **`ljust(width)`**:

- Justifica la cadena a la izquierda en un ancho dado.

`palabra = "Hola" resultado = palabra.ljust(10) print(resultado)  # Salida: "Hola      "`

24. **`lower()`**:

- Convierte la cadena a minúsculas.

`texto = "HoLa MuNdO" print(texto.lower())  # Salida: "hola mundo"`

25. **`lstrip()`**:

- Elimina los espacios en blanco a la izquierda de la cadena.

`cadena = "   Hola Mundo" resultado = cadena.lstrip() print(resultado)  # Salida: "Hola Mundo"`

26. **`maketrans()`**:

- Crea una tabla de traducción para `translate()`.

`origen = "aeiou" destino = "12345" tabla = str.maketrans(origen, destino)`

27. **`partition(separador)`**:

- Divide la cadena en tres partes usando el separador.

`frase = "Hola-Mundo" resultado = frase.partition("-") print(resultado)  # Salida: ('Hola', '-', 'Mundo')`

28. **`replace(antiguo, nuevo)`**:

- Reemplaza todas las ocurrencias de la subcadena antigua con la nueva.

`texto = "Hola Mundo" resultado = texto.replace("Hola", "Adiós") print(resultado)  # Salida: "Adiós Mundo"`

29. **`rfind(subcadena)`**:

- Retorna el índice de la última aparición de la subcadena.

`frase = "Hola Mundo Mundo" print(frase.rfind("Mundo"))  # Salida: 12`

30. **`rindex(subcadena)`**:

- Retorna el índice de la última aparición de la subcadena.

`frase = "Hola Mundo Mundo" print(frase.rindex("Mundo"))  # Salida: 12`

31. **`rjust(width)`**:

- Justifica la cadena a la derecha en un ancho dado.

`palabra = "Hola" resultado = palabra.rjust(10) print(resultado)  # Salida: "      Hola"`

32. **`rpartition(separador)`**:

- Divide la cadena en tres partes usando el separador, comenzando desde el final.

`frase = "Hola-Mundo-Otra-Vez" resultado = frase.rpartition("-") print(resultado)  # Salida: ('Hola-Mundo-Otra', '-', 'Vez')`

33. **`rsplit(separador)`**:

- Divide la cadena en una lista de palabras, comenzando desde el final.

`frase = "Hola Mundo Otra Vez" resultado = frase.rsplit(" ", 2) print(resultado)  # Salida: ['Hola Mundo', 'Otra', 'Vez']`

34. **`rstrip()`**:

- Elimina los espacios en blanco a la derecha de la cadena.

`cadena = "Hola Mundo    " resultado = cadena.rstrip() print(resultado)  # Salida: "Hola Mundo"`

35. **`split(separador)`**:

- Divide la cadena en una lista de palabras.

`frase = "Hola Mundo" resultado = frase.split(" ") print(resultado)  # Salida: ['Hola', 'Mundo']`

36. **`splitlines()`**:

- Divide la cadena en una lista de líneas.

`texto = "Hola\nMundo" resultado = texto.splitlines() print(resultado)  # Salida: ['Hola', 'Mundo']`

37. **`startswith(prefijo)`**:

- Retorna `True` si la cadena comienza con el prefijo especificado.

`texto = "Hola Mundo" print(texto.startswith("Hola"))  # Salida: True`

38. **`strip()`**:

- Elimina los espacios en blanco al principio y al final de la cadena.

`cadena = "   Hola Mundo    " resultado = cadena.strip() print(resultado)  # Salida: "Hola Mundo"`

39. **`swapcase()`**:

- Intercambia mayúsculas y minúsculas en la cadena.

`texto = "HoLa MuNdO" print(texto.swapcase())  # Salida: "hOlA mUnDo"`

40. **`title()`**:

- Convierte la cadena a formato de título (cada palabra comienza con mayúscula).

`frase = "hola mundo" print(frase.title())  # Salida: "Hola Mundo"`

41. **`translate(tabla)`**:

- Aplica una tabla de traducción creada por `maketrans()`.

`texto = "abc" tabla = str.maketrans("abc", "123") resultado = texto.translate(tabla) print(resultado)  # Salida: "123"`

42. **`upper()`**:

- Convierte la cadena a mayúsculas.

`texto = "hola mundo" print(texto.upper())  # Salida: "HOLA MUNDO"`

43. **`zfill(width)`**:

- Rellena la cadena con ceros a la izquierda hasta alcanzar la longitud especificada.

`numero = "42" resultado = numero.zfill(5) print(resultado)  # Salida: "00042"`


## CONJUNTOS

Son listas que tienen un orden específico, no contiene elementos repetidos y son mutables, aunque no se puede ni acceder ni modificar un elemento en específico

### SET

Son mutables.MÉTODOS
1. **`add(elemento)` - Agrega un elemento al conjunto:**
        
    `conjunto = {1, 2, 3} conjunto.add(4) # conjunto ahora es {1, 2, 3, 4}`
    
2. **`clear()` - Elimina todos los elementos del conjunto:**
        
    `conjunto = {1, 2, 3} conjunto.clear() # conjunto ahora es set()`
    
3. **`copy()` - Retorna una copia superficial del conjunto:**
        
    `conjunto = {1, 2, 3} copia_conjunto = conjunto.copy() # copia_conjunto es {1, 2, 3}`
    
4. **`difference(iterable)` - Retorna un nuevo conjunto con elementos que están en el conjunto pero no en el iterable:**
        
    `conjunto1 = {1, 2, 3} conjunto2 = {2, 3, 4} diferencia = conjunto1.difference(conjunto2) # diferencia es {1}`
    
5. **`difference_update(iterable)` - Elimina del conjunto los elementos que están en el iterable:**
        
    `conjunto1 = {1, 2, 3} conjunto2 = {2, 3, 4} conjunto1.difference_update(conjunto2) # conjunto1 ahora es {1}`
    
6. **`discard(elemento)` - Elimina un elemento del conjunto si está presente:**
        
    `conjunto = {1, 2, 3} conjunto.discard(2) # conjunto ahora es {1, 3}`
    
7. **`intersection(iterable)` - Retorna un nuevo conjunto con elementos que están en ambos conjuntos:**
    
    `conjunto1 = {1, 2, 3} conjunto2 = {2, 3, 4} interseccion = conjunto1.intersection(conjunto2) # interseccion es {2, 3}`
    
8. **`intersection_update(iterable)` - Actualiza el conjunto con elementos que están en ambos conjuntos:**
        
    `conjunto1 = {1, 2, 3} conjunto2 = {2, 3, 4} conjunto1.intersection_update(conjunto2) # conjunto1 ahora es {2, 3}`
    
9. **`isdisjoint(iterable)` - Retorna `True` si no hay elementos comunes entre los conjuntos:**
        
    `conjunto1 = {1, 2} conjunto2 = {3, 4} resultado = conjunto1.isdisjoint(conjunto2) # resultado es True`
    
10. **`issubset(iterable)` - Retorna `True` si todos los elementos del conjunto están en el iterable:**
    
`conjunto1 = {1, 2} conjunto2 = {1, 2, 3, 4} resultado = conjunto1.issubset(conjunto2) # resultado es True`

11. **`issuperset(iterable)` - Retorna `True` si el conjunto contiene todos los elementos del iterable:**

`conjunto1 = {1, 2, 3, 4} conjunto2 = {1, 2} resultado = conjunto1.issuperset(conjunto2) # resultado es True`

12. **`pop()` - Remueve y retorna un elemento aleatorio del conjunto:**

`conjunto = {1, 2, 3} elemento = conjunto.pop() # elemento es un elemento aleatorio, y conjunto ahora es {1, 2} o similar`

13. **`remove(elemento)` - Remueve un elemento del conjunto. Genera un error si el elemento no está presente:**

`conjunto = {1, 2, 3} conjunto.remove(2) # conjunto ahora es {1, 3}`

14. **`symmetric_difference(iterable)` - Retorna un nuevo conjunto con elementos que están en uno de los conjuntos, pero no en ambos:**

`conjunto1 = {1, 2, 3} conjunto2 = {3, 4, 5} diferencia_simetrica = conjunto1.symmetric_difference(conjunto2) # diferencia_simetrica es {1, 2, 4, 5}`

15. **`symmetric_difference_update(iterable)` - Actualiza el conjunto con elementos que están en uno de los conjuntos, pero no en ambos:**

`conjunto1 = {1, 2, 3} conjunto2 = {3, 4, 5} conjunto1.symmetric_difference_update(con``junto2) # conjunto1 ahora es {1, 2, 4, 5}`

16. **`union(iterable)` - Retorna un nuevo conjunto con todos los elementos de ambos conjuntos:**

`conjunto1 = {1, 2, 3} conjunto2 = {3, 4, 5} union = conjunto1.union(conjunto2) # union es {1, 2, 3, 4, 5}`

17. **`update(iterable)` - Actualiza el conjunto con elementos de otro conjunto o iterable:**

`conjunto1 = {1, 2, 3} conjunto2 = {3, 4, 5} conjunto1.update(conjunto2) # conjunto1 ahora es {1, 2, 3, 4, 5}`

### FROZENSET

Son inmutables.MÉTODOS
1. **`copy()` - Copia el frozenset:**
    
    - El método `copy()` devuelve una copia superficial del frozenset.
        
        `frozenset1 = frozenset([1, 2, 3]) frozenset2 = frozenset1.copy() print(frozenset2)  # Salida: frozenset({1, 2, 3})`
        
2. **`difference(other)` - Diferencia de frozensets:**
    
    - El método `difference()` retorna un nuevo frozenset que contiene elementos que están en el frozenset original pero no en el `other`.
                
        `frozenset1 = frozenset([1, 2, 3, 4]) frozenset2 = frozenset([3, 4, 5]) result = frozenset1.difference(frozenset2) print(result)  # Salida: frozenset({1, 2})`
        
3. **`intersection(other)` - Intersección de frozensets:**
    
    - El método `intersection()` retorna un nuevo frozenset que contiene elementos que están presentes en ambos frozensets.
                
        `frozenset1 = frozenset([1, 2, 3, 4]) frozenset2 = frozenset([3, 4, 5]) result = frozenset1.intersection(frozenset2) print(result)  # Salida: frozenset({3, 4})`
        
4. **`isdisjoint(other)` - Verifica si son disjuntos:**
    
    - El método `isdisjoint()` retorna `True` si no hay elementos comunes entre los dos frozensets.
                
        `frozenset1 = frozenset([1, 2, 3]) frozenset2 = frozenset([4, 5, 6]) result = frozenset1.isdisjoint(frozenset2) print(result)  # Salida: True`
        
5. **`issubset(other)` - Verifica si es subconjunto:**
    
    - El método `issubset()` retorna `True` si todos los elementos del frozenset están presentes en el `other`.
                
        `frozenset1 = frozenset([1, 2]) frozenset2 = frozenset([1, 2, 3, 4]) result = frozenset1.issubset(frozenset2) print(result)  # Salida: True`
        
6. **`issuperset(other)` - Verifica si es superconjunto:**
    
    - El método `issuperset()` retorna `True` si todos los elementos del `other` están presentes en el frozenset.
                
        `frozenset1 = frozenset([1, 2, 3, 4]) frozenset2 = frozenset([1, 2]) result = frozenset1.issuperset(frozenset2) print(result)  # Salida: True`
        
7. **`symmetric_difference(other)` - Diferencia simétrica de frozensets:**
    
    - El método `symmetric_difference()` retorna un nuevo frozenset con elementos que están en uno de los frozensets, pero no en ambos.
                
        `frozenset1 = frozenset([1, 2, 3, 4]) frozenset2 = frozenset([3, 4, 5]) result = frozenset1.symmetric_difference(frozenset2) print(result)  # Salida: frozenset({1, 2, 5})`
        
8. **`union(other)` - Unión de frozensets:**
    
    - El método `union()` retorna un nuevo frozenset que contiene todos los elementos de ambos frozensets.
                
        `frozenset1 = frozenset([1, 2, 3]) frozenset2 = frozenset([3, 4, 5]) result = frozenset1.union(frozenset2) print(result)  # Salida: frozenset({1, 2, 3, 4, 5})`


## DICCIONARIOS

Conjunto de pares(clave,valor)
![[Dicc1.png]]

Trato básico
![[Dicc2.png]]

EJEMPLO
![[Dicc3.png]]

MÉTODOS

1. **`clear()` - Limpia el diccionario:**
    
    - El método `clear()` elimina todos los elementos del diccionario.
                
        `diccionario = {'a': 1, 'b': 2} diccionario.clear() print(diccionario)  # Salida: {}`
        
2. **`copy()` - Copia el diccionario:**
    
    - El método `copy()` devuelve una copia superficial del diccionario.
                
        `diccionario = {'a': 1, 'b': 2} copia_diccionario = diccionario.copy()`
        
3. **`fromkeys(iterable, value=None)` - Crea un diccionario con claves de un iterable:**
    
    - El método `fromkeys()` crea un nuevo diccionario con claves tomadas de un iterable y asigna un valor opcional a todas las claves.
                
        `claves = ['a', 'b', 'c'] valor_predeterminado = 0 nuevo_diccionario = dict.fromkeys(claves, valor_predeterminado)`
        
4. **`get(key, default=None)` - Obtiene el valor asociado a una clave:**
    
    - El método `get()` devuelve el valor asociado con una clave, o un valor predeterminado si la clave no está presente.
                
        `diccionario = {'a': 1, 'b': 2} valor = diccionario.get('a', 0)`
        
5. **`items()` - Retorna una vista de pares clave-valor:**
    
    - El método `items()` retorna una vista de todos los pares clave-valor en el diccionario.
    
        `diccionario = {'a': 1, 'b': 2} pares = diccionario.items()`
        
6. **`keys()` - Retorna una vista de las claves:**
    
    - El método `keys()` retorna una vista de todas las claves en el diccionario.
                
        `diccionario = {'a': 1, 'b': 2} claves = diccionario.keys()`
        
7. **`pop(key, default)` - Elimina y retorna el valor asociado a una clave:**
    
    - El método `pop()` elimina la clave y retorna su valor. Si la clave no está presente, retorna el valor predeterminado.
                
        `diccionario = {'a': 1, 'b': 2} valor = diccionario.pop('a', 0)`
        
8. **`popitem()` - Elimina y retorna un par clave-valor arbitrario:**
    
    - El método `popitem()` elimina y retorna un par clave-valor arbitrario del diccionario.
                
        `diccionario = {'a': 1, 'b': 2} par = diccionario.popitem()`
        
9. **`setdefault(key, default=None)` - Retorna el valor de una clave; si no existe, la agrega con un valor predeterminado:**
    
    - El método `setdefault()` retorna el valor asociado con una clave. Si la clave no está presente, la agrega con el valor predeterminado.
                
        `diccionario = {'a': 1, 'b': 2} valor = diccionario.setdefault('c', 0)`
        
10. **`update(iterable)` - Actualiza el diccionario con elementos de otro iterable o diccionario:**
    
    - El método `update()` agrega pares clave-valor de otro diccionario o iterable al diccionario actual.
                
        `diccionario = {'a': 1, 'b': 2} diccionario.update({'b': 3, 'c': 4})`
        
11. **`values()` - Retorna una vista de los valores:**
    
    - El método `values()` retorna una vista de todos los valores en el diccionario.
                
        `diccionario = {'a': 1, 'b': 2} valores = diccionario.values()`
        
**OTROS MÉTODOS**
![[metodosDicc2.png]]

![[metodosDicc3.png]]

## FICHEROS

##### DE TEXTO

**PERMISOS
![[AbrirFicheros.png]]

**ABRIR
`fichero=open("ejemplo1.txt","r")-->lo abrimos en modo lectura

**CERRAR
`fichero.close()``

**LEER
`fichero.read()`
Al leer cursor se queda donde se ha acabado de leer
Leer por lineas-->fichero.readlines()

**VER DONDE ESTÁ EL CURSOR
`fichero.tell()`
para reiniciarlo-->.seek()

**ESCRIBIR
`fichero.write("Mensaje")`
.writelines("Mensaje")

**RECORRER UN FICHERO Y MOSTRARLO

~~~
with open("ejemplo.txt","r") as fichero:
	for linea in fichero
		print(linea)
~~~


##### CSV
import csv

*OPEN,CLOSE Y SEEK SE MANTIENEN*

**RECOGER CONTENIDO DE UN FICHERO

~~~
fichero=open("fichero.txt","r")
contenido=csv.reader(fichero)

list(contenido)
~~~

Vemos los datos. En este ejemplo es un fichero con 2 columnas separados por comas:
`datos[0][0]=...`

~~~
for row in contenido:
	print("Fila ")+str(contenido.line_num)+" "+str(row)
~~~
devuelve-->Fila 22 ...

PONER OTRO SEPARADOR

`contenido=csv.reader(fichero,quotechar='"'`

**ESCRIBIR

`csv.writer`
para líneas-->`csv.writerow`

##### JSON
import json

*OPEN,CLOSE Y SEEK SE MANTIENEN*



**COGER CONTENIDO DE UNA CADENA JSON**
*Una cadena JSON (JavaScript Object Notation) es una forma de representar datos estructurados que es fácilmente legible tanto para humanos como para máquinas.

EJEMPLO DE SINTAXIS DE CADENA JSON*
~~~
{
  "nombre": "Juan",
  "edad": 30,
  "ciudad": "Nueva York",
  "empleo": {
    "titulo": "Desarrollador de software",
    "empresa": "ABC Tech"
  },
  "intereses": ["programación", "viajar", "lectura"]
}


~~~
Se asemeja a un *mapa*

ASÍ SE PASA DE UNA CADENA JSON A UN ELEMENTO MAPEABLE(DICCIONARIO)
~~~

# Cadena JSON
cadena_json = '{"nombre": "Juan", "edad": 30, "ciudad": "Nueva York"}'

# Parsear la cadena JSON en un diccionario Python
diccionario = json.loads(cadena_json)

print(diccionario)

~~~


**COGER CONTENIDO DE UN FICHERO JSON**

~~~
with open("ejemplo1.json") as fichero:
	datos=json.load(fichero)
~~~

*CONTENIDO DEL FICHERO JSON AL MOSTRAR EL MAPA*
![[json3.png]]

para ver un dato cualquiera:
![[json2.png]]

**ESCRIBIR(UNA CADEN JSON EN UN FICHERO JSON)**

![[json4.png]]


## EXCEPCIONES

*EJEMPLO DE TRY-CATCH*

![[try_catch.png]]


## MÓDULOS

### Módulos de sistemas

##### Módulo os

El módulo [os](https://docs.python.org/3.4/library/os.html#module-os) nos permite acceder a funcionalidades dependientes del Sistema Operativo. Sobre todo, aquellas que nos refieren información sobre el entorno del mismo y nos permiten manipular la estructura de directorios.

|Descripción|Método|
|---|---|
|Saber si se puede acceder a un archivo o directorio|`os.access(path, modo_de_acceso)`|
|Conocer el directorio actual|`os.getcwd()`|
|Cambiar de directorio de trabajo|`os.chdir(nuevo_path)`|
|Cambiar al directorio de trabajo raíz|`os.chroot()`|
|Cambiar los permisos de un archivo o directorio|`os.chmod(path, permisos)`|
|Cambiar el propietario de un archivo o directorio|`os.chown(path, permisos)`|
|Crear un directorio|`os.mkdir(path[, modo])`|
|Crear directorios recursivamente|`os.mkdirs(path[, modo])`|
|Eliminar un archivo|`os.remove(path)`|
|Eliminar un directorio|`os.rmdir(path)`|
|Eliminar directorios recursivamente|`os.removedirs(path)`|
|Renombrar un archivo|`os.rename(actual, nuevo)`|
|Crear un enlace simbólico|`os.symlink(path, nombre_destino)`|

```
>>> import os
>>> os.getcwd()
'/home/jose/github/curso_python3/curso/u40'
>>> os.chdir("..")
>>> os.getcwd()
'/home/jose/github/curso_python3/curso'
```

El módulo os también nos provee del submódulo path (os.path) el cual nos permite acceder a ciertas funcionalidades relacionadas con los nombres de las rutas de archivos y directorios.

|Descripción|Método|
|---|---|
|Ruta absoluta|`os.path.abspath(path)`|
|Directorio base|`os.path.basename(path)`|
|Saber si un directorio existe|`os.path.exists(path)`|
|Conocer último acceso a un directorio|`os.path.getatime(path)`|
|Conocer tamaño del directorio|`os.path.getsize(path)`|
|Saber si una ruta es absoluta|`os.path.isabs(path)`|
|Saber si una ruta es un archivo|`os.path.isfile(path)`|
|Saber si una ruta es un directorio|`os.path.isdir(path)`|
|Saber si una ruta es un enlace simbólico|`os.path.islink(path)`|
|Saber si una ruta es un punto de montaje|`os.path.ismount(path)`|

##### Ejecutar comandos del sistema operativo. Módulo subprocess

Con la función `system()` del módulo `os` nos permite ejecutar comandos del sistema operativo.

```
>>> os.system("ls")
curso  modelo.odp  README.md
0
```

La función nos devuelve un código para indicar si la instrucción se ha ejecutado con éxito.

Tenemos otra forma de ejecutar comandos del sistema operativo que nos da más funcionalidad, por ejemplo nos permite guardar la salida del comando en una variable. Para ello podemos usar el módulo [subprocess](https://docs.python.org/3.4/library/subprocess.html)

```
>>> import subprocess
>>> subprocess.call("ls")
curso  modelo.odp  README.md
0

>>> salida=subprocess.check_output("ls")
>>> print(salida.decode())
curso
modelo.odp
README.md

>>> salida=subprocess.check_output(["df","-h"])

>>> salida = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE)
>>> salida.communicate()[0]
```

##### Módulo shutil

El módulo [shutil](https://docs.python.org/3.4/library/shutil.html#module-shutil) de funciones para realizar operaciones de alto nivel con archivos y directorios. Dentro de las operaciones que se pueden realizar está copiar, mover y borrar archivos y directorios; y copiar los permisos y el estado de los archivos.

|Descripción|Método|
|---|---|
|Copia un fichero complero o parte|`shutil.copyfileobj(fsrc, fdst[, length])`|
|Copia el contenido completo (sin metadatos) de un archivo|`shutil.copyfile(src, dst, *, follow_symlinks=True)`|
|copia los permisos de un archivo origen a uno destino|`shutil.copymode(src, dst, *, follow_symlinks=True)`|
|Copia los permisos, la fecha-hora del último acceso, la fecha-hora de la última modificación y los atributos de un archivo origen a un archivo destino|`shutil.copystat(src, dst, *, follow_symlinks=True)`|
|Copia un archivo (sólo datos y permisos)|`shutil.copy(src, dst, *, follow_symlinks=True)`|
|Copia archivos (datos, permisos y metadatos)|`shutil.move(src, dst, copy_function=copy2)`|
|Obtiene información del espacio total, usado y libre, en bytes|`shutil.disk_usage(path)`|
|Obtener la ruta de un archivo ejecutable|`shutil.chown(path, user=None, group=None)`|
|Saber si una ruta es un enlace simbólico|`shutil.which(cmd, mode=os.F_OK \| os.X_OK, path=None)`|

##### Módulos sys

El módulo [sys](https://docs.python.org/3.4/library/sys.html#module-sys) es el encargado de proveer variables y funcionalidades, directamente relacionadas con el intérprete.

Algunas variables definidas en el módulo:

|Variable|Descripción|
|---|---|
|`sys.argv`|Retorna una lista con todos los argumentos pasados por línea de comandos. Al ejecutar `python modulo.py arg1 arg2`, retornará una lista: `['modulo.py', 'arg1', 'arg2']`|
|`sys.executable`|Retorna el path absoluto del binario ejecutable del intérprete de Python|
|`sys.platform`|Retorna la plataforma sobre la cuál se está ejecutando el intérprete|
|`sys.version`|Retorna el número de versión de Python con información adicional|

Y algunos métodos:

|Método|Descripción|
|---|---|
|`sys.exit()`|Forzar la salida del intérprete|
|`sys.getdefaultencoding()`|Retorna la codificación de caracteres por defecto|

##### Ejecución de scripts con argumentos

Podemos enviar información (argumentos) a un programa cuando se ejecuta como un script, por ejemplo:

```
#!/usr/bin/env python    
import sys
print("Has instroducido",len(sys.argv),"argumento")
suma=0
for i in range(1,len(sys.argv)):
    suma=suma+int(sys.argv[i])
print("La suma es ",suma)

$  python3 sumar.py 3 4 5
Has introducido 4 argumento
La suma es  12
```


### Módulos de operaciones matemáticas
##### Módulo Math
El módulo [math](https://docs.python.org/3.4/library/math.html) nos proporciones distintas funciones y operaciones matemáticas.

```
>>> import math
>>> math.factorial(5)
120
>>> math.pow(2,3)
8.0
>>> math.sqrt(7)
2.6457513110645907
>>> math.cos(1)
0.5403023058681398
>>> math.pi
3.141592653589793
>>> math.log(10)
2.302585092994046
```

##### Módulo fractions

El módulo [fractions](https://docs.python.org/3.4/library/fractions.html) nos permite trabajar con fracciones.

```
>>> from fractions import Fraction
>>> a=Fraction(2,3)
>>> b=Fraction(1.5)
>>> b
Fraction(3, 2)
>>> c=a+b
>>> c
Fraction(13, 6)
```

##### Módulo statistics

El módulo [statistics](https://docs.python.org/3.4/library/statistics.html) nos proporciona funciones para hacer operaciones estadísticas.

```
>>> import statistics
>>> statistics.mean([1,4,5,2,6])
3.6

>>> statistics.median([1,4,5,2,6])
4
```

##### Módulo random

El módulo [random](https://docs.python.org/3.4/library/random.html) nos permite generar datos pseudo-aleatorios.

```
>>> import random
>>> random.randint(10,100)
34

>>> random.choice(["hola","que","tal"])
'que'

>>> frutas=["manzanas","platanos","naranjas"]
>>> random.shuffle(frutas)
>>> frutas
['naranjas', 'manzanas', 'platanos']

>>> lista = [1,3,5,2,7,4,9]
>>> numeros=random.sample(lista,3)
>>> numeros
[1, 2, 4]
```

### MÓDULOS DE FECHA Y HORA
##### Módulo time

El tiempo es medido como un número real que representa los segundos transcurridos desde el 1 de enero de 1970. Por lo tanto es imposible representar fechas anteriores a esta y fechas a partir de 2038 (tamaño del float en la lubraría C (32 bits)).

```
>>> import time
>>> time.time()
1488619835.7858684
```

Para convertir la cantidad de segundos a la fecha y hora local:

```
>>> tiempo = time.time()
>>> time.localtime(tiempo)
time.struct_time(tm_year=2017, tm_mon=3, tm_mday=4, tm_hour=10, tm_min=37, tm_sec=19, tm_wday=5, tm_yday=63, tm_isdst=0)
```

Si queremos obtener la fecha y hora actual:

```
>>> time.localtime()
time.struct_time(tm_year=2017, tm_mon=3, tm_mday=4, tm_hour=10, tm_min=37, tm_sec=30, tm_wday=5, tm_yday=63, tm_isdst=0)
```

Nos devuelve a una estructura a la que podemos acceder a sus distintos campos.

```
>>> tiempo = time.localtime()
>>> tiempo.tm_year
2017
```

Podemos representar la fecha y hora como una cadena:

```
>>> time.asctime()
'Sat Mar  4 10:41:41 2017'
>>> time.asctime(tiempo)
'Sat Mar  4 10:39:21 2017'
```

O con un determinado formato:

```
>>> time.strftime('%d/%m/%Y %H:%M:%S')
'04/03/2017 10:44:52'
>>> time.strftime('%d/%m/%Y %H:%M:%S',tiempo)
'04/03/2017 10:39:21'
```


##### Módulo datetime

Los módulos datetime y calendar amplían las posibilidades del módulo time que provee funciones para manipular expresiones de tiempo.

```
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2017, 3, 4, 10, 52, 12, 859564)
>>> datetime.now().day,datetime.now().month,datetime.now().year
(4, 3, 2017)
```

Para comparar fechas y horas:

```
>>> from datetime import datetime, date, time, timedelta
>>> hora1 = time(10,5,0)
>>> hora2 = time(23,15,0)
>>> hora1>hora2
False

>>> fecha1=date.today()
>>> fecha2=fecha1+timedelta(days=2)
>>> fecha1
datetime.date(2017, 3, 4)
>>> fecha2
datetime.date(2017, 3, 6)
>>> fecha1<fecha2
True
```

Podemos imprimir aplicando un formato:

```
>>> fecha1.strftime("%d/%m/%Y")
'04/03/2017'
>>> hora1.strftime("%H:%M:%S")
'10:05:00'
```

Podemos convertir una cadena a un `datetime`:

```
>>> tiempo = datetime.strptime("12/10/2017","%d/%m/%Y")
```

Y podemos trabajar con cantidades (segundos, minutos, horas, días, semanas,…) con `timedelta`:

```
>>> hoy = date.today()
>>> ayer = hoy - timedelta(days=1)
>>> diferencia=hoy -ayer
>>> diferencia
datetime.timedelta(1)

>>> fecha1=datetime.now()
>>> fecha2=datetime(1995,10,12,12,23,33)
>>> diferencia=fecha1-fecha2
>>> diferencia
datetime.timedelta(7813, 81981, 333199)
```

##### Módulo calendar

Podemos obtener el calendario del mes actual:

```
>>> año = date.today().year 
>>> mes = date.today().month
>>> calendario_mes = calendar.month(año, mes)
>>> print(calendario_mes)
     March 2017
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31
```

Y para mostrar todos los meses del año:

```
>>> print(calendar.TextCalendar(calendar.MONDAY).formatyear(2017,2, 1, 1, 2))
```

### Instalar módulos externos

Python posse una activa comunidad de desarrolladores y usuarios que desarrollan toanto los módulos estándar de python, como módulos y paquetes desarolados por terceros.

##### PyPI y pip

- El _Python Package Index_ o _PyPI_, es el repositorio de paquetes de software oficial para aplicaciones de terceros en el lenguaje de programación Python.
    
- `pip`: Sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python que se encuentran alojados en el repositorio _PyPI_.
    

##### Instalación de módulos python

Para instalar un nuevo paquete python tengo varias alternativas:

1. Utilizar el que este empaquetado en la distribución que estés usando. Podemos tener problemas si necesitamos una versión determinada.
    
    ```
     # apt-cache show python3-requests
     ...
     Version: 2.4.3-6
     ...
    ```
    
2. Instalar pip en nuestro equipo, y como superusuario instalar el paquete python que nos interesa. Esta solución nos puede dar muchos problemas, ya que podemos romper las dependencias entre las versiones de nuestros paquetes python instalados en el sistema y algún paquete puede dejar de funcionar.
    
    ```
     # pip search requests
     ...
     requests (2.13.0)      - Python HTTP for Humans.
     ...
    ```
    
3. Utilizar entornos virtuales: es un mecanismo que me permite gestionar programas y paquetes python sin tener permisos de administración, es decir, cualquier usuario sin privilegios puede tener uno o más “espacios aislados” (ya veremos más adelante que los entornos virtuales se guardan en directorios) donde poder instalar distintas versiones de programas y paquetes python. Para crear los entornos virtuales vamos a usar el programa `virtualenv` o el módulo `venv`.
    

###### Creando entornos virtuales con `virtualenv`

Podemos utilizar este software para trabajar con cualquier distribución de python, pero evidentemente es obligatorio si estamos trabajando con python 2.x o python 3.x (una versión anterior a la 3.3).

```
# apt-get install python-virtualenv
```

Si queremos crear un entorno virtual con python3:

```
$ virtualenv -p /usr/bin/python3 entorno2
```

La opción `-p` nos permite indicar el interprete que se va a utilizar en el entorno.

Para activar nuestro entorno virtual:

```
$ source entorno2/bin/activate
(entorno2)$ 
```

Y para desactivarlo:

```
(entorno2)$ deactivate
$
```

###### Creando entornos virtuales con `venv`

A partir de la versión 3.3 de python podemos utilizar el módulo `venv` para crear el entorno virtual.

Instalamos el siguiente paquete para instalar el módulos:

```
# apt-get install python3-venv
```

Ahora ya como un usuario sin privilegio podemos crear un entorno virtual con python3:

```
$ python3 -m venv entorno3
```

La opción `-m` del interprete nos permite ejecutar un módulo como si fuera un programa.

Para activar y desactivar el entono virtual:

```
$ source entorno3/bin/activate
(entorno3)$ deactivate
$ 
```

###### Instalando paquetes en nuestro entorno virtual

Independientemente del sistema utilizado para crear nuestro entorno virtual, una vez que lo tenemos activado podemos instalar paquetes python en él utilizando la herramienta `pip` (que la tenemos instalada automáticamente en nuestro entorno). Partiendo de un entorno activado, podemos, por ejemplo, instalar la última versión de django:

```
(entorno3)$ pip install django
```

Si queremos ver los paquetes que tenemos instalados con sus dependencias:

```
(entorno3)$ pip list
Django (1.10.5)
pip (1.5.6)
setuptools (5.5.1)
```

Si necesitamos buscar un paquete podemos utilizar la siguiente opción:

```
(entorno3)$ pip search requests
```

Si a continuación necesitamos instalar una versión determinada del paquete, que no sea la última, podemos hacerlo de la siguiente manera:

```
(entorno3)$ pip install requests=="2.12"
```

Si necesitamos borrar un paquete podemos ejecutar:

```
(entorno3)$ pip uninstall requests
```

Y, por supuesto para instalar la última versión, simplemente:

```
(entorno3)$ pip install requests    
```

Para terminar de repasar la herramienta `pip`, vamos a explicar como podemos guardar en un fichero (que se suele llamar `requirements.txt`) la lista de paquetes instalados, que nos permite de manera sencilla crear otro entorno virtual en otra máquina con los mismos paquetes instalados. Para ello vamos a usar la siguiente opción de `pip`:

```
(entorno3)$ pip freeze
Django==1.10.5
requests==2.13.0
```

Y si queremos guardar esta información en un fichero que podamos distribuir:

```
(entorno3)$ pip freeze > requirements.txt
```

De tal manera que otro usuario, en otro entorno, teniendo este fichero pude reproducirlo e instalar los mismos paquetes de la siguiente manera:

```
(entorno4)$ pip install -r requirements.txt
```



