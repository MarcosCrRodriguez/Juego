#--------------------clase_enemigo--------------------#

import pygame
from configuraciones import reescalar_imagenes, obtener_rectangulos
from class_plataforma import *

class Enemigo:
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad_enemigo) -> None:
        #CONFECCION
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #ANIMACIONES
        self.contador_pasos_enemigo = 0
        self.comportamiento = "e_izquierda"
        self.animaciones_enemigo = animaciones
        self.reescalar_animaciones()
        #RECTANGULOS
        rectangulo = self.animaciones_enemigo["enemigo_izquierda"][0].get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados_enemigo = obtener_rectangulos(rectangulo)
        #ACCION_ENEMIGO
        self.velocidad_enemigo = velocidad_enemigo
        
    def reescalar_animaciones(self)->None:
        for clave in self.animaciones_enemigo:
            reescalar_imagenes(self.animaciones_enemigo[clave], (self.ancho, self.alto))

    def animar_enemigo(self, pantalla, que_animacion:str)->None:
        animacion = self.animaciones_enemigo[que_animacion]
        largo = len(animacion)

        if self.contador_pasos_enemigo >= largo:
            self.contador_pasos_enemigo = 0

        pantalla.blit(animacion[self.contador_pasos_enemigo], self.lados_enemigo["main"]) 
        self.contador_pasos_enemigo += 2 

    def realizar_comportamiento(self, velocidad_enemigo)->None:
        for lado in self.lados_enemigo:
            self.lados_enemigo[lado].x += velocidad_enemigo

    # def aplicar_graverdad(self, piso)->None:
    #     if self.lados_enemigo["bottom"].colliderect(piso["top"]):
    #         self.desplazamiento_y = 0
    #         self.esta_saltando = False
    #         self.lados_enemigo["main"].bottom = piso["main"].top

    def update(self, pantalla)->None:
        match self.comportamiento:
            case "e_izquierda":
                self.animar_enemigo(pantalla, "enemigo_izquierda")
                self.realizar_comportamiento(self.velocidad_enemigo* -1)
            case "e_derecha":
                self.animar_enemigo(pantalla, "enemigo_derecha")
                self.realizar_comportamiento(self.velocidad_enemigo)

        # self.aplicar_graverdad(piso)

    def colision_plataforma(self, plataforma_izquierda:Plataforma, plataforma_derecha:Plataforma, primer_clave:str, segunda_clave:str)->None:
        if self.lados_enemigo["left"].colliderect(plataforma_izquierda.lados_plataforma[primer_clave]):
            self.comportamiento = "e_derecha"
        elif self.lados_enemigo["right"].colliderect(plataforma_derecha.lados_plataforma[segunda_clave]):
            self.comportamiento = "e_izquierda"

