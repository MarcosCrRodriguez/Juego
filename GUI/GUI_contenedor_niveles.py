import pygame
from pygame.locals import *

from GUI.GUI_label import *
from GUI.GUI_form import *
from GUI.GUI_button_image import *
from Levels.archivo_json import *
from GUI.GUI_menu_settings import *

class Form_Contenedor_Niveles(Form):
    def __init__(self, pantalla: pygame.Surface, nivel) -> None:
        super().__init__(pantalla, 0, 0, pantalla.get_width(), pantalla.get_height(), None)
        self.nivel = nivel
        self.nivel._slave = self._slave
        # self.volumen = 0.1

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
        # eventos = pygame.event.get()
        # for evento in eventos:
        #     if evento.type == KEYDOWN:
        #         if evento.key == pygame.K_p:
        #             self.btn_settings("menu")
        #             print("menu")
        self.nivel.update(lista_eventos)
        for widget in self.lista_widgets:
            widget.update(lista_eventos)
        self.draw()

    def btn_home_click(self, param):
        self.end_dialog()

    def completed(self):
        if self.terminado == "Completado" or self.terminado == "Fallido":
            self.btn_home_click("exit")

    # def btn_settings(self, texto):
    #     settings_dict = []
        
    #     form_settings = Form_Settings(self._master, 450, 100, 1000, 600, (220,0,220), "White", True, "GUI\\background_settings.png",
    #                                    settings_dict, 100, 100, 10, self.volumen)
        
    #     self.show_dialog(form_settings)
