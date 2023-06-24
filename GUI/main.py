import pygame
import sys
from pygame.locals import *
from GUI.mi_formulario import *

pygame.init()
WIDHT = 1200
HEIGT = 600
FPS = 60

reloj = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((WIDHT,HEIGT))

form_principal = Form_Prueba(PANTALLA, 200, 100, 900, 350, "gold", "Magenta", 5, True)

while True:
    reloj.tick(FPS)
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)

    PANTALLA.fill("Black")

    form_principal.update(eventos)

    pygame.display.flip()