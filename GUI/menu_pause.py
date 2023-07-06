import pygame
from pygame.locals import *

from GUI.GUI_widget import *
from GUI.GUI_textbox import *
from GUI.GUI_slider import *
from GUI.GUI_label import *
from GUI.GUI_form import *
from GUI.GUI_button import *
from GUI.GUI_button_image import *

class Form_Menu_Pause(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border="Black", border_size=-1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.volumen = 0.2
        self.flag_play = True

        self.game_pause = False

        pygame.mixer.init()

        self.window = pygame.image.load("GUI/background_pause_menu.jpg")
        self.window = pygame.transform.scale(self.window,(w,h))     

        #-------------------------------CONTROLES-----------------------------------#
        self.btn_renaudar = Button_Image(self._slave, x, y, 245, 95, 85, 58, "GUI/back_menu.png", self.btn_pause_click, "Any") 
        self.btn_play = Button(self._slave, x, y, 100, 100, 100, 50, "Gray", "Black", self.btn_play_click, "Nombre", "Pause", font="Comic Sans", font_size=15, font_color="Black")
        self.label_volume = Label(self._slave, 650, 190, 100, 50, "20%", font="Comic Sans", font_size=15, font_color="White", path_image="GUI/Table.png")
        self.slider_volumen = Slider(self._slave, x, y, 100, 200, 500, 15, self.volumen, "Blue", "White")
        #---------------------------------------------------------------------------#

        #Agrego controles a lista
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.btn_renaudar)
        self.lista_widgets.append(self.label_volume)
        self.lista_widgets.append(self.slider_volumen)

        pygame.mixer.music.load("GUI/Metal Gear Rising REVENGEANCE MainMenu.mp3")

        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)

        self.render()

    def update(self, lista_eventos):
        if self.verificar_dialog_result():            
            if self.active:
                self.draw()
                self.render()

                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos)

    def render(self):   
        self._slave.blit(self.window, (0,0))

    def btn_pause_click(self, texto):
        self.game_pause = False

    def btn_play_click(self, texto):
        if self.flag_play:
            pygame.mixer.music.pause()
            self.btn_play._color_background = "Cyan"
            self.btn_play._font_color = "Red"
            self.btn_play.set_text("Play")
        else:
            pygame.mixer.music.unpause()
            self.btn_play._color_background = "Gray"
            self.btn_play._font_color = "Black"
            self.btn_play.set_text("Pause")

        self.flag_play = not self.flag_play

    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volume.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)

   