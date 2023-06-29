#--------------------clase_per_principal--------------------#

import pygame
from Levels.configuraciones import reescalar_imagenes, obtener_rectangulos
from Levels.class_plataforma import *
from Levels.class_proyectil import *

class Personaje_Principal:
    def __init__(self, tamaño:tuple, animaciones:dict, posicion_inicial:tuple, velocidad:int) -> None:
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
        self.rectangulo = self.animaciones["camina_derecha"][0].get_rect()
        self.rectangulo.x = posicion_inicial[0]
        self.rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(self.rectangulo)
        #ACCION_PJ
        self.velocidad = velocidad
        self.desplazamiento_y = 0
        #DIRECCION
        self.direccion_derecha = True
        self.salto_derecha = True
        #self.esta_quieto = True
        #SCORE
        self.mi_score = 0
        #NIVEL SALUD
        self.salud = 3
        self.daño_recibido = 0

        self.damage_2 = pygame.mixer.Sound("Recursos\\Daño_recibido\Sonido\\vpcn005.ogg")
        self.damage_2.set_volume(0.4)
        self.damage_1 = pygame.mixer.Sound("Recursos\\Daño_recibido\Sonido\\vpcn030.ogg")
        self.damage_1.set_volume(0.4)
        self.damage_0 = pygame.mixer.Sound("Recursos\\Daño_recibido\Sonido\\vpcn031.ogg")
        self.damage_0.set_volume(0.4)

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
                    self.salta_vol = pygame.mixer.Sound("Recursos\\Salta\\Sound\\vpcn100.ogg")
                    self.salta_vol.set_volume(0.2)
                    self.salta_vol.play()
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
                    self.salta_vol = pygame.mixer.Sound("Recursos\\Proyectil_Animacion_PJ\\Sound\\vpcn101.ogg")
                    self.salta_vol.set_volume(0.2)
                    self.salta_vol.play()
            case "recibe_daño":
                if not self.esta_saltando:
                    self.colision_enemigo(pantalla, lista_enemigos)

        self.aplicar_graverdad(pantalla, piso, lista_plataformas)

    def colision_plataforma(self, lista_colision_plataformas:list, lado_pj:str, lado_plataforma:str, direccion:str)->None:
        for plataforma in lista_colision_plataformas:
            if self.lados[lado_pj].colliderect(plataforma.lados_plataforma[lado_plataforma]):
                self.que_hace = "quieto"
                if self.lados["bottom"].colliderect(plataforma.lados_plataforma["top"]):
                    self.que_hace = direccion

    def colision_enemigo(self, pantalla, lista_enemigos, posicion_inicial)->bool:
        con_vida = True

        for enemigo in lista_enemigos:
            if self.lados["main"].colliderect(enemigo.lados_enemigo["main"]):
                self.animar(pantalla, "recibo_daño")
                self.salud -= 1
                self.daño_recibido += 88
                # luego de recivir daño vuelve a la posicion de inicio
                self.rectangulo.x = posicion_inicial[0]
                self.rectangulo.y = posicion_inicial[1]
                self.lados = obtener_rectangulos(self.rectangulo)
                match self.salud:
                    case 2:
                        self.damage_2.play()
                    case 1:
                        self.damage_1.play()
                    case 0:
                        self.damage_0.play()
                if self.salud < 0:
                    con_vida = False

        return con_vida    

    # revisar.....
    def enemigo_dispara(self, segundo_piso, enemigo)->bool:
        hostil = False

        if self.lados["bottom"].colliderect(segundo_piso.lados_plataforma["top"]):
            # enemigo.comportamiento = "lanzar_proyectil"
            enemigo.velocidad_enemigo = 7
            hostil = True
        else:
            enemigo.velocidad_enemigo = 2
        # else:
        #     if enemigo.direccion_derecha:
        #         enemigo.comportamiento = "e_derecha"
        #     else:
        #         enemigo.comportamiento = "e_izquierda"

        return hostil
            
    def verificar_colision_item(self, lista_item:list, sound:str)->None:
        for item in range(len(lista_item)):
            if self.lados["main"].colliderect(lista_item[item].rectangulo):
                lista_item[item].sonido_colision.play()
                self.mi_score += 100 
                lista_item.remove(lista_item[item])
                if len(lista_item) == 0:
                    self.all_collected = pygame.mixer.Sound(sound)
                    self.all_collected.set_volume(0.4)
                    self.all_collected.play()
                break

    def verificar_colision_vida(self, lista_item:list, sound_1:str, sound_2:str)->None:
        for item in range(len(lista_item)):
            if self.lados["main"].colliderect(lista_item[item].rectangulo):
                lista_item[item].sonido_colision.play()
                if self.salud == 3:
                    self.all_collected = pygame.mixer.Sound(sound_1)
                    self.all_collected.set_volume(0.4)
                    self.all_collected.play()
                else:
                    self.salud += 1 
                    self.daño_recibido -= 88
                    self.all_collected = pygame.mixer.Sound(sound_2)
                    self.all_collected.set_volume(0.4)
                    self.all_collected.play()
                lista_item.remove(lista_item[item])
                break

    def verificar_colision_final_item(self, lista_item:list, path:str)->bool:
        retorno = False

        for item in range(len(lista_item)):
            if self.lados["main"].colliderect(lista_item[item].rectangulo):
                lista_item.remove(lista_item[item])
                finish = pygame.mixer.Sound(path)
                finish.set_volume(0.4)
                finish.play()
                retorno = True
                break

        return retorno

    


        