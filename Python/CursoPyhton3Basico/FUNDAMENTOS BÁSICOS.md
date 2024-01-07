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