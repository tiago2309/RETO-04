# Ejercicio 5: Determinar si un número real es positivo, negativo o cero

x = float(input("Ingrese un número real: "))

if x > 0:
    print(f"El número {x} es positivo")
elif x < 0:
    print(f"El número {x} es negativo")
else:
    print(f"El número {x} es el neutro para la suma")
