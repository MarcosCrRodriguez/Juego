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

class Nivel_Tres(Nivel):
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
        fondo = pygame.image.load("Recursos\\fondo_3.png")
        fondo = pygame.transform.scale(fondo,(W,H))

        #IMAGEN_TIMER
        pygame.font.init()
        font_timer = pygame.font.SysFont("Arial", 30)

        fondo_timer = pygame.image.load("Recursos\\em_castelvania.png")
        fondo_timer = pygame.transform.scale(fondo_timer,(250, 97))

        #IMAGEN_SCORE
        fondo_score = pygame.image.load("Recursos\\fondo_score.png")
        fondo_score = pygame.transform.scale(fondo_score,(188, 70))

        #MUSICA
        pygame.mixer.music.load("Sound_track\[Music] Metal Gear Rising Revengeance - Vs. Jetstream Sam.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)

        #PERSONAJE
        posicion_inicial = (600, 830)
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
        posicion_inicial_final_boss = (1280, 735)
        tamaño_final_boss = (190, 265)
        diccionario_animaciones_final_boss = {}
        diccionario_animaciones_final_boss["enemigo_derecha"] = camina_final_boss
        diccionario_animaciones_final_boss["enemigo_izquierda"] = camina_final_boss_izquierda
        # diccionario_animaciones_final_boss["rage_derecha"] = rage_final_boss
        # diccionario_animaciones_final_boss["rage_izquierda"] = rage_final_boss_izquierda
        diccionario_animaciones_final_boss["destroyed_derecha"] = daño_recibido_final_boss
        diccionario_animaciones_final_boss["destroyed_izquierda"] = daño_recibido_final_boss_izquierda
        diccionario_animaciones_final_boss["meteor_derecha"] = meteor_attack_final_boss
        diccionario_animaciones_final_boss["meteor_izquierda"] = meteor_attack_final_boss_izquierda
        diccionario_animaciones_final_boss["r_meteor_derecha"] = meteor_attack_final_boss_rage
        diccionario_animaciones_final_boss["r_meteor_izquierda"] = meteor_attack_final_boss_izquierda_rage

        final_boss = Enemigo(tamaño_final_boss, diccionario_animaciones_final_boss, posicion_inicial_final_boss, 5)

        posicion_inicial_bird = (820, 34)
        tamaño_bird = (75, 75)
        diccionario_animaciones_bird = {}
        diccionario_animaciones_bird["enemigo_derecha"] = bird_vuela
        diccionario_animaciones_bird["enemigo_izquierda"] = bird_vuela_izquierda

        bird = Enemigo(tamaño_bird, diccionario_animaciones_bird, posicion_inicial_bird, 6)

        #Proximamente creer clase para la plataforma
        #PISO
        piso = pygame.Rect(0,0,W,20)
        piso.top = mi_personaje.lados["main"].bottom

        lados_piso = obtener_rectangulos(piso)

        #PLATAFORMAS
        posicion_inicial_plataforma_1 = (375,580)
        tamaño_plataforma_1 = (325,30)
        posicion_inicial_plataforma_2 = (1900 - 675,580)
        tamaño_plataforma_2 = (325,30)
        posicion_inicial_primer_piso = (0,750)
        tamaño_primer_piso = (175,115)
        posicion_inicial_segundo_piso = (1725,750)
        tamaño_segundo_piso = (175,115)
        posicion_inicial_plataforma_3 = (300,830)
        tamaño_plataforma_3 = (175,115)
        posicion_inicial_plataforma_4 = (1475,830)
        tamaño_plataforma_4 = (175,115) 
        posicion_inicial_plataforma_vida = (850, 460)
        tamaño_plataforma_vida = (200, 125)

        posicion_inicial_rr = (W,0)
        tamaño_rectangulo_r = (6,H)
        posicion_inicial_rl = (-6,0)
        tamaño_rectangulo_l = (7,H)
        posicion_inicial_rt = (0,25)
        tamaño_rectangulo_t = (W,15)

        rectangulo_derecha = Plataforma(tamaño_rectangulo_r, posicion_inicial_rr, "Recursos\\costado.png")
        rectangulo_izquierda = Plataforma(tamaño_rectangulo_l, posicion_inicial_rl, "Recursos\\costado.png")
        rectangulo_arriba = Plataforma(tamaño_rectangulo_t, posicion_inicial_rt, "Recursos\\arriba.png")
        primer_plataforma = Plataforma(tamaño_plataforma_1, posicion_inicial_plataforma_1, "Recursos\\floor.png")
        segunda_plataforma = Plataforma(tamaño_plataforma_2, posicion_inicial_plataforma_2, "Recursos\\floor.png")
        primer_piso = Plataforma(tamaño_primer_piso, posicion_inicial_primer_piso, "Recursos\corrupto_pf_1.png")
        segundo_piso = Plataforma(tamaño_segundo_piso, posicion_inicial_segundo_piso, "Recursos\corrupto_pf_1.png")
        tercer_piso = Plataforma(tamaño_plataforma_3, posicion_inicial_plataforma_3, "Recursos\corrupto_pf_1.png")
        cuarto_piso = Plataforma(tamaño_plataforma_4, posicion_inicial_plataforma_4, "Recursos\corrupto_pf_1.png")
        plataforma_vida = Plataforma(tamaño_plataforma_vida, posicion_inicial_plataforma_vida, "Recursos\corrupto_pf_2.png")

        #FUENTE_COINS
        font_coins = pygame.font.SysFont("Arial", 30)

        #ITEMS
        posicion_inicial_moneda_1 = (450, 495)
        tamaño_moneda_1 = (40, 40)
        posicion_inicial_moneda_2 = (600, 495)
        tamaño_moneda_2 = (40, 40)
        posicion_inicial_moneda_3 = (1300, 495)
        tamaño_moneda_3 = (40, 40)
        posicion_inicial_moneda_4 = (1450, 495)
        tamaño_moneda_4 = (40, 40)
        diccionario_animaciones_score_item = {}
        diccionario_animaciones_score_item["moneda"] = score_moneda

        primer_moneda = Score_Item(tamaño_moneda_1, diccionario_animaciones_score_item, posicion_inicial_moneda_1, "moneda")
        segunda_moneda = Score_Item(tamaño_moneda_2, diccionario_animaciones_score_item, posicion_inicial_moneda_2, "moneda")
        tercer_moneda = Score_Item(tamaño_moneda_3, diccionario_animaciones_score_item, posicion_inicial_moneda_3, "moneda")
        cuarta_moneda = Score_Item(tamaño_moneda_4, diccionario_animaciones_score_item, posicion_inicial_moneda_4, "moneda")
        
        lista_plataformas = [plataforma_vida, tercer_piso, segundo_piso, rectangulo_arriba, cuarto_piso, primer_plataforma, primer_piso, rectangulo_derecha, rectangulo_izquierda, segunda_plataforma]
        lista_colision_plataformas = [plataforma_vida, segunda_plataforma, primer_piso, segundo_piso, primer_plataforma, rectangulo_derecha, rectangulo_izquierda, rectangulo_arriba, tercer_piso, cuarto_piso]
        lista_monedas = [primer_moneda, segunda_moneda, tercer_moneda, cuarta_moneda]
        lista_enemigos = [final_boss, bird]

        lista_plataforma_final = [plataforma_vida, tercer_piso, segundo_piso, cuarto_piso, primer_piso, rectangulo_derecha, rectangulo_izquierda]

        #CORAZON
        corazones = True 
        final_lvl = True 

        super().__init__(pantalla, mi_personaje, final_boss, bird, lista_plataformas, lista_colision_plataformas, lista_enemigos,
                         lista_monedas, lados_piso, mi_imagen, icono_pj, fondo_vida, fondo, font_timer, fondo_timer, fondo_score, font_coins, 
                         (900,800), (925,175), 300, corazones, segundo_piso, final_lvl, lista_plataforma_final, (895, 265))