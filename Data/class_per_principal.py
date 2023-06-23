#--------------------clase_per_principal--------------------#

import pygame
from configuraciones import reescalar_imagenes, obtener_rectangulos
from class_plataforma import *
from class_proyectil import *

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
        self.daño_recivido = 0

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

        # Creo barra de vida - (proximamente seran corazones) 

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
                        # proyectil_pj.animar_proyectil(pantalla, "proyectil_pj_derecha")
                        # proyectil_pj.lanzar_proyectil(proyectil_pj.velocidad)
                    else:
                        self.animar(pantalla, "animacion_proyectil_pj_izquierda")
                        # proyectil_pj.animar_proyectil(pantalla, "proyectil_pj_izquierda")
                        # proyectil_pj.lanzar_proyectil(proyectil_pj.velocidad* -1)
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
                self.daño_recivido += 88
                # luego de recivir daño vuelve a la posicion de inicio
                self.rectangulo.x = posicion_inicial[0]
                self.rectangulo.y = posicion_inicial[1]
                self.lados = obtener_rectangulos(self.rectangulo)
                match self.salud:
                    case 2:
                        self.damage = pygame.mixer.Sound("Recursos\\Daño_recibido\Sonido\\vpcn005.ogg")
                        self.damage.set_volume(0.4)
                        self.damage.play()
                    case 1:
                        self.damage = pygame.mixer.Sound("Recursos\\Daño_recibido\Sonido\\vpcn030.ogg")
                        self.damage.set_volume(0.4)
                        self.damage.play()
                    case 0:
                        self.damage = pygame.mixer.Sound("Recursos\\Daño_recibido\Sonido\\vpcn031.ogg")
                        self.damage.set_volume(0.4)
                        self.damage.play()
                if self.salud < 0:
                    con_vida = False

        return con_vida    

    # revisar
    def verificar_colision_monedas(self, lista_monedas:list)->None:
        for moneda in range(len(lista_monedas)):
            if self.lados["main"].colliderect(lista_monedas[moneda].rectangulo):
                lista_monedas[moneda].sonido_colision.play()
                lista_monedas.remove(lista_monedas[moneda])
                #del lista_monedas[moneda]
                self.mi_score += 1
                if len(lista_monedas) == 0:
                    self.all_collected = pygame.mixer.Sound("Recursos\\Score_Item\\All_Grabed\\yare.ogg")
                    self.all_collected.set_volume(0.4)
                    self.all_collected.play()
                break

    # def desaparecer_moneda(self, moneda)->None:
    #     moneda.rectangulo.x = -200
    #     moneda.rectangulo.y = -200
        
    


        