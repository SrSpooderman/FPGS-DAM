#Buscar una secuencia de dos letras dentro de un texto con posiciones
coso = str(input("palabra: "))
lea = str(input("letra a buscar: "))
contador = 0
for pos in range(0,len(coso)):
    print("pos",pos)
    if coso[pos] == lea[0]:
        if coso[pos+1] == lea[1]:
            contador += 1
            print("cont",contador)
        else:
            pass
    else:
        pass
print("Hay ",contador," ",lea)