#importaciones
import pygame
import time
#variables
inicio_coord = (1,0)
final_coord = (11,5)
muros_coord = [[0, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0], [0, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [10, 1], [11, 1], [0, 2], [2, 2], [4, 2], [10, 2], [11, 2], [0, 3], [2, 3], [4, 3], [6, 3], [7, 3], [9, 3], [10, 3], [11, 3], [0, 4], [4, 4], [6, 4], [11, 4], [0, 5], [1, 5], [2, 5], [6, 5], [8, 5], [9, 5], [4, 6], [6, 6], [8, 6], [11, 6], [0, 7], [1, 7], [3, 7], [4, 7], [6, 7], [8, 7], [9, 7], [10, 7], [11, 7], [0, 8], [1, 8], [3, 8], [4, 8], [6, 8], [10, 8], [11, 8], [0, 9], [3, 9], [4, 9], [6, 9], [7, 9], [8, 9], [10, 9], [11, 9], [0, 10], [1, 10], [7, 10], [8, 10], [10, 10], [11, 10], [0, 11], [1, 11], [2, 11], [3, 11], [4, 11], [5, 11], [6, 11], [7, 11], [8, 11], [9, 11], [10, 11], [11, 11]]
pos_final = [final_coord[0],final_coord[1]]
tamaño = [12,12]

tamaño_ventana = (500,500)
anchura = tamaño_ventana[0]/tamaño[0]
altura = tamaño_ventana[1]/tamaño[1]

ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
MORADO = (123, 2, 142)


#crear muros
def crear_muros(muros_coord,tamaño): #nomenclatura variables
    muros = []
    for x,y in muros_coord:
        muros.append([x,y])
    for ns in range(0, tamaño[1]):
        muroN = [-1, ns]
        muroS = [tamaño[0], ns]
        muros.append(muroN)
        muros.append(muroS)
    for eo in range(0, tamaño[0]):
        muroE = [eo, -1]
        muroO = [eo, tamaño[1]]
        muros.append(muroE)
        muros.append(muroO)
    return(muros)


#elegir direccion
def elegir_direccion(pos_actual,muros,camino):
    direccion = ""
    muro_n = [pos_actual[0], pos_actual[1]-1]
    muro_s = [pos_actual[0], pos_actual[1]+1]
    muro_e = [pos_actual[0]+1, pos_actual[1]]
    muro_o = [pos_actual[0]-1, pos_actual[1]]
    camino.append(pos_actual)
    
    if muro_n not in muros and muro_n not in camino:
        direccion = "norte"
    elif muro_e not in muros and muro_e not in camino:
        direccion = "este"
    elif muro_s not in muros and muro_s not in camino:
        direccion = "sur"
    elif muro_o not in muros and muro_o not in camino:
        direccion = "oeste"
    else:
        direccion = "block"
        
    return(direccion)


#muro a pygame
def muro_pygame(coord,anchura,altura):
    wpygame = []
    for x,y in coord:
        newx = x*anchura
        newy = y*altura
        muro = [newx,newy]
        wpygame.append(muro)
    return(wpygame)
#main
muros = crear_muros(muros_coord,tamaño)
bucle1 = True
bucle2 = True
while bucle1:
    bucle2 = True
    camino = []
    pos_actual = [inicio_coord[0],inicio_coord[1]]
    while bucle2:
        direccion = elegir_direccion(pos_actual,muros,camino)
        if direccion == "norte":
            pos_actual = [pos_actual[0], pos_actual[1]-1]
        if direccion == "este":
            pos_actual = [pos_actual[0]+1, pos_actual[1]]
        if direccion == "oeste":
            pos_actual = [pos_actual[0]-1, pos_actual[1]]
        if direccion == "sur":
            pos_actual = [pos_actual[0], pos_actual[1]+1]
        if direccion == "block":
            muros.append(pos_actual)
            bucle2 = False
        if pos_actual == pos_final:
            camino.append(pos_actual)
            bucle1 = False
            bucle2 = False
print(camino)

murospygame = muro_pygame(muros_coord,anchura,altura)
caminopygame= muro_pygame(camino,anchura,altura)

ventana = False
pygame.init()
vtn = pygame.display.set_mode(tamaño_ventana)
while not ventana:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ventana = True
    for x,y in murospygame:
        pygame.draw.rect(vtn, VERDE,[x,y,anchura,altura])
    for x,y in caminopygame:
        pygame.draw.rect(vtn, MORADO,[x,y,anchura,altura])
    pygame.draw.rect(vtn, ROJO, [int(inicio_coord[0]*anchura),int(inicio_coord[1]*altura),anchura,altura])
    pygame.draw.rect(vtn, AZUL, [int(final_coord[0]*anchura),int(final_coord[1]*altura),anchura,altura])
    pygame.display.flip()