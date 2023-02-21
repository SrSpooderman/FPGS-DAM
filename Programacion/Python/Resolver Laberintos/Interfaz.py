#importaciones
import pygame
#posiciones
inicio_coord = (0,3)
final_coord = (2,0)
muros_coord = [(1,0),(1,2),(2,2)]

area = 5
tamaño_ventana = (500,600)
pixel_size = tamaño_ventana[1]/area

inicio_pos = [int(inicio_coord[0]*pixel_size),int(inicio_coord[1]*pixel_size)]
final_pos = [int(final_coord[0]*pixel_size),int(final_coord[1]*pixel_size)]
muros_pos = []
for x,y in muros_coord:
    newx = x*pixel_size
    newy = y*pixel_size
    muro = [newx,newy]
    muros_pos.append(muro)
#colores
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)


bucle = False
#main
pygame.init()
vtn = pygame.display.set_mode(tamaño_ventana)
while not bucle:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bucle = True
    for x,y in muros_pos:
        pygame.draw.rect(vtn, VERDE,[x,y,pixel_size,pixel_size])
    pygame.draw.rect(vtn, ROJO, [inicio_pos[0],inicio_pos[1],pixel_size,pixel_size])
    pygame.draw.rect(vtn, AZUL, [final_pos[0],final_pos[1],pixel_size,pixel_size])
    
    pygame.display.flip()