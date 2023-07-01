import pygame
from pygame.locals import *

from GUI.GUI_label import *
from GUI.GUI_form import *
from GUI.GUI_button_image import *
from GUI.GUI_contenedor_niveles import *
from Levels.manejador_niveles import Manejador_Niveles
from Levels.nivel import *
from Levels.archivo_json import *

class Form_Menu_Niveles(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, path_imagen, niveles_dict, margen_x, margen_y, espacio):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)

        self.manejador_niveles = Manejador_Niveles(self._master)
        self.nivel_completado = "Incompleto"

        retorno = generar_nivel_completado("archivo_nivel_completado.json", self.nivel_completado)
        if retorno != -1:
            print("\nSe cargaron correctamente los datos")
        else:
            print("Algo salio mal al generar el json")

        self.nivel_acutal = "N/A"

        aux_imagen = pygame.image.load(path_imagen)
        aux_imagen = pygame.transform.scale(aux_imagen,(w,h))

        self._slave = aux_imagen

        self._niveles_dict = niveles_dict

        self._margen_y = margen_y

        label_nivel = Label(self._slave, x=margen_x +10, y=20, w=w/2 -margen_x-10, h=50, text="Nivel", 
                        font="Verdana", font_size=30, font_color="White", path_image="GUI\\bar.png")
        label_dificultad = Label(self._slave, x=margen_x +10 +w/2-margen_x-10, y=20, w=w/2 -margen_x-10, h=50, text="Dificultad", 
                        font="Verdana", font_size=30, font_color="White", path_image="GUI\\bar.png")
        
        self.lista_widgets.append(label_nivel)
        self.lista_widgets.append(label_dificultad)

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
                                     onclick_param="", text="", font="Verdana", font_size=15, font_color=(0,255,0), path_image="GUI\home.png")
        self._btn_level_1 = Button_Image(screen=self._slave, x=272, y=108, master_x=x, master_y=y, w=70, h=70,
                                         color_background=(255,0,0), color_border=(0,0,255), onclick=self.entrar_nivel,
                                         onclick_param="nivel_uno", text="", font="Verdana", font_size=15, font_color=(0,255,0), path_image="GUI\\1st_lvl.png")
        self._btn_level_2 = Button_Image(screen=self._slave, x=275, y=218, master_x=x, master_y=y, w=70, h=70,
                                         color_background=(255,0,0), color_border=(0,0,255), onclick=self.entrar_nivel,
                                         onclick_param="nivel_dos", text="", font="Verdana", font_size=15, font_color=(0,255,0), path_image="GUI\\2nd_lvl.png")
        self._btn_level_3 = Button_Image(screen=self._slave, x=275, y=328, master_x=x, master_y=y, w=70, h=70,
                                         color_background=(255,0,0), color_border=(0,0,255), onclick=self.entrar_nivel,
                                         onclick_param="nivel_tres", text="", font="Verdana", font_size=15, font_color=(0,255,0), path_image="GUI\\3rd_lvl.png")

        self.lista_widgets.append(self._btn_home)
        self.lista_widgets.append(self._btn_level_1)

    def on(self, parametro):
        print("hola", parametro)
 
    def update(self, lista_eventos):
        if self.verificar_dialog_result():                  
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
            if self.nivel_acutal != "N/A":
                self.desbloqueo_niveles()
        else:
            self.hijo.update(lista_eventos)

    def btn_home_click(self, param):
        self.end_dialog()

    def entrar_nivel(self, nombre_nivel):
        nivel = self.manejador_niveles.get_nivel(nombre_nivel)
        self.nivel_acutal = nombre_nivel

        frm_contenedor_nivel = Form_Contenedor_Niveles(self._master, nivel)

        self.show_dialog(frm_contenedor_nivel)
        self.desbloqueo_niveles()

    def desbloqueo_niveles(self):
        self.nivel_completado = leer_nivel_completado("archivo_nivel_completado.json")

        if self.nivel_completado == "Incompleto":
            self.nivel_completado = False
        elif self.nivel_completado == "Fallido":
            self.nivel_completado = False
        elif self.nivel_completado == "Completado":
            self.nivel_completado = True

        if self.nivel_acutal == "nivel_uno" and self.nivel_completado == True:
            self.lista_widgets.append(self._btn_level_2)
        elif self.nivel_acutal == "nivel_dos" and self.nivel_completado == True:
            self.lista_widgets.append(self._btn_level_3)

    # def update(self, lista_eventos):
    #     if self.active:
    #         for widget in self.lista_widgets:
    #             widget.update(lista_eventos)
    #         self.draw()
