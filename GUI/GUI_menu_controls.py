import pygame
from pygame.locals import *

from GUI.GUI_slider import *
from GUI.GUI_label import *
from GUI.GUI_form import *
from GUI.GUI_button_image import *
from GUI.GUI_contenedor_niveles import *
from Levels.manejador_niveles import Manejador_Niveles
from Levels.nivel import *
from Levels.archivo_json import *

class Form_Controls(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, path_imagen, niveles_dict, margen_x, margen_y, espacio):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)

        aux_imagen = pygame.image.load(path_imagen)
        aux_imagen = pygame.transform.scale(aux_imagen,(w,h))

        self.q_buttom = pygame.image.load("GUI\\16.png")
        self.q_buttom = pygame.transform.scale(self.q_buttom,(35,35))
        self.top_arrow = pygame.image.load("GUI\\42.png")
        self.top_arrow = pygame.transform.scale(self.top_arrow,(35,35))
        self.left_arrow = pygame.image.load("GUI\\45.png")
        self.left_arrow = pygame.transform.scale(self.left_arrow,(35,35))
        self.right_arrow = pygame.image.load("GUI\\43.png")
        self.right_arrow = pygame.transform.scale(self.right_arrow,(35,35))
        self.F12 = pygame.image.load("GUI\\F12.png")
        self.F12 = pygame.transform.scale(self.F12,(65,43))

        font_controls = pygame.font.SysFont("Comic Sans", 34)
        self.texto_q = font_controls.render("------------  fire projectile", True, "Gray")
        self.texto_top_arrow = font_controls.render("------------  jump", True, "Gray")
        self.texto_left_arrow = font_controls.render("------------  move left", True, "Gray")
        self.texto_right_arrow = font_controls.render("------------  move right", True, "Gray")
        self.texto_f12 = font_controls.render("------------  programmer visual", True, "Gray")

        self._slave = aux_imagen

        self._niveles_dict = niveles_dict

        self._margen_y = margen_y

        label_nivel = Label(self._slave, x=margen_x-20, y=20, w=w/2 -margen_x-10, h=50, text="Controls", 
                        font="Verdana", font_size=30, font_color="White", path_image="GUI\\bar.png")
        
        self.lista_widgets.append(label_nivel)

        pos_inicial_y = margen_y

        for j in self._niveles_dict:
            pos_inicial_x = margen_x
            for n,s in j.items():
                cadena = ""
                cadena = f"{s}"
                jugador = Label(self._slave, pos_inicial_x, pos_inicial_y, w/2-margen_x, 100, cadena,
                                "Verdana", 30, "White","GUI\Table.png")
                self.lista_widgets.append(jugador)
                pos_inicial_x += w/2 - margen_x
            pos_inicial_y += 100 + espacio

        self._btn_home = Button_Image(screen=self._slave, x=w-70, y=h-70, master_x=x, master_y=y, w=50, h=50,
                                     color_background=(255,0,0), color_border=(255,0,255), onclick=self.btn_home_click,
                                     onclick_param="", text="", font="Verdana", font_size=15, font_color=(0,255,0), 
                                     path_image="GUI\home.png")

        self.lista_widgets.append(self._btn_home)
 
    def update(self, lista_eventos):
        if self.verificar_dialog_result():                  
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self._slave.blit(self.q_buttom, (30,115))
            self._slave.blit(self.top_arrow, (30,175))
            self._slave.blit(self.left_arrow, (30,235))
            self._slave.blit(self.right_arrow, (30,295))
            self._slave.blit(self.F12, (20,355))
            self._slave.blit(self.texto_q, (110,110))
            self._slave.blit(self.texto_top_arrow, (110,170))
            self._slave.blit(self.texto_left_arrow, (110,230))
            self._slave.blit(self.texto_right_arrow, (110,290))
            self._slave.blit(self.texto_f12, (110,350))
            self.draw()
        else:
            self.hijo.update(lista_eventos)

    def btn_home_click(self, param):
        self.end_dialog()
    


