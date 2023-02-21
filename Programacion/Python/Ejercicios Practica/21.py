print("Calculo de areas")
figura = input("De que figura quieres calcular el area: ")
if figura == "triangulo":
    print("Has elegido triangulo, necesito unos datos")
    base = int(input("Dime la base: "))
    altura = int(input("Dime la altura: "))
    print("El area del triangulo es ", ((base*altura)/2))
elif figura == "circulo":
    print("Has elegido circulo, necesito unos datos")
    radio = int(input("Dime el radio: "))
    print("El area del circulo es ", 3.14*(radio**2))
else:
    print("Tu elección no se encuentra en nuestros parametros")