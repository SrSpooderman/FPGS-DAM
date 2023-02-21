#Buscar una secuencia de 3 letras dentro de un texto mediante iguales
text="hoolaa. me gustan las olasssss. Hhooooola como estas"
contador = 0
letra_anterior = "*"
lentra_anteanterior="*"
for letra_actual in text:
    if letra_actual == "a" and letra_anterior=="l" and lentra_anteanterior == "o":
        contador+=1
    lentra_anteanterior = letra_anterior
    letra_anterior= letra_actual
print("contador ", contador)