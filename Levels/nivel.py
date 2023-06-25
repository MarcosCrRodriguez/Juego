#--------------------nivel--------------------#

import pygame
import time
from pygame.locals import *
from Levels.configuraciones import *
from Levels.class_per_principal import *
from Levels.class_enemigo import *
from Levels.class_proyectil import *
from Levels.class_plataforma import *
from Levels.class_score_item import *
from Levels.modo import *
from Levels.nivel import *

class Nivel:
    def __init__(self, pantalla, personaje_principal, primer_enemigo, segundo_enemigo, lista_plataformas, lista_colision_plataformas, lista_enemigos, 
                 lista_items, lados_piso, mi_imagen, icono_pj, fondo_vida, fondo, font_timer, fondo_timer, fondo_score, font_coins, final_tuple, pos_inicial_corazon, timer, corazones, segundo_piso, final_lvl) -> None:
        self._slave = pantalla
        self.jugador = personaje_principal
        self.primer_enemigo = primer_enemigo
        self.segundo_enemigo = segundo_enemigo
        
        self.tres_enemigos = False
        if len(lista_enemigos) == 3:
            self.tercer_enemigo = self.armor_segundo
            self.tres_enemigos = True

        self.lista_enemigos = lista_enemigos

        self.plataformas = lista_plataformas
        self.plataformas_colision = lista_colision_plataformas
        self.lista_items = lista_items
        self.lista_proyectiles = []

        self.segundo_piso = segundo_piso

        #PROYECTIL
        self.tamaño_proyectil = (35, 50)
        self.diccionario_animaciones_proyectil = {}
        self.diccionario_animaciones_proyectil["proyectil_derecha"] = proyectil_personaje
        self.diccionario_animaciones_proyectil["proyectil_izquierda"] = proyectil_personaje_izquierda

        self.lados_piso = lados_piso

        self.mi_imagen = mi_imagen
        self.icono_pj = icono_pj
        self.fondo_vida = fondo_vida
        self.fondo = fondo
        self.font_timer = font_timer
        self.fondo_timer = fondo_timer
        self.fondo_score = fondo_score
        self.font_coins = font_coins

        self.verde_oscuro = (0, 100, 0)
        self.violeta = (138, 43, 226)

        self.final_tuple = final_tuple
        self.lista_next_lvl = []

        self.hay_corazones = corazones
        self.is_final_lvl = final_lvl

        posicion_inicial_corazon = pos_inicial_corazon
        tamaño_corazon = (50, 50)

        diccionario_animaciones_corazon = {}
        diccionario_animaciones_corazon["corazon"] = corazon_animation 

        self.corazon = Score_Item(tamaño_corazon, diccionario_animaciones_corazon, posicion_inicial_corazon, "corazon")
        
        self.lista_corazones = []
        self.lista_corazones.append(self.corazon)

        if self.is_final_lvl:
            self.borde_vida_finalboss = pygame.image.load("Recursos\\borde_vida_finalboss.png")
            self.borde_vida_finalboss = pygame.transform.scale(self.borde_vida_finalboss,(541, 80))
            self.barra_vida = pygame.image.load("Recursos\\barra_vida.png")
            self.barra_vida = pygame.transform.scale(self.barra_vida,(330, 25))

        #TIMER
        self.start_time = time.time()
        self.duration = timer

        self.floor = pygame.image.load("Recursos\\floor.png")
        self.floor = pygame.transform.scale(self.floor,(1900,30))

    def update(self, lista_eventos)->None:
        # self.finish = True

        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_F12:
                cambiar_modo()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                print(evento.pos)

        current_time = time.time() - self.start_time
        time_left = max(self.duration - current_time, 0)
        minutes = int(time_left // 60)
        seconds = int(time_left % 60)

        self.leer_inputs()
        self.actualizar_pantalla()          

        for proyectil in self.lista_proyectiles:
            proyectil.lanzar_proyectil(proyectil.velocidad)
            if self.velocidad_proyectil > 0:
                proyectil.animar_proyectil(self._slave, "proyectil_derecha")
            else:
                proyectil.animar_proyectil(self._slave, "proyectil_izquierda")
            
            if self.is_final_lvl  == False:              
                proyectil.colision_proyectil(self.plataformas_colision, self.lista_enemigos, self.lista_proyectiles, self._slave)
                self.jugador.enemigo_dispara(self.segundo_piso, self.segundo_enemigo)
            else:
                proyectil.colision_proyectil_final_boss(self._slave, self.plataformas_colision, self.lista_proyectiles, self.primer_enemigo)

        self.jugador.colision_enemigo(self._slave, self.lista_enemigos, (70, 740))
        self.jugador.verificar_colision_item(self.lista_items, "Recursos\\Score_Item\\All_Grabed\\yare.ogg")
        if self.hay_corazones:
            self.jugador.verificar_colision_vida(self.lista_corazones, "Recursos\\Corazon\\Sound\\vpcn120.ogg", "Recursos\\Corazon\\Sound\\vpcn118.ogg") 

        if self.is_final_lvl  == False:
            self.primer_enemigo.colision_plataforma(self.plataformas[1], self.plataformas[4], "right", "left")
            if self.tres_enemigos:
                self.item_recover = self.tercer_enemigo.colision_plataforma(self.plataformas[1], self.plataformas[7], "left", "right")
        else:
            # armar nueva colision que se teletransporte por el mapa mientras colisiona para el "final_boss"
            self.primer_enemigo.colision_plataforma(self.plataformas[1], self.plataformas[4], "right", "left")
            #self.primer_enemigo.meteor_attack()

        self.segundo_enemigo.colision_plataforma(self.plataformas[3], self.plataformas[3], "left", "right")        

        texto = self.font_coins.render(f"Coins X {self.jugador.mi_score}", False, "Black", self.verde_oscuro)
        self._slave.blit(self.fondo_score, (12,110))
        self._slave.blit(texto, (22,120)) 

        text_surface = self.font_timer.render(f"Timer: {minutes:02d}:{seconds:02d}", True, "White")
        self._slave.blit(self.fondo_timer, (860, 8))
        self._slave.blit(text_surface, (900, 35))

        # if time_left == 0:
        #     self.finish = False
        # elif con_vida == False:
        #     self.finish = False 

        self.dibujar_rectangulos()

        # return self.finish 
    
    def leer_inputs(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.jugador.que_hace = "derecha"
            self.jugador.colision_plataforma(self.plataformas_colision, "right", "left", "derecha")
            self.jugador.direccion_derecha = True
            self.jugador.salto_derecha = True
            # mi_personaje.esta_quieto = False
        elif keys[pygame.K_LEFT]:
            self.jugador.que_hace = "izquierda"
            self.jugador.colision_plataforma(self.plataformas_colision, "left", "right", "izquierda")
            self.jugador.direccion_derecha = False
            self.jugador.salto_derecha = False
            # mi_personaje.esta_quieto = False
        elif keys[pygame.K_UP]:
            self.jugador.que_hace = "salta"
            # self.jugador.colision_plataforma(self.plataformas_colision, "top", "bottom", "salta")
            # mi_personaje.esta_quieto = False
        elif keys[pygame.K_q]:
            if len(self.lista_proyectiles) < 1:
                self.jugador.que_hace = "pj_proyectil"
                if self.jugador.direccion_derecha:
                    self.velocidad_proyectil = 18
                else:
                    self.velocidad_proyectil = -18
                proyectil = Proyectil(self.tamaño_proyectil, self.diccionario_animaciones_proyectil, self.jugador.lados["main"].center, self.velocidad_proyectil, "proyectil_derecha")
                self.lista_proyectiles.append(proyectil)
        else:
            self.jugador.que_hace = "quieto"
            # mi_personaje.esta_quieto = True

    def actualizar_pantalla(self)->None:
        self._slave.blit(self.fondo, (0,0))

        for plataforma in range(len(self.plataformas)):
            self.plataformas[plataforma].draw(self._slave)

        for item in range(len(self.lista_items)):
            self.lista_items[item].animar_item(self._slave, "moneda")

        if self.hay_corazones:
            for corazon in range(len(self.lista_corazones)):
                self.lista_corazones[corazon].animar_item(self._slave, "corazon")

        if len(self.lista_items) == 0:
            self.obtener_next_lvl()

        self._slave.blit(self.fondo_vida, (102,15))
        self._slave.blit(self.icono_pj, (12,8))
        self._slave.blit(self.mi_imagen, (20,15))
        pygame.draw.rect(self._slave, (255,0,0), (102,20, 264, 18)) 
        pygame.draw.rect(self._slave, self.verde_oscuro, (102,20, 264 - self.jugador.daño_recibido, 18))
            
        self.jugador.update(self._slave, self.lados_piso, self.plataformas, self.lista_enemigos)
        for enemigo in self.lista_enemigos:
            enemigo.update(self._slave)
        
        if self.is_final_lvl:
            self._slave.blit(self.floor, (0, 995))
            pygame.draw.rect(self._slave, (255,0,0), (1445, 42, 330, 25))
            pygame.draw.rect(self._slave, self.violeta, (1445, 42, 330 - self.primer_enemigo.daño_recibido_finalboss, 25)) 
            self._slave.blit(self.borde_vida_finalboss, (1346, 17))

            self.primer_enemigo.update_vida_finalboss(self._slave, self.primer_enemigo.vida_finalboss, 20)

    def dibujar_rectangulos(self):
        if get_modo():
            for lado in self.jugador.lados:
                pygame.draw.rect(self._slave, "Blue", self.jugador.lados[lado], 2)
                pygame.draw.rect(self._slave, "Orange", self.lados_piso[lado], 2)
                for enemigo in self.lista_enemigos:
                    pygame.draw.rect(self._slave, "Red", enemigo.lados_enemigo[lado], 2)
                for plataforma in self.plataformas:
                    pygame.draw.rect(self._slave, "Yellow", plataforma.lados_plataforma[lado], 2)
                if len(self.lista_proyectiles) > 0:
                    for proyectil in self.lista_proyectiles:
                        pygame.draw.rect(self._slave, "Gray", proyectil.lados_proyectil[lado], 2)

            for item in self.lista_items:
                pygame.draw.rect(self._slave, "Blue", item.rectangulo, 2)
            if self.hay_corazones:
                for corazon in self.lista_corazones:
                        pygame.draw.rect(self._slave, "Blue", corazon.rectangulo, 2)
            
            if len(self.lista_next_lvl) > 0:
                for next_lvl in self.lista_next_lvl:
                        pygame.draw.rect(self._slave, "Blue", next_lvl.rectangulo, 2)
            
    def obtener_next_lvl(self)->None:
        #NEXT_LVL
        tamaño_next_lvl = (105, 105)
        diccionario_animaciones_next_lvl = {} 
        diccionario_animaciones_next_lvl["next_lvl"] = next_lvl

        self.next_lvl = Score_Item(tamaño_next_lvl, diccionario_animaciones_next_lvl, self.final_tuple, "next_lvl")
    
        self.next_lvl.animar_item(self._slave, "next_lvl")

        self.lista_next_lvl.append(self.next_lvl)
        
