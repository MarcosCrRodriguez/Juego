#--------------------main--------------------#

import pygame
import sys

from nivel_uno import Nivel_Uno
from nivel_dos import Nivel_Dos
# from GUI.mi_formulario import *

W,H = 1900,1000
FPS = 25
TAMAÑO_PANTALLA = (W,H)

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((TAMAÑO_PANTALLA))

nivel_actual = Nivel_Dos(PANTALLA)
# form_prueba = Form_Prueba(PANTALLA, 200, 100, 900, 350, "gold", "Magenta", 5, True)

running = True

while running:
    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            running = False

    # form_prueba.update(eventos)
    finish = nivel_actual.update(eventos) 

    if finish == False:
        break   

    pygame.display.update()

pygame.quit()
sys.exit()
