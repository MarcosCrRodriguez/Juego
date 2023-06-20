#--------------------clase_plataforma--------------------#

import pygame
from configuraciones import obtener_rectangulos

class Plataforma:
    def __init__(self, tamaño, posicion_inicial_plataforma, path_imagen) -> None:
        #CONFECCION
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #RECTANGULOS
        self.plataforma = pygame.image.load(path_imagen)
        self.plataforma = pygame.transform.scale(self.plataforma, tamaño)
        rectangulo_plataforma = self.plataforma.get_rect()
        rectangulo_plataforma.x = posicion_inicial_plataforma[0]
        rectangulo_plataforma.y = posicion_inicial_plataforma[1]
        self.lados_plataforma = obtener_rectangulos(rectangulo_plataforma)

    def dibujar(self, pantalla)->None:
        pantalla.blit(self.plataforma, self.lados_plataforma["main"])
