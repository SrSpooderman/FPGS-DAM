uno = int(input())
dos = int(input())
tres = int(input())    
array = uno, dos, tres

if uno == dos == tres:
    print("Los tres son iguales")
elif uno != dos != tres != uno:
    print("Los tres son diferentes")
else:
    print("Has repetido dos numeros")
    #Mejora para saber que numeros se repiten
    """if uno == dos:
        print("El primero es igual al segundo")
    elif dos == tres:
        print("El segundo es igual al tercero")
    elif uno == tres:
        print("El primero es igual al tercero")"""