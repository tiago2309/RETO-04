# Ejercicio 4: Verificar si el primer número real es múltiplo del segundo

a = float(input("Ingrese el primer número real: "))
b = float(input("Ingrese el segundo número real: "))

if b == 0:
    print("No se puede dividir por cero.")
elif a % b == 0:
    print(f"{a} es múltiplo de {b}.")
else:
    print(f"{a} NO es múltiplo de {b}.")
