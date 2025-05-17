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
