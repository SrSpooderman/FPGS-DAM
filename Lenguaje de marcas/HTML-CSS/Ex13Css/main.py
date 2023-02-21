import os
import random

nombres = ["Pepe", "Jaime", "Felipe", "Roberto", "Ernesto"]
puntuacion = [5,8,1,2,9]
color = ""
orden = ""
archivo = open("index.html","w")
estilo = open("index.css","w")
while True:
    color = str(input("Que color? Azul o Rojo: "))
    if color in ["Azul","azul","Rojo","rojo"]:
        break
    else:
        print("Color fuera de los valores")
while True:
    orden = str(input("Que tipo de orden ascendente o descendente?: "))
    if orden in ["Ascendente", "Descendente","ascendente","descendente","a","d"]:
        break
    else:
        print("Orden fuera de los valores")
#ordenar array
intercambio = True
if orden in ["Ascendente","ascendente","a"]:
    while intercambio:
        intercambio = False
        for i in range(len(puntuacion)-1):
            if puntuacion[i] > puntuacion[i + 1]:
                puntuacion[i], puntuacion[i + 1] = puntuacion[i + 1], puntuacion[i]
                nombres[i], nombres[i + 1] = nombres[i + 1], nombres[i]
                intercambio = True
elif orden in ["Descendente","descendente","d"]:
    while intercambio:
        intercambio = False
        for i in range(len(puntuacion)-1):
            if puntuacion[i] < puntuacion[i + 1]:
                puntuacion[i], puntuacion[i + 1] = puntuacion[i + 1], puntuacion[i]
                nombres[i], nombres[i + 1] = nombres[i + 1], nombres[i]
                intercambio = True
#hacer el html
archivo.write("<!DOCTYPE html>"+os.linesep)
archivo.write('<link rel="stylesheet" type="text/css" href="index.css">'+os.linesep)
archivo.write("<body>"+os.linesep+"<table>"+os.linesep)
#crear teblas nombre
archivo.write("<tr>"+os.linesep)
for nombre in nombres:
    archivo.write("<td>"+nombre+"</td>"+os.linesep)
archivo.write("</tr>"+os.linesep)
#crear tablas puntuacion
archivo.write("<tr>"+os.linesep)
for puntos in puntuacion:
    archivo.write("<td>"+str(puntos)+"</td>"+os.linesep)
archivo.write("</tr>"+os.linesep)

archivo.write("<table>"+os.linesep+"</body>"+os.linesep+"</html>")

#crear css
estilo.write("table{"+"border:1px solid black; border-collapse: collapse;}"+os.linesep+"td{border: 1px solid black;"+"}"+os.linesep)
num = str(random.randint(50,255))
num2 = str(random.randint(50,255))
if color in ["Rojo","rojo"]:
    estilo.write("td:nth-child(odd){"+"color: rgb("+num+"27,27);}")
    estilo.write("td:nth-child(even){"+"color: rgb("+num2+"27,27);}")
elif color in ["Azul","azul"]:
    estilo.write("td:nth-child(odd){"+"color: rgb(27,27,"+num+");}")
    estilo.write("td:nth-child(even){"+"color: rgb(27,27,"+num2+");}")