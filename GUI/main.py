import pygame
import sys
from pygame.locals import *
from mi_formulario import *

pygame.init()
WIDHT = 1200
HEIGT = 600
FPS = 60

reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode((WIDHT,HEIGT))

form_prueba = Form_Prueba(pantalla, 200, 100, 900, 350, "gold", "Magenta", 5, True)

while True:
    reloj.tick(FPS)
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill("Black")

    form_prueba.update(eventos)

    pygame.display.flip()