#No identifica muros
#Es completamente ampliable uwu

inicio_coord = (2,2) 
final_coord = (6,3)
muros_coord = [(1,0),(1,2),(2,2)]
pos_actual = [inicio_coord[0],inicio_coord[1]]
pos_final = [final_coord[0],final_coord[1]]
camino = []
direccion_ant = ""
direccion = ""
camino.append(pos_actual)
while pos_actual != pos_final:
    diferencia_x = final_coord[0]-pos_actual[0]
    diferencia_y = final_coord[1]-pos_actual[1]
    if (abs(diferencia_x) < abs(diferencia_y)):
        if diferencia_x < 0:
            direccion = "O"
        elif diferencia_x > 0:
            direccion = "E"
    elif (abs(diferencia_x) > abs(diferencia_y)):
        if diferencia_y < 0:
            direccion = "N"
        elif diferencia_y > 0:
            direccion = "S"
    if diferencia_y == 0:
        if diferencia_x < 0:
            direccion = "O"
        elif diferencia_x > 0:
            direccion = "E"
    elif diferencia_x == 0:
        if diferencia_y < 0:
            direccion = "N"
        elif diferencia_y > 0:
            direccion = "S"
    #elegir direccion
    if direccion == "N":
        pos_actual = [pos_actual[0],pos_actual[1]-1]
    elif direccion == "S":
        pos_actual = [pos_actual[0],pos_actual[1]+1]
    elif direccion == "E":
        pos_actual = [pos_actual[0]+1,pos_actual[1]]
    elif direccion == "O":
        pos_actual = [pos_actual[0]-1,pos_actual[1]]
    direccion_ant = direccion
    camino.append(pos_actual)
print(camino)