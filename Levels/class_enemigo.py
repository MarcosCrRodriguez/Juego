#--------------------clase_enemigo--------------------#

import pygame
import random
from Levels.configuraciones import reescalar_imagenes, obtener_rectangulos
from Levels.class_plataforma import *
from Levels.class_proyectil import *
from Levels.configuraciones import *

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
        self.rectangulo = self.animaciones_enemigo["enemigo_izquierda"][0].get_rect()
        self.rectangulo.x = posicion_inicial[0]
        self.rectangulo.y = posicion_inicial[1]
        self.lados_enemigo = obtener_rectangulos(self.rectangulo)
        #ACCION_ENEMIGO
        self.velocidad_enemigo = velocidad_enemigo
        #DIRECCION
        self.direccion_derecha = True

        self.velocidad_proyectil = 12

        self.sonido_teleeport = pygame.mixer.Sound("Recursos\\Final_Boss\\teleporter.wav")
        self.sonido_teleeport.set_volume(0.4)
        self.sonido_shine = pygame.mixer.Sound("Recursos\Final_Boss\shinde.wav")
        self.sonido_shine.set_volume(0.4)
        self.sonido_metari = pygame.mixer.Sound("Recursos\Final_Boss\metari.wav")
        self.sonido_metari.set_volume(0.4)
        self.sonido_kurae = pygame.mixer.Sound("Recursos\Final_Boss\kurae.wav")
        self.sonido_kurae.set_volume(0.4)
        self.vida_cero = pygame.mixer.Sound("Recursos\\Final_Boss\\final_boss_die.wav")
        self.vida_cero.set_volume(0.4)

        self.vida_finalboss = 330
        self.daño_recibido_finalboss = 0
        
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

    def update(self, pantalla)->None:
        match self.comportamiento:
            case "e_izquierda":
                self.animar_enemigo(pantalla, "enemigo_izquierda")
                self.realizar_comportamiento(self.velocidad_enemigo* -1)
                self.direccion_derecha = False
            case "e_derecha":
                self.animar_enemigo(pantalla, "enemigo_derecha")
                self.realizar_comportamiento(self.velocidad_enemigo)
                self.direccion_derecha = True
            case "lanzar_proyectil":
                if self.direccion_derecha:
                    self.animar_enemigo(pantalla, "proyectil_izquierda")
                    self.enemigo_dispara(self.velocidad_proyectil)
                else:
                    self.animar_enemigo(pantalla, "proyectil_derecha")
                    self.enemigo_dispara(self.velocidad_proyectil* -1)
            # case "r_derecha":
            #     self.animar_enemigo(pantalla, "rage_derecha")
            #     self.realizar_comportamiento((self.velocidad_enemigo + 5)* -1)
            #     self.direccion_derecha = False
            # case "r_izquierda":
            #     self.animar_enemigo(pantalla, "rage_izquierda")
            #     self.realizar_comportamiento(self.velocidad_enemigo + 5)
            #     self.direccion_derecha = True


    def update_vida_finalboss(self, pantalla, vida_actual, lista_enemigos)->bool:
        # self.lista_meteoros = []
        esta_atacando = False

        match vida_actual:
            case 0:
                self.remove_objeto(lista_enemigos)
                self.vida_cero.play()
            case 50:
                #self.sonido_metari.play()
                if self.direccion_derecha:
                    self.direccion_meteor_attack(pantalla, self.velocidad_enemigo+5, "r_meteor_derecha")
                else:
                    self.direccion_meteor_attack(pantalla, (self.velocidad_enemigo+5)* -1, "r_meteor_izquierda")
                esta_atacando = True
            case 100:
                #self.sonido_metari.play()
                if self.direccion_derecha:
                    self.direccion_meteor_attack(pantalla, self.velocidad_enemigo+5, "r_meteor_derecha")
                else:
                    self.direccion_meteor_attack(pantalla, (self.velocidad_enemigo+5)* -1, "r_meteor_izquierda")
                esta_atacando = True
            case 150:
                #self.sonido_kurae.play()
                if self.direccion_derecha:
                    self.direccion_meteor_attack(pantalla, self.velocidad_enemigo+5, "r_meteor_derecha")
                else:
                    self.direccion_meteor_attack(pantalla, (self.velocidad_enemigo+5), "r_meteor_izquierda")
                esta_atacando = True
            case 200:
                #self.sonido_kurae.play()
                if self.direccion_derecha:
                    self.direccion_meteor_attack(pantalla, self.velocidad_enemigo, "meteor_derecha")
                else:
                    self.direccion_meteor_attack(pantalla, self.velocidad_enemigo* -1, "meteor_izquierda")
                esta_atacando = True
            case 250:
                #self.sonido_shine.play()
                if self.direccion_derecha:
                    self.direccion_meteor_attack(pantalla, self.velocidad_enemigo, "meteor_derecha")
                else:
                    self.direccion_meteor_attack(pantalla, self.velocidad_enemigo* -1, "meteor_izquierda")
                esta_atacando = True
            case 300:
                #self.sonido_shine.play()
                if self.direccion_derecha:
                    self.direccion_meteor_attack(pantalla, self.velocidad_enemigo, "meteor_derecha")
                else:
                    self.direccion_meteor_attack(pantalla, self.velocidad_enemigo* -1, "meteor_izquierda")
                esta_atacando = True
        
        return esta_atacando

        # return self.lista_meteoros        

    def direccion_meteor_attack(self, pantalla, velocidad_enemigo, direccion):
        self.animar_enemigo(pantalla, direccion)
        self.realizar_comportamiento(velocidad_enemigo)

    def teletransportacion(self, plataforma:Plataforma, primer_clave:str, segunda_clave:str, posicion_teletransporte:tuple):
        if self.lados_enemigo[primer_clave].colliderect(plataforma.lados_plataforma[segunda_clave]):
            self.sonido_teleeport.play()
            self.rectangulo.x = posicion_teletransporte[0]
            self.rectangulo.y = posicion_teletransporte[1]
            self.lados_enemigo = obtener_rectangulos(self.rectangulo)

    def colision_para_tp(self, plataforma_izquierda:Plataforma, primer_clave:str, segunda_clave:str, direccion:str)->None:
        if self.lados_enemigo[primer_clave].colliderect(plataforma_izquierda.lados_plataforma[segunda_clave]):
            self.comportamiento = direccion

    def enemigo_dispara(self, velocidad):
        pass

    def colision_plataforma(self, plataforma_izquierda:Plataforma, plataforma_derecha:Plataforma, primer_clave:str, segunda_clave:str)->None:
        if self.lados_enemigo["left"].colliderect(plataforma_izquierda.lados_plataforma[primer_clave]):
            self.comportamiento = "e_derecha"
        elif self.lados_enemigo["right"].colliderect(plataforma_derecha.lados_plataforma[segunda_clave]):
            self.comportamiento = "e_izquierda"

    def remove_objeto(self, lista_objeto):
        for objeto in lista_objeto:
                lista_objeto.remove(objeto)
