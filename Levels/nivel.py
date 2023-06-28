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
                 lista_items, lados_piso, mi_imagen, icono_pj, fondo_vida, fondo, font_timer, fondo_timer, fondo_score, font_coins, final_tuple, pos_inicial_corazon, 
                 timer, corazones, segundo_piso, final_lvl, lista_plataforma_final, posicion_inicial_pj) -> None:
        self._slave = pantalla
        self.jugador = personaje_principal
        self.primer_enemigo = primer_enemigo
        self.segundo_enemigo = segundo_enemigo
        
        self.tres_enemigos = False
        if len(lista_enemigos) == 3:
            self.tercer_enemigo = self.armor_segundo
            self.tres_enemigos = True

        self.lista_enemigos = lista_enemigos
        self.largo_lista_enemigos = len(self.lista_enemigos)

        self.plataformas = lista_plataformas
        self.plataformas_colision = lista_colision_plataformas
        self.lista_items = lista_items
        self.lista_proyectiles = []
        self.lista_proyectiles_enemigo = []
        self.lista_plataforma_final = lista_plataforma_final

        self.segundo_piso = segundo_piso

        self.posicion_inicial_pj = posicion_inicial_pj

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
        self.azul = (0, 0, 255)

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

        self.esta_atacando = False

        if self.is_final_lvl:
            self.borde_vida_finalboss = pygame.image.load("Recursos\\borde_vida_finalboss.png")
            self.borde_vida_finalboss = pygame.transform.scale(self.borde_vida_finalboss,(541, 80))
            self.barra_vida = pygame.image.load("Recursos\\barra_vida.png")
            self.barra_vida = pygame.transform.scale(self.barra_vida,(330, 25))

            self.sonido_spawn = pygame.mixer.Sound("Recursos\Final_Boss\spawn.wav")
            self.sonido_spawn.set_volume(0.4)
            self.sonido_spawn.play()

            self.lista_meteoros = self.crear_lista_meteoros(25, 15)

        #TIMER
        self.start_time = time.time()
        self.duration = timer

        self.floor = pygame.image.load("Recursos\\floor.png")
        self.floor = pygame.transform.scale(self.floor,(1900,30))

        self.finish = True

    def update(self, lista_eventos)->None:
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
                self.largo_lista_enemigos = proyectil.colision_proyectil(self.plataformas_colision, self.lista_enemigos, self.lista_proyectiles, self._slave)    
            else:
                proyectil.colision_proyectil_final_boss(self._slave, self.plataformas_colision, self.lista_proyectiles, self.primer_enemigo)

        # if self.hostil:
        #     if len(self.lista_proyectiles_enemigo) < 1:
        #         if self.segundo_enemigo.direccion_derecha:
        #             self.velocidad_proyectil_e = 13
        #         else:
        #             self.velocidad_proyectil_e = -13

        #         proyectil_enemigo = Proyectil(self.tamaño_proyectil, self.diccionario_animaciones_proyectil, self.segundo_enemigo.lados_enemigo["main"].center, self.velocidad_proyectil_e, "proyectil_derecha")
        #         self.lista_proyectiles_enemigo.append(proyectil_enemigo) 

        #     if self.largo_lista_enemigos != 0:
        #         for proyectil_enemigo in self.lista_proyectiles_enemigo:
        #             proyectil_enemigo.lanzar_proyectil(proyectil_enemigo.velocidad)
        #             if self.velocidad_proyectil_e > 0:
        #                 proyectil_enemigo.animar_proyectil(self._slave, "proyectil_derecha")
        #             else:
        #                 proyectil_enemigo.animar_proyectil(self._slave, "proyectil_izquierda")

        #             proyectil_enemigo.colision_proyectil_pj(self._slave, self.plataformas_colision, self.jugador, self.lista_proyectiles_enemigo, (70, 740))
        # else:
        #     pass

        con_vida = self.jugador.colision_enemigo(self._slave, self.lista_enemigos, self.posicion_inicial_pj)
        self.jugador.verificar_colision_item(self.lista_items, "Recursos\\Score_Item\\All_Grabed\\yare.ogg")
        if self.hay_corazones:
            self.jugador.verificar_colision_vida(self.lista_corazones, "Recursos\\Corazon\\Sound\\vpcn120.ogg", "Recursos\\Corazon\\Sound\\vpcn118.ogg") 

        if self.is_final_lvl  == False:
            self.primer_enemigo.colision_plataforma(self.plataformas[1], self.plataformas[4], "right", "left")
            self.hostil = self.jugador.enemigo_dispara(self.segundo_piso, self.segundo_enemigo)
            if self.tres_enemigos:
                self.item_recover = self.tercer_enemigo.colision_plataforma(self.plataformas[1], self.plataformas[7], "left", "right")
        else:
            self.primer_enemigo.teletransportacion(self.plataformas[1], "left", "right", (1350, 323))
            self.primer_enemigo.colision_para_tp(self.plataformas[9], "left", "left", "e_derecha")
            self.primer_enemigo.teletransportacion(self.plataformas[9], "right", "right", (500, 735))
            self.primer_enemigo.teletransportacion(self.plataformas[4], "right", "left", (385, 323))
            self.primer_enemigo.colision_para_tp(self.plataformas[5], "right", "right", "e_izquierda")
            self.primer_enemigo.teletransportacion(self.plataformas[5], "left", "left", (1280, 735))
            # self.primer_enemigo.meteor_attack()  

        self.segundo_enemigo.colision_plataforma(self.plataformas[3], self.plataformas[3], "left", "right")       

        texto = self.font_coins.render(f"Coins X {self.jugador.mi_score}", False, "Black", self.verde_oscuro)
        self._slave.blit(self.fondo_score, (12,110))
        self._slave.blit(texto, (22,120)) 

        text_surface = self.font_timer.render(f"Timer: {minutes:02d}:{seconds:02d}", True, "White")
        self._slave.blit(self.fondo_timer, (860, 8))
        self._slave.blit(text_surface, (900, 35))

        if time_left == 0:
            self.finish = False
        elif con_vida == False:
            self.finish = False 

        # print(self.finish)

        self.dibujar_rectangulos()

        return self.finish 
    
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

        if len(self.lista_items) == 0 and self.is_final_lvl == False:
            self.obtener_next_lvl()
        if len(self.lista_items) == 0 and self.is_final_lvl:
            if self.primer_enemigo.vida_finalboss == 0:
                self.obtener_next_lvl()

            # if len(self.lista_next_lvl) != 0:
                # self.jugador.colision_final_item(self.lista_next_lvl)

        self._slave.blit(self.fondo_vida, (102,15))
        self._slave.blit(self.icono_pj, (12,8))
        self._slave.blit(self.mi_imagen, (20,15))
        pygame.draw.rect(self._slave, (255,0,0), (102,20, 264, 18)) 
        pygame.draw.rect(self._slave, self.verde_oscuro, (102,20, 264 - self.jugador.daño_recibido, 18))

        pygame.draw.rect(self._slave, (0,0,0), (102,54, 83, 28))
        if len(self.lista_proyectiles) == 0:
            pygame.draw.rect(self._slave, self.azul, (102,54, 83, 28)) 
            
        self.jugador.update(self._slave, self.lados_piso, self.plataformas, self.lista_enemigos)
        for enemigo in self.lista_enemigos:
            enemigo.update(self._slave)
        
        if self.is_final_lvl:
            self._slave.blit(self.floor, (0, 995))
            pygame.draw.rect(self._slave, (255,0,0), (1445, 42, 330, 25))
            pygame.draw.rect(self._slave, self.violeta, (1445, 42, 330 - self.primer_enemigo.daño_recibido_finalboss, 25)) 
            self._slave.blit(self.borde_vida_finalboss, (1346, 17))

            self.esta_atacando = self.primer_enemigo.update_vida_finalboss(self._slave, self.primer_enemigo.vida_finalboss, self.lista_enemigos)
            
            if self.esta_atacando:
                # for meteoro in self.lista_meteoros:
                    # self._slave.blit(meteoro["superficie"], meteoro["rectangulo"])
                for meteoro in range(len(self.lista_meteoros)):
                    self.lista_meteoros[meteoro].animar_proyectil(self._slave, "meteor")
                    self.lista_meteoros[meteoro].lanzar_meteoro(15)

                for meteoro in self.lista_meteoros:
                    meteoro.colision_proyectil_pj(self._slave, self.lados_piso, self.lista_plataforma_final, self.jugador, self.lista_meteoros, self.posicion_inicial_pj)
            
            elif self.esta_atacando == False:
                self.lista_meteoros = self.crear_lista_meteoros(25, 15)

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
                # if len(self.lista_proyectiles_enemigo) > 0:
                #     for proyectil_enemigo in self.lista_proyectiles_enemigo:
                #         pygame.draw.rect(self._slave, "Gray", proyectil_enemigo.lados_proyectil[lado], 2)
                # if self.esta_atacando:
                #     for meteoro in self.lista_meteoros:
                #         pygame.draw.rect(self._slave, "Gray", meteoro["rectangulo"], 2)
                if self.esta_atacando:
                    for meteoro in self.lista_meteoros:
                        pygame.draw.rect(self._slave, "Gray", meteoro.lados_proyectil[lado], 2)

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

    def crear_lista_meteoros(self, cantidad, velocidad_proyectil)->list:
        lista_nueva = [] 

        for i in range(cantidad):
            tamaño_meteorito = (35, 65)
            diccionario_animaciones_meteorito = {}
            diccionario_animaciones_meteorito["meteor"] = meteorito_finalboss
            x = random.randrange(0, 1900, 60)
            #print(x)
            y = random.randrange(-200, 0, 60)
            #print(y)

            meteoro = Proyectil(tamaño_meteorito, diccionario_animaciones_meteorito, (x,y), velocidad_proyectil, "meteor")
            lista_nueva.append(meteoro)
        
        return lista_nueva
        
