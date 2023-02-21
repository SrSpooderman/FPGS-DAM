#Dentro de un string buscar una letra especifica y mostrar la cantidad de letras
coso = str(input("palabra: "))
lea = str(input("letra a buscar: "))
contador = 0
for letra in coso:
    if letra == lea:
        contador += 1
    else:
        pass
print("Hay ",contador," ",lea)