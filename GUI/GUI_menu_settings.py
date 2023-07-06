import pygame
from pygame.locals import *

from GUI.GUI_slider import *
from GUI.GUI_label import *
from GUI.GUI_form import *
from GUI.GUI_button_image import *
from GUI.GUI_contenedor_niveles import *
from GUI.GUI_menu_controls import *
from Levels.manejador_niveles import Manejador_Niveles
from Levels.nivel import *
from Levels.archivo_json import *

class Form_Settings(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, path_imagen, niveles_dict, margen_x, margen_y, espacio, volumen):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)

        self.volumen = volumen
        self.flag_play = True

        aux_imagen = pygame.image.load(path_imagen)
        aux_imagen = pygame.transform.scale(aux_imagen,(w,h))

        pygame.mixer.music.set_volume(self.volumen)

        self._slave = aux_imagen

        self._niveles_dict = niveles_dict

        self._margen_y = margen_y

        label_nivel = Label(self._slave, x=margen_x-20, y=20, w=w/2 -margen_x-10, h=50, text="Settings", 
                        font="Verdana", font_size=30, font_color="White", path_image="GUI/bar.png")
        
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
        self.btn_play = Button(self._slave, x, y, 100, 100, 100, 50, "Red", "Blue", self.btn_play_click, "Nombre", 
                               "Pause", font="Comic Sans", font_size=15, font_color="White")
        self.control_play = Button(self._slave, x, y, 100, 280, 120, 60, "Gray", "Black", self.btn_controls_click, "Nombre", 
                               "Controls", font="Comic Sans", font_size=20, font_color="Black")
        self.label_volume = Label(self._slave, 650, 190, 100, 50, "20%", font="Comic Sans", font_size=15, 
                                  font_color="White", path_image="GUI\Table.png")
        self.slider_volumen = Slider(self._slave, x, y, 100, 200, 500, 15, self.volumen, "Blue", "White")

        self.lista_widgets.append(self._btn_home)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.control_play)
        self.lista_widgets.append(self.label_volume)
        self.lista_widgets.append(self.slider_volumen)
 
    def update(self, lista_eventos):
        if self.verificar_dialog_result():                  
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.update_volumen(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)

    def btn_home_click(self, param):
        self.end_dialog()

    def btn_play_click(self, texto):
        if self.flag_play:
            pygame.mixer.music.pause()
            self.btn_play._color_background = "Cyan"
            self.btn_play._font_color = "Red"
            self.btn_play.set_text("Play")
        else:
            pygame.mixer.music.unpause()
            self.btn_play._color_background = "Red"
            self.btn_play._font_color = "White"
            self.btn_play.set_text("Pause")

        self.flag_play = not self.flag_play
    
    def btn_controls_click(self, texto):
        settings_dict = []
        
        form_controls = Form_Controls(self._master, 450, 100, 1000, 600, (220,0,220), "White", True, "GUI/background_settings.png",
                                       settings_dict, 100, 100, 10)

        self.show_dialog(form_controls)

    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volume.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)

