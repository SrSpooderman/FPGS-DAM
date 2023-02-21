año = int(input())

if año%4 == 0:
    #es multiple de 4 por lo tanto puede ser bisiesto
    if año%100 == 0:
        if año%400 == 0:
            print("El año es bisiesto")
        else:
            print("El año no es bisiesto")
    else:
        print("El año es bisiesto")
else:
    print("No es año bisiesto")