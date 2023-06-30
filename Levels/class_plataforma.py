#--------------------clase_plataforma--------------------#

import pygame
from Levels.configuraciones import obtener_rectangulos
from Levels.class_objeto import *

class Plataforma (Objeto):
    def __init__(self, tamaño:tuple, posicion_inicial_plataforma:tuple, path_imagen:str) -> None:

        super().__init__(tamaño)
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

    def draw(self, pantalla)->None:
        pantalla.blit(self.plataforma, self.lados_plataforma["main"])
