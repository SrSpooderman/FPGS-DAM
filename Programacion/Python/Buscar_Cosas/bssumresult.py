#Buscar en un array una suma de numeros que de un valor y luego printar
valor = 14
l = [2,3,4,5,6,7,9,10,11,12]

for pos1 in range(0, len(l)):
    for pos2 in range(0,len(l)):
        if pos1 == pos2:
            pass
        else:
            if l[pos1]+l[pos2] == valor:
                print(l[pos1],"sumado con ",l[pos2]," es igual a", valor)
            else:
                pass