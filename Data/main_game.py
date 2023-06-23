#--------------------main--------------------#

import pygame
import sys

from nivel_uno import Nivel_Uno

W,H = 1900,1000
FPS = 25
TAMAÑO_PANTALLA = (W,H)

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((TAMAÑO_PANTALLA))

nivel_actual = Nivel_Uno(PANTALLA)

running = True

while running:
    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            running = False

    finish = nivel_actual.update(eventos) 

    if finish == False:
        break   

    pygame.display.update()

pygame.quit()
sys.exit()
