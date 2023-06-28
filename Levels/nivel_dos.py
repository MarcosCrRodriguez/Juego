#--------------------nivel_uno--------------------#

import pygame
from pygame.locals import *
from Levels.configuraciones import *
from Levels.class_per_principal import *
from Levels.class_enemigo import *
from Levels.class_proyectil import *
from Levels.class_plataforma import *
from Levels.class_score_item import *
from Levels.modo import *
from Levels.nivel import *

class Nivel_Dos(Nivel):
    def __init__(self, pantalla:pygame.Surface) -> None:
        
        W = pantalla.get_width()
        H = pantalla.get_height()

        #VIDA
        mi_imagen = pygame.image.load("Recursos\\face_pj.png")
        mi_imagen = pygame.transform.scale(mi_imagen,(76,76))
        icono_pj = pygame.image.load("Recursos\\icono_pj.png")
        icono_pj = pygame.transform.scale(icono_pj,(90,90))
        fondo_vida = pygame.image.load("Recursos\\vida.png")
        fondo_vida = pygame.transform.scale(fondo_vida,(275, 75))

        #ICONO
        icono = pygame.image.load("Recursos\\icon.png")
        pygame.display.set_icon(icono)

        #FONDO
        fondo = pygame.image.load("Recursos\\fondo_2.jpg")
        fondo = pygame.transform.scale(fondo,(W,H))

        #IMAGEN_TIMER
        pygame.font.init()
        font_timer = pygame.font.SysFont("Arial", 30)

        fondo_timer = pygame.image.load("Recursos\\em_castelvania.png")
        fondo_timer = pygame.transform.scale(fondo_timer,(250, 97))

        #IMAGEN_SCORE
        fondo_score = pygame.image.load("Recursos\\fondo_score.png")
        fondo_score = pygame.transform.scale(fondo_score,(155, 70))

        #MUSICA
        pygame.mixer.music.load("Sound_track\\[Music] Metal Gear Rising Revengeance - The Mastermind.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)

        #PERSONAJE
        posicion_inicial = (H/2 - 380, 775)
        tamaño = (110, 165)
        diccionario_animaciones_personaje = {}
        diccionario_animaciones_personaje["quieto_derecha"] = personaje_quieto
        diccionario_animaciones_personaje["quieto_izquierda"] = personaje_quieto_izquierda
        diccionario_animaciones_personaje["salta_derecha"] = personaje_salta
        diccionario_animaciones_personaje["salta_izquierda"] = personaje_salta_izquierda
        diccionario_animaciones_personaje["camina_derecha"] = personaje_camina
        diccionario_animaciones_personaje["camina_izquierda"] = personaje_camina_izquierda
        diccionario_animaciones_personaje["animacion_proyectil_pj"] = personaje_proyectil_animacion
        diccionario_animaciones_personaje["animacion_proyectil_pj_izquierda"] = personaje_proyectil_animacion_izquierda
        diccionario_animaciones_personaje["recibo_daño"] = personaje_daño_recibido
        # diccionario_animaciones_personaje["final_derecha"] = final
        # diccionario_animaciones_personaje["final_izquierda"] = final_izquierda

        mi_personaje = Personaje_Principal(tamaño, diccionario_animaciones_personaje, posicion_inicial, 12)

        #ENEMIGO 
        posicion_inicial_armor = (1700, 775)
        tamaño_armor = (110, 165)
        diccionario_animaciones_armor = {}
        diccionario_animaciones_armor["enemigo_izquierda"] = armor_camina
        diccionario_animaciones_armor["enemigo_derecha"] = armor_camina_derecha
        diccionario_animaciones_armor["destroyed_derecha"] = armor_destroyed
        diccionario_animaciones_armor["destroyed_izquierda"] = armor_destroyed_izquierda

        armor = Enemigo(tamaño_armor, diccionario_animaciones_armor, posicion_inicial_armor, 4)

        posicion_inicial_armor_s = (0, 490)
        tamaño_armor_s = (110, 165)
        diccionario_animaciones_armor_s = {}
        diccionario_animaciones_armor_s["enemigo_izquierda"] = armor_camina
        diccionario_animaciones_armor_s["enemigo_derecha"] = armor_camina_derecha
        diccionario_animaciones_armor_s["destroyed_derecha"] = armor_destroyed
        diccionario_animaciones_armor_s["destroyed_izquierda"] = armor_destroyed_izquierda

        self.armor_segundo = Enemigo(tamaño_armor_s, diccionario_animaciones_armor_s, posicion_inicial_armor_s, 1)

        posicion_inicial_crabtank = (820, 372)
        tamaño_crabtank = (158, 128)
        diccionario_animaciones_crabtank = {}
        diccionario_animaciones_crabtank["enemigo_izquierda"] = crabtank_camina
        diccionario_animaciones_crabtank["enemigo_derecha"] = crabtank_camina_derecha
        diccionario_animaciones_crabtank["proyectil_derecha"] = crabtank_proyectil
        diccionario_animaciones_crabtank["proyectil_izquierda"] = crabtank_proyectil_izquierda
        diccionario_animaciones_crabtank["destroyed_derecha"] = crabtank_destroyed
        diccionario_animaciones_crabtank["destroyed_izquierda"] = crabtank_destroyed_izquierda

        crabtank = Enemigo(tamaño_crabtank, diccionario_animaciones_crabtank, posicion_inicial_crabtank, 2)

        #Proximamente creer clase para la plataforma
        #PISO
        piso = pygame.Rect(0,0,W,20)
        piso.top = mi_personaje.lados["main"].bottom

        lados_piso = obtener_rectangulos(piso)

        #PLATAFORMAS
        posicion_inicial_plataforma_1 = (1440,689)
        tamaño_plataforma_1 = (170,25)
        posicion_inicial_plataforma_2 = (1112,775)
        tamaño_plataforma_2 = (170,25)
        posicion_inicial_primer_piso = (1650,570)
        tamaño_primer_piso = (250,25)
        posicion_inicial_segundo_piso = (535, 492)
        tamaño_segundo_piso = (690,25)
        posicion_inicial_plataforma_5 = (0,645)
        tamaño_plataforma_5 = (380,25) 

        posicion_inicial_rr = (W,0)
        tamaño_rectangulo_r = (6,H)
        posicion_inicial_rl = (-6,0)
        tamaño_rectangulo_l = (7,H)
        posicion_inicial_rt = (0,-8)
        tamaño_rectangulo_t = (W,6)

        rectangulo_derecha = Plataforma(tamaño_rectangulo_r, posicion_inicial_rr, "Recursos\\costado.png")
        rectangulo_izquierda = Plataforma(tamaño_rectangulo_l, posicion_inicial_rl, "Recursos\\costado.png")
        rectangulo_arriba = Plataforma(tamaño_rectangulo_t, posicion_inicial_rt, "Recursos\\arriba.png")
        primer_piso = Plataforma(tamaño_plataforma_1, posicion_inicial_plataforma_1, "Recursos\\primer_piso.png")
        segundo_piso = Plataforma(tamaño_plataforma_2, posicion_inicial_plataforma_2, "Recursos\\primer_piso.png")
        tercer_piso = Plataforma(tamaño_primer_piso, posicion_inicial_primer_piso, "Recursos\\primer_piso.png")
        cuarto_piso = Plataforma(tamaño_segundo_piso, posicion_inicial_segundo_piso, "Recursos\\primer_piso.png")
        quinto_piso = Plataforma(tamaño_plataforma_5, posicion_inicial_plataforma_5, "Recursos\\primer_piso.png")

        posicion_inicial_invisible_1 = (1400,340)
        tamaño_invisible_1 = (170,25)
        posicion_inicial_invisible_2 = (1640,250)
        tamaño_invisible_2 = (260,25)

        invisible_1 = Plataforma(tamaño_invisible_1, posicion_inicial_invisible_1, "Recursos\\primer_piso.png")
        invisible_2 = Plataforma(tamaño_invisible_2, posicion_inicial_invisible_2, "Recursos\\primer_piso.png")

        # self.lista_last_plataforms = []
        # self.lista_last_plataforms.append(invisible_1)
        # self.lista_last_plataforms.append(invisible_2)
        

        #FUENTE_COINS
        font_coins = pygame.font.SysFont("Arial", 30)

        #ITEMS
        posicion_inicial_moneda_1 = (1495, 610)
        tamaño_moneda_1 = (40, 40)
        posicion_inicial_moneda_2 = (1700, 495)
        tamaño_moneda_2 = (40, 40)
        posicion_inicial_moneda_3 = (1800, 495)
        tamaño_moneda_3 = (40, 40)
        posicion_inicial_moneda_4 = (1174, 705)
        tamaño_moneda_4 = (40, 40)
        posicion_inicial_moneda_5 = (650, 410)
        tamaño_moneda_5 = (40, 40)
        posicion_inicial_moneda_6 = (850, 410)
        tamaño_moneda_6 = (40, 40)
        posicion_inicial_moneda_7 = (1050, 410)
        tamaño_moneda_7 = (40, 40)
        posicion_inicial_moneda_8 = (260, 560)
        tamaño_moneda_8 = (40, 40)
        
        diccionario_animaciones_score_item = {}
        diccionario_animaciones_score_item["moneda"] = score_moneda 

        primer_moneda = Score_Item(tamaño_moneda_1, diccionario_animaciones_score_item, posicion_inicial_moneda_1, "moneda")
        segunda_moneda = Score_Item(tamaño_moneda_2, diccionario_animaciones_score_item, posicion_inicial_moneda_2, "moneda")
        tercer_moneda = Score_Item(tamaño_moneda_3, diccionario_animaciones_score_item, posicion_inicial_moneda_3, "moneda")
        cuarta_moneda = Score_Item(tamaño_moneda_4, diccionario_animaciones_score_item, posicion_inicial_moneda_4, "moneda")
        quinta_moneda = Score_Item(tamaño_moneda_5, diccionario_animaciones_score_item, posicion_inicial_moneda_5, "moneda")
        sexta_moneda = Score_Item(tamaño_moneda_6, diccionario_animaciones_score_item, posicion_inicial_moneda_6, "moneda")
        septima_moneda = Score_Item(tamaño_moneda_7, diccionario_animaciones_score_item, posicion_inicial_moneda_7, "moneda")
        octava_moneda = Score_Item(tamaño_moneda_8, diccionario_animaciones_score_item, posicion_inicial_moneda_8, "moneda")

        lista_plataformas = [primer_piso, rectangulo_izquierda, tercer_piso, cuarto_piso, rectangulo_derecha, segundo_piso,  rectangulo_arriba, quinto_piso, invisible_1, invisible_2]
        lista_colision_plataformas = [primer_piso, rectangulo_izquierda, tercer_piso, cuarto_piso, rectangulo_derecha, segundo_piso,  rectangulo_arriba, quinto_piso, invisible_2]
        lista_monedas = [primer_moneda, segunda_moneda, tercer_moneda, cuarta_moneda, quinta_moneda, sexta_moneda, septima_moneda, octava_moneda]
        lista_enemigos = [armor, crabtank, self.armor_segundo]

        lista_plataforma_final = [tercer_piso, segundo_piso, cuarto_piso, primer_piso, rectangulo_derecha, rectangulo_izquierda]

        #CORAZON
        corazones = True 
        final_lvl = False

        super().__init__(pantalla, mi_personaje, armor, crabtank, lista_plataformas, lista_colision_plataformas, lista_enemigos,
                         lista_monedas, lados_piso, mi_imagen, icono_pj, fondo_vida, fondo, font_timer, fondo_timer, fondo_score, font_coins, 
                         (1730,100),(100, 560), 90, corazones, cuarto_piso, final_lvl, lista_plataforma_final, (70, 740))