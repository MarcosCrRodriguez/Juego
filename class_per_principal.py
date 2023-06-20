#--------------------clase_per_principal--------------------#

import pygame
from configuraciones import reescalar_imagenes, obtener_rectangulos
from class_plataforma import *

class Personaje_Principal:
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad) -> None:
        #CONFECCION
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #GRAVEDAD
        self.gravedad = 1
        self.potencia_salto = -18
        self.limite_velocidad_caida = 18
        self.esta_saltando = False
        #ANIMACIONES
        self.contador_pasos = 0
        self.que_hace = "quieto"
        self.animaciones = animaciones
        self.reescalar_animaciones()
        #RECTANGULOS
        rectangulo = self.animaciones["camina_derecha"][0].get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(rectangulo)
        #ACCION_PJ
        self.velocidad = velocidad
        self.desplazamiento_y = 0
        #DIRECCION
        self.direccion_derecha = True
        self.salto_derecha = True
        #SCORE
        self.mi_score = 0

    #quieto - saltar - caminar_derecha - caminar_izquierda
    def reescalar_animaciones(self)->None:
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], (self.ancho, self.alto))

    def animar(self, pantalla, que_animacion:str)->None:
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        pantalla.blit(animacion[self.contador_pasos], self.lados["main"]) 
        self.contador_pasos += 1   

    def mover(self, velocidad)->None:
        # para mover al personaje hay que mover la x del rectangulo principal
        # movemos todos los lados del rectangulo
        for lado in self.lados:
            self.lados[lado].x += velocidad
            
    def aplicar_graverdad(self, pantalla, piso, lista_plataformas)->None:
        if self.esta_saltando:
            if self.salto_derecha:
                self.animar(pantalla, "salta_derecha")
            else:
                self.animar(pantalla, "salta_izquierda")

            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y

            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad
        
        for plataforma in lista_plataformas:
            if self.lados["bottom"].colliderect(plataforma.lados_plataforma["top"]):
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.lados["main"].bottom = plataforma.lados_plataforma["main"].top
                break
            else:
                self.esta_saltando = True

        if self.lados["bottom"].colliderect(piso["top"]):
            self.desplazamiento_y = 0
            self.esta_saltando = False
            self.lados["main"].bottom = piso["main"].top        

    def update(self, pantalla, piso, lista_plataformas, lista_enemigos)->None:
        match self.que_hace:
            case "derecha":
                if not self.esta_saltando:
                    self.animar(pantalla, "camina_derecha")
                self.mover(self.velocidad)
            case "izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla, "camina_izquierda")
                self.mover(self.velocidad * -1)
            case "salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
            case "quieto":
                if not self.esta_saltando:
                    if self.direccion_derecha:
                        self.animar(pantalla, "quieto_derecha")
                    else:
                        self.animar(pantalla, "quieto_izquierda")
            case "pj_proyectil":
                if not self.esta_saltando:
                    if self.direccion_derecha:
                        self.animar(pantalla, "animacion_proyectil_pj")
                    else:
                        self.animar(pantalla, "animacion_proyectil_pj_izquierda")
            case "recibe_daño":
                if not self.esta_saltando:
                    self.colision_enemigo(pantalla, lista_enemigos)

        self.aplicar_graverdad(pantalla, piso, lista_plataformas)

    # revisar
    def colision_plataforma(self, segunda_plataforma:Plataforma)->None:
        if self.lados["right"].colliderect(segunda_plataforma.lados_plataforma["left"]):
            self.que_hace = "quieto"
            if self.lados["bottom"].colliderect(segunda_plataforma.lados_plataforma["top"]):
                self.que_hace = "derecha"

    # revisar X2
    def colision_enemigo(self, pantalla, lista_enemigos):
        for enemigo in lista_enemigos:
            if self.lados["main"].colliderect(enemigo.lados_enemigo["main"]):
                self.animar(pantalla, "recibo_daño")
                self.mover(-45)

    def verificar_colision_monedas(self, lista_monedas)->None:
        for moneda in lista_monedas:
            if self.lados["main"].colliderect(moneda.rectangulo):
                moneda.sonido_colision.play()
                self.desaparecer_moneda(moneda)
                self.mi_score += 1

    def desaparecer_moneda(self, moneda)->None:
        moneda.rectangulo.x = -200
        moneda.rectangulo.y = -200
        
    


        