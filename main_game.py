#--------------------main--------------------#

import pygame
import sys

from GUI.mi_formulario import *
from GUI.GUI_button_image import *
from GUI.GUI_label import *

W,H = 1900,1000
FPS = 28
TAMAÑO_PANTALLA = (W,H)

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((TAMAÑO_PANTALLA))

game_pause = False

fondo = pygame.image.load("GUI\\background_menu.png")
fondo = pygame.transform.scale(fondo,(TAMAÑO_PANTALLA))

form_prueba = Form_Prueba(PANTALLA, 200, 100, 900, 350, "gold", "Gray", 5, True)

# pause_menu = pygame.image.load("GUI\\Window.png")

running = True

while running:
    RELOJ.tick(FPS)
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            running = False
        # if evento.type == KEYDOWN:
        #     if evento.key == pygame.K_p:
        #         game_pause = True
        # llamar otro formulario

    PANTALLA.blit(fondo, (0,0))
    form_prueba.update(eventos)

    form_prueba.comprobar_nivel_completado() 

    pygame.display.flip()

pygame.quit()
sys.exit()

    
