#--------------------main--------------------#

import pygame
import sys

from GUI.mi_formulario import *

W,H = 1900,1000
FPS = 28
TAMAÑO_PANTALLA = (W,H)

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((TAMAÑO_PANTALLA))

pygame.display.set_caption("Fight_Club")
icono = pygame.image.load("Recursos/icon.png")
pygame.display.set_icon(icono)

fondo = pygame.image.load("GUI/background_menu.png")
fondo = pygame.transform.scale(fondo,(TAMAÑO_PANTALLA))

form_prueba = Form_Prueba(PANTALLA, 200, 100, 1000, 600, "gold", "Gray", 5, True)

running = True

while running:
    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            running = False

    PANTALLA.blit(fondo, (0,0))
    form_prueba.update(eventos) 

    pygame.display.flip()

pygame.quit()
sys.exit()    
