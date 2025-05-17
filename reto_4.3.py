# Ejercicio 3: Determinar si un carácter es un dígito

caracter = input("Ingrese un carácter: ")

if len(caracter) != 1:
    print("Error: debe ingresar solo un carácter.")
elif caracter.isdigit():
    print(f"El carácter '{caracter}' es un dígito.")
else:
    print(f"El carácter '{caracter}' NO es un dígito.")
