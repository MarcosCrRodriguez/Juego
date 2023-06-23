#--------------------clase_score_item--------------------#

import pygame
from configuraciones import reescalar_imagenes

class Score_Item:
    def __init__(self, tamaño, animaciones, posicion_inicial) -> None:
        #CONFECCION
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #ANIMACIONES
        self.contador_pasos = 0
        self.animaciones_item = animaciones
        self.reescalar_animaciones()
        #RECTANGULOS
        self.rectangulo = self.animaciones_item["moneda"][0].get_rect()
        self.rectangulo.x = posicion_inicial[0]
        self.rectangulo.y = posicion_inicial[1]
        #SONIDO
        self.sonido_colision = pygame.mixer.Sound("Sound_track\coin_sound.wav")
        self.sonido_colision.set_volume(0.6)

    def reescalar_animaciones(self)->None:
        for clave in self.animaciones_item:
            reescalar_imagenes(self.animaciones_item[clave], (self.ancho, self.alto))

    def animar_item(self, pantalla, que_animacion:str)->None:
        animacion = self.animaciones_item[que_animacion]
        largo = len(animacion)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        pantalla.blit(animacion[self.contador_pasos], self.rectangulo) 
        self.contador_pasos += 1 