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

