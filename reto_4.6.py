# Ejercicio 6: Verificar si un punto está dentro de un círculo

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
