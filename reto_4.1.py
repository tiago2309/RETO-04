# Ejercicio 1: Verificar si un número corresponde al código ASCII de una vocal minúscula

n = int(input("Ingrese un número entero: "))

# Vocales minúsculas y sus códigos ASCII: a=97, e=101, i=105, o=111, u=117
if n in [97, 101, 105, 111, 117]:
    print(f"El número {n} corresponde al código ASCII de una vocal minúscula.")
else:
    print(f"El número {n} NO corresponde al código ASCII de una vocal minúscula.")
