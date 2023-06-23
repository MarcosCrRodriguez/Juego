#--------------------clase_proyectil--------------------#

import pygame
from configuraciones import reescalar_imagenes, obtener_rectangulos, destroy_objetct
from class_plataforma import *

class Proyectil:
    def __init__(self, tamaño, animaciones, posicion_actual, velocidad) -> None:
        #CONFECCION
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #ANIMACIONES
        self.contador_pasos = 0
        self.animaciones_proyectil = animaciones
        self.reescalar_animaciones()
        #RECTANGULOS
        self.rectangulo = self.animaciones_proyectil["proyectil_pj_derecha"][0].get_rect()
        self.rectangulo.x = posicion_actual[0]
        self.rectangulo.y = posicion_actual[1]
        self.lados_proyectil = obtener_rectangulos(self.rectangulo)
        #SONIDO
        self.sonido_colision = pygame.mixer.Sound("Recursos\\Proyerctil_pj\\Colision_proyectil\\Sound Effect.wav")
        self.sonido_colision.set_volume(0.4)

        self.velocidad = velocidad

    def reescalar_animaciones(self)->None:
        for clave in self.animaciones_proyectil:
            reescalar_imagenes(self.animaciones_proyectil[clave], (self.ancho, self.alto))        

    def lanzar_proyectil(self, velocidad)->None:
        for lado in self.lados_proyectil:
            self.lados_proyectil[lado].x += velocidad

    def animar_proyectil(self, pantalla, que_animacion:str)->None:
        animacion = self.animaciones_proyectil[que_animacion]
        largo = len(animacion)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        pantalla.blit(animacion[self.contador_pasos], self.lados_proyectil["main"]) 
        self.contador_pasos += 1 

    def colision_proyectil(self, lista_plataformas):
        for lado in lista_plataformas:
            if self.lados_proyectil["main"].colliderect(lado.lados_plataforma["main"]):
                self.sonido_colision.play()
                destroy_objetct(self) 