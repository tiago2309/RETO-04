# Ejercicio 2: Verificar si el código ASCII de la primera letra de una cadena de longitud 1 es par o impar

cadena = input("Ingrese una cadena de longitud 1: ")

if len(cadena) != 1:
    print("Error: debe ingresar exactamente un solo carácter.")
else:
    codigo_ascii = ord(cadena[0])
    if codigo_ascii % 2 == 0:
        print(f"El código ASCII de '{cadena}' es {codigo_ascii} y es PAR.")
    else:
        print(f"El código ASCII de '{cadena}' es {codigo_ascii} y es IMPAR.")