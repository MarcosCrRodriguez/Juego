#--------------------configuraciones--------------------#

import pygame

#------------------------------------------------------------#
def reescalar_imagenes(lista_imagenes, tamaño)->None:
    for i in range(len(lista_imagenes)):
        lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i], tamaño)

def girar_imagenes(lista_original, flip_x, flip_y)->list:
    lista_girada = []

    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))

    return lista_girada

def obtener_rectangulos(principal)->dict:
    diccionario = {}
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom -10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right -6, principal.top, 6, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 6, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 10)

    return diccionario

def destroy_objetct(objeto)->None:
    del objeto
#------------------------------------------------------------#

personaje_quieto = [pygame.image.load("Recursos\\Quieto\\0.png"),
                    pygame.image.load("Recursos\\Quieto\\1.png"),
                    pygame.image.load("Recursos\\Quieto\\2.png"),
                    pygame.image.load("Recursos\\Quieto\\3.png"),
                    pygame.image.load("Recursos\\Quieto\\4.png"),
                    pygame.image.load("Recursos\\Quieto\\5.png")
                    ]

personaje_quieto_izquierda = girar_imagenes(personaje_quieto, True, False)

personaje_camina = [pygame.image.load("Recursos\\Camina\\54.png"),
                    pygame.image.load("Recursos\\Camina\\55.png"),
                    pygame.image.load("Recursos\\Camina\\56.png"),
                    pygame.image.load("Recursos\\Camina\\57.png")
                    # pygame.image.load("Recursos\\Camina\\58.png"),
                    # pygame.image.load("Recursos\\Camina\\59.png")
                    ]

personaje_camina_izquierda = girar_imagenes(personaje_camina, True, False)

personaje_salta = [pygame.image.load("Recursos\\Salta\\82.png")
                   ]

personaje_salta_izquierda = girar_imagenes(personaje_salta, True, False)

personaje_proyectil_animacion = [pygame.image.load("Recursos\\Proyectil_Animacion_PJ\\216.png"),
                                 pygame.image.load("Recursos\\Proyectil_Animacion_PJ\\217.png"),
                                 pygame.image.load("Recursos\\Proyectil_Animacion_PJ\\218.png"),
                                 pygame.image.load("Recursos\\Proyectil_Animacion_PJ\\219.png"),
                                 pygame.image.load("Recursos\\Proyectil_Animacion_PJ\\220.png"),
                                 pygame.image.load("Recursos\\Proyectil_Animacion_PJ\\221.png"),
                                 pygame.image.load("Recursos\\Proyectil_Animacion_PJ\\222.png"),
                                 pygame.image.load("Recursos\\Proyectil_Animacion_PJ\\223.png")
                                 ]

personaje_proyectil_animacion_izquierda = girar_imagenes(personaje_proyectil_animacion, True, False)

personaje_daño_recibido = [pygame.image.load("Recursos\\Daño_recibido\\852.png"),
                           pygame.image.load("Recursos\\Daño_recibido\\853.png"),
                           pygame.image.load("Recursos\\Daño_recibido\\854.png"),
                           pygame.image.load("Recursos\\Daño_recibido\\855.png")
                           ]

#------------------------------------------------------------#

armor_camina = [pygame.image.load("Recursos\\Armor_Camina\\84.png"),
                pygame.image.load("Recursos\\Armor_Camina\\85.png"),
                pygame.image.load("Recursos\\Armor_Camina\\86.png"),
                pygame.image.load("Recursos\\Armor_Camina\\87.png"),
                pygame.image.load("Recursos\\Armor_Camina\\88.png"),
                pygame.image.load("Recursos\\Armor_Camina\\89.png"),
                pygame.image.load("Recursos\\Armor_Camina\\90.png"),
                pygame.image.load("Recursos\\Armor_Camina\\91.png"),
                pygame.image.load("Recursos\\Armor_Camina\\92.png"),
                pygame.image.load("Recursos\\Armor_Camina\\93.png"),
                pygame.image.load("Recursos\\Armor_Camina\\94.png"),
                pygame.image.load("Recursos\\Armor_Camina\\95.png"),
                pygame.image.load("Recursos\\Armor_Camina\\96.png"),
                pygame.image.load("Recursos\\Armor_Camina\\97.png"),
                pygame.image.load("Recursos\\Armor_Camina\\98.png"),
                pygame.image.load("Recursos\\Armor_Camina\\99.png")
                ]

armor_camina_derecha = girar_imagenes(armor_camina, True, False)

#------------------------------------------------------------#

crabtank_camina = [pygame.image.load("Recursos\\Crabtank_Camina\\14.png"),
                   pygame.image.load("Recursos\\Crabtank_Camina\\15.png"),
                   pygame.image.load("Recursos\\Crabtank_Camina\\16.png"),
                   pygame.image.load("Recursos\\Crabtank_Camina\\17.png"),
                   pygame.image.load("Recursos\\Crabtank_Camina\\18.png"),
                   pygame.image.load("Recursos\\Crabtank_Camina\\19.png"),
                   pygame.image.load("Recursos\\Crabtank_Camina\\20.png"),
                   pygame.image.load("Recursos\\Crabtank_Camina\\21.png"),
                   pygame.image.load("Recursos\\Crabtank_Camina\\22.png"),
                   pygame.image.load("Recursos\\Crabtank_Camina\\23.png"),
                   pygame.image.load("Recursos\\Crabtank_Camina\\24.png"),
                   pygame.image.load("Recursos\\Crabtank_Camina\\25.png")
                   ]

crabtank_camina_derecha = girar_imagenes(crabtank_camina, True, False) 

#------------------------------------------------------------#

score_moneda = [pygame.image.load("Recursos\\Score_Item\\22.png"),
                pygame.image.load("Recursos\\Score_Item\\23.png"),
                pygame.image.load("Recursos\\Score_Item\\24.png"),
                pygame.image.load("Recursos\\Score_Item\\25.png"),
                pygame.image.load("Recursos\\Score_Item\\26.png"),
                pygame.image.load("Recursos\\Score_Item\\27.png"),
                pygame.image.load("Recursos\\Score_Item\\28.png"),
                pygame.image.load("Recursos\\Score_Item\\29.png"),
                pygame.image.load("Recursos\\Score_Item\\30.png"),
                pygame.image.load("Recursos\\Score_Item\\31.png"),
                pygame.image.load("Recursos\\Score_Item\\32.png"),
                pygame.image.load("Recursos\\Score_Item\\33.png"),
                pygame.image.load("Recursos\\Score_Item\\34.png"),
                pygame.image.load("Recursos\\Score_Item\\35.png"),
                pygame.image.load("Recursos\\Score_Item\\36.png"),
                pygame.image.load("Recursos\\Score_Item\\37.png")
                ]

#------------------------------------------------------------#

proyectil_personaje = [pygame.image.load("Recursos\\Proyerctil_pj\\631.png"),
                       pygame.image.load("Recursos\\Proyerctil_pj\\633.png")
                       ]

proyectil_personaje_izquierda = girar_imagenes(proyectil_personaje, True, False)

#------------------------------------------------------------#