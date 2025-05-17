# RETO-04
## Código ASCII de una vocal minúscula
### 1. Dado un número entero, determinar si ese número corresponde al código ASCII de una vocal minúscula.

Primero se pide al usuario un número entero. Luego, se usa chr() para convertir ese número a su carácter ASCII y se verifica si ese carácter está en la lista de vocales minúsculas (['a', 'e', 'i', 'o', 'u']). Si sí, se imprime el mensaje correspondiente.

```
n = int(input("Ingrese un número entero: "))

# Vocales minúsculas y sus códigos ASCII: a=97, e=101, i=105, o=111, u=117
if n in [97, 101, 105, 111, 117]:
    print(f"El número {n} corresponde al código ASCII de una vocal minúscula.")
else:
    print(f"El número {n} NO corresponde al código ASCII de una vocal minúscula.")
```

## Código ASCII par o impar
### 2. Dada una cadena de longitud 1, determine si el código ASCII de primera letra de la cadena es par o no.
Se pide una cadena de longitud 1. Luego, usando ord(), se obtiene el código ASCII del primer carácter. Usando el operador módulo (%), se verifica si es par (% 2 == 0) o impar (% 2 != 0) y se muestra el resultado.

```
cadena = input("Ingrese una cadena de longitud 1: ")

if len(cadena) != 1:
    print("Error: debe ingresar exactamente un solo carácter.")
else:
    codigo_ascii = ord(cadena[0])
    if codigo_ascii % 2 == 0:
        print(f"El código ASCII de '{cadena}' es {codigo_ascii} y es PAR.")
    else:
        print(f"El código ASCII de '{cadena}' es {codigo_ascii} y es IMPAR.")
```

## ¿Es un dígito?
### 3. Dado un carácter, construya un programa en Python para determinar si el carácter es un dígito o no.
Se pide un carácter y se verifica si el usuario ingresó exactamente uno. Luego se utiliza el método .isdigit() que devuelve True si el carácter es un dígito entre 0 y 9, y se imprime el mensaje correspondiente.

```
caracter = input("Ingrese un carácter: ")

if len(caracter) != 1:
    print("Error: debe ingresar solo un carácter.")
elif caracter.isdigit():
    print(f"El carácter '{caracter}' es un dígito.")
else:
    print(f"El carácter '{caracter}' NO es un dígito.")
```

## Múltiplo entre reales
### 4. Realice un programa que lea dos números reales y determine si el primero es múltiplo del segundo.
Se piden dos números reales. Primero se verifica que el segundo no sea cero para evitar división por cero. Luego se usa el operador módulo (%) para comprobar si el primer número es divisible por el segundo sin residuo (i.e. múltiplo).

```
a = float(input("Ingrese el primer número real: "))
b = float(input("Ingrese el segundo número real: "))

if b == 0:
    print("No se puede dividir por cero.")
elif a % b == 0:
    print(f"{a} es múltiplo de {b}.")
else:
    print(f"{a} NO es múltiplo de {b}.")
```

## Signo de un número real
### 5. Dado un número real x, construya un programa que permita determinar si el número es positivo, negativo o cero. Para cada caso de debe imprimir el texto que se especifica a continuación:

Positivo: "El número x es positivo"
Negativo: "El número x es negativo"
Cero (0): "El número x es el neutro para la suma"

Se ingresa un número real. El programa usa una estructura if-elif-else para determinar si es mayor que cero (positivo), menor (negativo) o igual a cero (neutro para la suma). Imprime el mensaje correspondiente.

```
x = float(input("Ingrese un número real: "))

if x > 0:
    print(f"El número {x} es positivo")
elif x < 0:
    print(f"El número {x} es negativo")
else:
    print(f"El número {x} es el neutro para la suma")
```

## Punto dentro de un círculo
### 6. Dado el centro y el radio de un círculo, determinar si un punto de R2 pertenece o no al interior del círculo.
Se piden las coordenadas del centro y el radio del círculo, y luego las coordenadas del punto. Usando la fórmula de distancia euclidiana al cuadrado, se compara la distancia al cuadrado del punto al centro con el radio al cuadrado. Según el resultado, se determina si el punto está dentro, fuera o sobre el círculo.

```
# Coordenadas del centro del círculo
x_centro = float(input("Ingrese la coordenada x del centro del círculo: "))
y_centro = float(input("Ingrese la coordenada y del centro del círculo: "))
radio = float(input("Ingrese el radio del círculo: "))

# Coordenadas del punto a evaluar
x_punto = float(input("Ingrese la coordenada x del punto: "))
y_punto = float(input("Ingrese la coordenada y del punto: "))

# Distancia del punto al centro
distancia_cuadrada = (x_punto - x_centro)**2 + (y_punto - y_centro)**2

if distancia_cuadrada < radio**2:
    print("El punto está dentro del círculo.")
elif distancia_cuadrada == radio**2:
    print("El punto está sobre el borde del círculo.")
else:
    print("El punto está fuera del círculo.")
```

## ¿Se puede formar un triángulo?
### 7. Dadas tres longitudes positivas, determinar si con esas longitudes se puede construir un triángulo.
Se piden tres longitudes positivas. Primero se valida que sean mayores que cero. Luego, se aplica la desigualdad triangular: la suma de cualquier par de lados debe ser mayor que el tercer lado. Si todas se cumplen, puede formarse un triángulo.

```
a = float(input("Ingrese la longitud del lado a: "))
b = float(input("Ingrese la longitud del lado b: "))
c = float(input("Ingrese la longitud del lado c: "))

if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        print("Las longitudes pueden formar un triángulo.")
    else:
        print("Las longitudes NO pueden formar un triángulo.")
else:
    print("Todas las longitudes deben ser positivas.")
```

## Capital según país (América)
### 8. Escriba un programa que reciba el nombre en minúsculas de un país de America y retorne la ciudad capital, si el país no pertenece al continente debe arrojar país no identificado (Utilice match-case).
Se pide el nombre de un país en minúsculas. Usando la estructura match-case (disponible desde Python 3.10), se comparan los valores contra una lista de países. Si hay coincidencia, se imprime la capital. Si no hay coincidencia, se imprime "país no identificado".

```
pais = input("Ingrese el nombre de un país de América en minúsculas: ")

match pais:
    case "colombia":
        print("La capital es Bogotá")
    case "mexico":
        print("La capital es Ciudad de México")
    case "argentina":
        print("La capital es Buenos Aires")
    case "brasil":
        print("La capital es Brasilia")
    case "chile":
        print("La capital es Santiago")
    case "peru":
        print("La capital es Lima")
    case "ecuador":
        print("La capital es Quito")
    case "venezuela":
        print("La capital es Caracas")
    case "uruguay":
        print("La capital es Montevideo")
    case "paraguay":
        print("La capital es Asunción")
    case "bolivia":
        print("La capital es Sucre")
    case "costa rica":
        print("La capital es San José")
    case "panama":
        print("La capital es Ciudad de Panamá")
    case "guatemala":
        print("La capital es Ciudad de Guatemala")
    case _:
        print("país no identificado")
```

Y listo!! De esa manera logramos realizar los 8 retos y adicional esta el archivo de los retos en VS Code.
