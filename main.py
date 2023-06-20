#--------------------main--------------------#

import pygame, sys
from pygame.locals import *
from configuraciones import *
from class_per_principal import *
from class_enemigo import *
from class_plataforma import *
from class_score_item import *
from modo import *

#------------------------------------------------------------#
def actualizar_pantalla(pantalla, un_personaje:Personaje_Principal, fondo, lados_piso, lista_plataformas, lista_enemigos, armor:Enemigo, crabtank:Enemigo, lista_monedas)->None:
    pantalla.blit(fondo, (0,0))

    for plataforma in range(len(lista_plataformas)):
        lista_plataformas[plataforma].dibujar(pantalla)

    for moneda in range(len(lista_monedas)):
        lista_monedas[moneda].animar_item(pantalla, "moneda")

    un_personaje.update(pantalla, lados_piso, lista_plataformas, lista_enemigos)
    armor.update(pantalla)
    crabtank.update(pantalla)
#------------------------------------------------------------#

W,H = 1900,1000
FPS = 25
TAMAÑO_PANTALLA = (W,H)

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((W,H))

#ICONO
icono = pygame.image.load("Recursos\\icon.png")
pygame.display.set_icon(icono)

#FONDO
fondo = pygame.image.load("Recursos\\fondo_1.png")
fondo = pygame.transform.scale(fondo,TAMAÑO_PANTALLA)

