#Importaciones
import random
import datetime
min_time = datetime.timedelta(
    hours=8,
    minutes=2,
    seconds=2
)
#Main
print("Dime la cantidad de numeros que quieres en tu array")
len_array = int(input())
print("Dime la cantidad de veces que quieres testear")
cant_rep = int(input())
array_origin = []
for item in range (0, len_array):
    array_origin.append(random.randint(0, 10000))
"""print(array_origin)
print("---")"""
#Procesos diversos
#Burbuja
def burbuja(array):
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(array)-1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                intercambio = True
    return array
#Seleccion
def seleccion(array):
    for pasada in range (len(array)):
        min = array[len(array)-1]
        min_pos = ""
        for num in range(pasada,len(array)):
            if array[num] < min:
                min = array[num]
                min_pos = num
            elif array[num] > min:
                pass
            elif array[num] == min:
                min = array[num]
                min_pos = num
        aux = array[pasada]
        array[pasada] = min
        array[min_pos] = aux
    return array
#Inserción
def insercion(array):
    for pasada in range(len(array)):
        min = array[len(array)-1]
        min_pos = ""
        for num in range (pasada, len(array)):
            if array[num] < min:
                min = array[num]
                min_pos = num
            elif array[num] > min:
                pass
            elif array[num] == min:
                min = array[num]
                min_pos = num
        array.pop(min_pos)
        array.insert(pasada,min)
    return array
#Final
for rep in range(0,cant_rep):
    time_start = datetime.datetime.now() #Inicio del contador
    a = burbuja(array_origin)
    time_stop = datetime.datetime.now() #Final del contador
    elapse_1 = time_stop - time_start
    if elapse_1.total_seconds() < min_time.total_seconds():
        min_time = elapse_1
for rep in range(0,cant_rep):
    time_start = datetime.datetime.now() #Inicio del contador
    b = seleccion(array_origin)
    time_stop = datetime.datetime.now() #Final del contador
    elapse_2 = time_stop - time_start
    if elapse_2.total_seconds() < min_time.total_seconds():
        min_time = elapse_2
for rep in range(0,cant_rep):
    time_start = datetime.datetime.now() #Inicio del contador
    c = insercion(array_origin)
    time_stop = datetime.datetime.now() #Final del contador
    elapse_3 = time_stop - time_start
    if elapse_3.total_seconds() < min_time.total_seconds():
        min_time = elapse_3
print(a)
print(elapse_1,"Burbuja Array:")
print(elapse_2,"Selección Array:")
print(elapse_3,"Inserción Array:")