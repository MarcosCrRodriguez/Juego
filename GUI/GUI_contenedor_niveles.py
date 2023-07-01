import pygame
from pygame.locals import *

from GUI.GUI_label import *
from GUI.GUI_form import *
from GUI.GUI_button_image import *
from Levels.archivo_json import *

class Form_Contenedor_Niveles(Form):
    def __init__(self, pantalla: pygame.Surface, nivel) -> None:
        super().__init__(pantalla, 0, 0, pantalla.get_width(), pantalla.get_height(), None)
        self.nivel = nivel
        self.nivel._slave = self._slave

        self.terminado = "Incompleto"

        self._btn_home = Button_Image(screen=self._slave,
                        master_x = self._x,
                        master_y = self._y, 
                        x = self._slave.get_width() - 100,
                        y = self._slave.get_height() - 100,
                        w = 50,
                        h = 50,
                        onclick = self.btn_home_click,
                        onclick_param = "",
                        path_image= "GUI\home.png")

    def update(self, lista_eventos):
        self.terminado = leer_nivel_completado("archivo_nivel_completado.json")
        self.completed()
        self.nivel.update(lista_eventos)
        for widget in self.lista_widgets:
            widget.update(lista_eventos)
        self.draw()

    def btn_home_click(self, param):
        self.end_dialog()

    def completed(self):
        if self.terminado == "Completado" or self.terminado == "Fallido":
            self.btn_home_click("exit")
            #self.lista_widgets.append(self._btn_home)
