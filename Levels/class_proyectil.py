#--------------------clase_proyectil--------------------#

import pygame
from Levels.configuraciones import reescalar_imagenes, obtener_rectangulos
from Levels.class_plataforma import *
from Levels.class_enemigo import *
from Levels.class_objeto import *
# import os

class Proyectil (Objeto):
    def __init__(self, tamaño:tuple, animaciones:dict, posicion_actual:tuple, velocidad:int, clave:str) -> None:

        super().__init__(tamaño)
        #CONFECCION
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #ANIMACIONES
        self.contador_pasos = 0
        self.animaciones_proyectil = animaciones
        self.reescalar_animaciones()
        #RECTANGULOS
        self.rectangulo = self.animaciones_proyectil[clave][0].get_rect()
        self.rectangulo.x = posicion_actual[0]
        self.rectangulo.y = posicion_actual[1]
        self.lados_proyectil = obtener_rectangulos(self.rectangulo)
        #SONIDO
        self.sonido_colision = pygame.mixer.Sound("Recursos/Proyerctil_pj/Colision_proyectil/Sound Effect.wav")
        self.sonido_colision.set_volume(0.4)

        self.velocidad = velocidad

    def reescalar_animaciones(self)->None:
        for clave in self.animaciones_proyectil:
            reescalar_imagenes(self.animaciones_proyectil[clave], (self.ancho, self.alto))        

    def lanzar_proyectil(self, velocidad)->None:
        for lado in self.lados_proyectil:
            self.lados_proyectil[lado].x += velocidad
    
    def lanzar_meteoro(self, velocidad)->None:
        for lado in self.lados_proyectil:
            self.lados_proyectil[lado].y += velocidad

    def animar_proyectil(self, pantalla, que_animacion:str)->None:
        animacion = self.animaciones_proyectil[que_animacion]
        largo = len(animacion)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        pantalla.blit(animacion[self.contador_pasos], self.lados_proyectil["main"]) 
        self.contador_pasos += 1 

    def colision_proyectil(self, lista_plataformas, lista_enemigo, lista_proyectiles, pantalla, jugador):
        for lado in lista_plataformas:
            if self.lados_proyectil["main"].colliderect(lado.lados_plataforma["main"]):
                self.sonido_colision.play()
                self.remove_objeto(lista_proyectiles)

        for enemigo in lista_enemigo:
            if self.lados_proyectil["main"].colliderect(enemigo.lados_enemigo["main"]):
                self.sonido_colision.play()
                jugador.mi_score += 500
                enemigo.comportamiento = "destroyed"
                if enemigo.direccion_derecha:
                    enemigo.animar_enemigo(pantalla, "destroyed_izquierda")
                else:
                    enemigo.animar_enemigo(pantalla, "destroyed_derecha")
                enemigo.animar_enemigo(pantalla, "burst")
                self.remove_objeto(lista_proyectiles)
                lista_enemigo.remove(enemigo)

        return len(lista_enemigo)
    
    def eliminar_smile(self, pantalla, jugador, lista_smile, lista_proyectiles):
        for smile in lista_smile:
            if self.lados_proyectil["main"].colliderect(smile.lados_enemigo["main"]):
                self.sonido_colision.play()
                jugador.mi_score += 300
                smile.animar_enemigo(pantalla, "burst")
                self.remove_objeto(lista_proyectiles)
                lista_smile.remove(smile)

    def colision_proyectil_pj(self, pantalla, lados_piso, lista_plataformas, jugador, lista_proyectiles, posicion_inicial, meteoro):
        for lado in lista_plataformas:
            if self.lados_proyectil["main"].colliderect(lado.lados_plataforma["main"]):
                self.sonido_colision.play()
                lista_proyectiles.remove(meteoro)

        if self.lados_proyectil["main"].colliderect(lados_piso["main"]):
            self.sonido_colision.play()
            lista_proyectiles.remove(meteoro)
        
        if self.lados_proyectil["main"].colliderect(jugador.lados["main"]):
            jugador.animar(pantalla, "recibo_daño")
            jugador.salud -= 1
            jugador.daño_recibido += 88
            match jugador.salud:
                case 2:
                    jugador.damage_2.play()
                case 1:
                    jugador.damage_1.play()
                case 0:
                    jugador.damage_0.play()
            # luego de recivir daño vuelve a la posicion de inicio
            jugador.rectangulo.x = posicion_inicial[0]
            jugador.rectangulo.y = posicion_inicial[1]
            jugador.lados = obtener_rectangulos(jugador.rectangulo)
            lista_proyectiles.remove(meteoro)
            
    def colision_proyectil_final_boss(self, pantalla, lista_plataformas, lista_proyectiles, final_boss):
        for lado in lista_plataformas:
            if self.lados_proyectil["main"].colliderect(lado.lados_plataforma["main"]):
                self.sonido_colision.play()
                self.remove_objeto(lista_proyectiles)

        if final_boss.vida_finalboss != 0:
            if self.lados_proyectil["main"].colliderect(final_boss.lados_enemigo["main"]):
                self.daño_final_boss(pantalla, final_boss)
                self.sonido_colision.play()
                self.remove_objeto(lista_proyectiles)
            
    def daño_final_boss(self, pantalla, final_boss):
        if final_boss.direccion_derecha:
            final_boss.animar_enemigo(pantalla, "destroyed_derecha")
        else:
            final_boss.animar_enemigo(pantalla, "destroyed_izquierda")
        final_boss.vida_finalboss -= 5
        final_boss.daño_recibido_finalboss += 5

    def remove_objeto(self, lista_objeto):
        for objeto in lista_objeto:
                lista_objeto.remove(objeto)
                