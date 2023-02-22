# Checkear si 2 números de la lista sumados son igual a 'valor'
import random
from datetime import datetime

time_start = datetime.now()
valor = random.randint(0, 80000)
lista = []
diccionario = {}
resultados = []

for i in range(0, 10000):
    n = random.randint(0, 50000)
    lista.append(n)
    diccionario[n] = True
# Hacer una pasada para cada numero de la lista, sumándolo a cada número de la lista
num_results = 0
for i in range(0, len(lista)):
    complemento = valor - lista[i]
    if complemento in diccionario:
        resultados.append([lista[i], complemento])
    num_results += 1

time_stop = datetime.now()
elapse_1 = time_stop - time_start
#Printar valores para el tiempo y las sumas junto los resultados
print("Valor buscado:", valor)
print("\nLa suma de estos numeros dan", valor, "\n\n", resultados)
print(time_start)
print(time_stop)
print(elapse_1)