#MUSICA
pygame.mixer.music.load("Sound_track\\Metal Gear Rising Revengeance Soundtrack - 01. Rules of Nature (Platinum Mix).mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

#PERSONAJE
posicion_inicial = (H/2 - 380, 740)
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

mi_personaje = Personaje_Principal(tamaño, diccionario_animaciones_personaje, posicion_inicial, 12)

#FUENTE
fuente = pygame.font.SysFont("Arial", 30)

#ENEMIGO 
posicion_inicial_armor = (1700, 740)
tamaño_armor = (110, 165)
diccionario_animaciones_armor = {}
diccionario_animaciones_armor["enemigo_izquierda"] = armor_camina
diccionario_animaciones_armor["enemigo_derecha"] = armor_camina_derecha

armor = Enemigo(tamaño_armor, diccionario_animaciones_armor, posicion_inicial_armor, 3)

posicion_inicial_crabtank = (820, 388)
tamaño_crabtank = (158, 128)
diccionario_animaciones_crabtank = {}
diccionario_animaciones_crabtank["enemigo_izquierda"] = crabtank_camina
diccionario_animaciones_crabtank["enemigo_derecha"] = crabtank_camina_derecha

crabtank = Enemigo(tamaño_crabtank, diccionario_animaciones_crabtank, posicion_inicial_crabtank, 2)

#Proximamente creer clase para la plataforma
#PISO
piso = pygame.Rect(0,0,W,20)
piso.top = mi_personaje.lados["main"].bottom

#PLATAFORMAS
posicion_inicial_plataforma_1 = (1264,689)
tamaño_plataforma_1 = (118,190)
posicion_inicial_plataforma_2 = (1112,745)
tamaño_plataforma_2 = (100,159)
posicion_inicial_primer_piso = (1395,570)
tamaño_primer_piso = (505,25)
posicion_inicial_segundo_piso = (561, 505)
tamaño_segundo_piso = (436,25) 

posicion_inicial_rd = (W,0)
tamaño_rectangulo_d = (5,H)

rectangulo_derecha = Plataforma(tamaño_rectangulo_d, posicion_inicial_rd, "Recursos\\lado_derecho.png")
primer_plataforma = Plataforma(tamaño_plataforma_1, posicion_inicial_plataforma_1, "Recursos\\door_plataform.png")
segunda_plataforma = Plataforma(tamaño_plataforma_2, posicion_inicial_plataforma_2, "Recursos\\stone.png")
primer_piso = Plataforma(tamaño_primer_piso, posicion_inicial_primer_piso, "Recursos\\primer_piso.png")
segundo_piso = Plataforma(tamaño_segundo_piso, posicion_inicial_segundo_piso, "Recursos\\primer_piso.png")

#ITEMS
posicion_inicial_moneda_1 = (1500, 495)
tamaño_moneda_1 = (40, 40)
posicion_inicial_moneda_2 = (1600, 495)
tamaño_moneda_2 = (40, 40)
posicion_inicial_moneda_3 = (1700, 495)
tamaño_moneda_3 = (40, 40)
posicion_inicial_moneda_4 = (1800, 495)
tamaño_moneda_4 = (40, 40)
posicion_inicial_moneda_5 = (519, 395)
tamaño_moneda_5 = (40, 40)
posicion_inicial_moneda_6 = (420, 315)
tamaño_moneda_6 = (40, 40)
posicion_inicial_moneda_7 = (283, 245)
tamaño_moneda_7 = (40, 40)
posicion_inicial_moneda_8 = (160, 328)
tamaño_moneda_8 = (40, 40)
diccionario_animaciones_score_item = {}
diccionario_animaciones_score_item["moneda"] = score_moneda

primer_moneda = Score_Item(tamaño_moneda_1, diccionario_animaciones_score_item, posicion_inicial_moneda_1)
segunda_moneda = Score_Item(tamaño_moneda_2, diccionario_animaciones_score_item, posicion_inicial_moneda_2)
tercer_moneda = Score_Item(tamaño_moneda_3, diccionario_animaciones_score_item, posicion_inicial_moneda_3)
cuarta_moneda = Score_Item(tamaño_moneda_4, diccionario_animaciones_score_item, posicion_inicial_moneda_4)
quinta_moneda = Score_Item(tamaño_moneda_5, diccionario_animaciones_score_item, posicion_inicial_moneda_5)
sexta_moneda = Score_Item(tamaño_moneda_6, diccionario_animaciones_score_item, posicion_inicial_moneda_6)
septima_moneda = Score_Item(tamaño_moneda_7, diccionario_animaciones_score_item, posicion_inicial_moneda_7)
octava_moneda = Score_Item(tamaño_moneda_8, diccionario_animaciones_score_item, posicion_inicial_moneda_8)

lista_plataformas = [primer_plataforma, segunda_plataforma, primer_piso, segundo_piso, rectangulo_derecha]
lista_enemigos = [armor, crabtank]
lista_monedas = [primer_moneda, segunda_moneda, tercer_moneda, cuarta_moneda, quinta_moneda, sexta_moneda, septima_moneda, octava_moneda]

lados_piso = obtener_rectangulos(piso)

while True:
    RELOJ.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_F12:
            cambiar_modo()
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            # posicion que clockea en la pantalla 'pos'
            print(evento.pos)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        mi_personaje.que_hace = "derecha"
        # arregle la funcion, para que colisione del lado izquierdo de las plataformas
        mi_personaje.colision_plataforma(segunda_plataforma)
        mi_personaje.direccion_derecha = True
        mi_personaje.salto_derecha = True
    elif keys[pygame.K_LEFT]:
        mi_personaje.que_hace = "izquierda"
        mi_personaje.direccion_derecha = False
        mi_personaje.salto_derecha = False
    elif keys[pygame.K_UP]:
        mi_personaje.que_hace = "salta"
    elif keys[pygame.K_q]:
        mi_personaje.que_hace = "pj_proyectil"
    else:
        mi_personaje.que_hace = "quieto"

    actualizar_pantalla(PANTALLA, mi_personaje, fondo, lados_piso, lista_plataformas, lista_enemigos, armor, crabtank, lista_monedas)

    # mi_personaje.colision_plataforma(segunda_plataforma)
    mi_personaje.colision_enemigo(PANTALLA, lista_enemigos)
    mi_personaje.verificar_colision_monedas(lista_monedas)
    armor.colision_plataforma(segunda_plataforma, rectangulo_derecha, "right", "left")
    crabtank.colision_plataforma(segundo_piso, segundo_piso, "left", "right")

    texto = fuente.render(f"Coins X {mi_personaje.mi_score}", False, "Black", "Gray")
    PANTALLA.blit(texto, (0,0)) 

    if get_modo():
        for lado in mi_personaje.lados:
            pygame.draw.rect(PANTALLA, "Red", armor.lados_enemigo[lado], 2)
            pygame.draw.rect(PANTALLA, "Red", crabtank.lados_enemigo[lado], 2)
            pygame.draw.rect(PANTALLA, "Blue", mi_personaje.lados[lado], 2)
            pygame.draw.rect(PANTALLA, "Yellow", lados_piso[lado], 2)
            pygame.draw.rect(PANTALLA, "Yellow", primer_piso.lados_plataforma[lado], 2)
            pygame.draw.rect(PANTALLA, "Yellow", segundo_piso.lados_plataforma[lado], 2)
            pygame.draw.rect(PANTALLA, "Orange", primer_plataforma.lados_plataforma[lado], 2)
            pygame.draw.rect(PANTALLA, "Orange", segunda_plataforma.lados_plataforma[lado], 2)
            pygame.draw.rect(PANTALLA, "Yellow", rectangulo_derecha.lados_plataforma[lado], 2)

        for moneda in lista_monedas:
            pygame.draw.rect(PANTALLA, "Blue", primer_moneda.rectangulo, 2)
            pygame.draw.rect(PANTALLA, "Blue", segunda_moneda.rectangulo, 2)
            pygame.draw.rect(PANTALLA, "Blue", tercer_moneda.rectangulo, 2)
            pygame.draw.rect(PANTALLA, "Blue", cuarta_moneda.rectangulo, 2)
            pygame.draw.rect(PANTALLA, "Blue", quinta_moneda.rectangulo, 2)
            pygame.draw.rect(PANTALLA, "Blue", sexta_moneda.rectangulo, 2)
            pygame.draw.rect(PANTALLA, "Blue", septima_moneda.rectangulo, 2)
            pygame.draw.rect(PANTALLA, "Blue", octava_moneda.rectangulo, 2)

    pygame.display.update()
