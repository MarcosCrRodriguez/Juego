import pygame
from pygame.locals import *

from GUI_label import *
from GUI_form import *
from GUI_button_image import *

class Form_Menu_Niveles(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, path_imagen, niveles_dict, margen_x, margen_y, espacio):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)

        aux_imagen = pygame.image.load(path_imagen)
        aux_imagen = pygame.transform.scale(aux_imagen,(w,h))

        self._slave = aux_imagen
        self.niveles_dict = niveles_dict

        self.margen_y = margen_y

        label_nivel = Label(self._slave, x=margen_x +10, y=20, w=w/2 -margen_x-10, h=50, text="Nivel", 
                        font="Verdana", font_size=30, font_color="White", path_image="GUI\\bar.png")
        
        self.lista_widgets.append(label_nivel)

        pos_inicial_y = margen_y