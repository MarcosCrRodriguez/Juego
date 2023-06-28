import pygame
from pygame.locals import *

from GUI.GUI_widget import *
from GUI.GUI_textbox import *
from GUI.GUI_slider import *
from GUI.GUI_label import *
from GUI.GUI_form import *
from GUI.GUI_button import *
from GUI.GUI_button_image import *
from GUI.GUI_menu_score import *
from GUI.GUI_menu_niveles import *
from Levels.archivo_json import *

class Form_Prueba(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border="Black", border_size=-1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.volumen = 0.2
        self.flag_play = True

        pygame.mixer.init()

        self.window = pygame.image.load("GUI\\window_galaxy.png")
        self.window = pygame.transform.scale(self.window,(w,h))     

        #-------------------------------CONTROLES-----------------------------------#
        self.txtbox = TextBox(self._slave, x, y, 50, 50, 150, 30, "Grey", "White", "Red", "Green", 2, font="Comic Sans", font_size=15, font_color="Black")
        self.btn_play = Button(self._slave, x, y, 100, 100, 100, 50, "Red", "Blue", self.btn_play_click, "Nombre", "Pause", font="Verdana", font_size=15, font_color="White")
        self.cadena_play = Button(self._slave, x, y, 235, 50, 80, 30, "Grey", "Blue", self.btn_cadena_click, "Nombre", "Get name", font="Verdana", font_size=15, font_color="Black")
        self.label_volume = Label(self._slave, 650, 190, 100, 50, "20%", font="Comic Sans", font_size=15, font_color="White", path_image="GUI\Table.png")
        self.slider_volumen = Slider(self._slave, x, y, 100, 200, 500, 15, self.volumen, "Blue", "White")
        self.btn_tabla = Button_Image(self._slave, x, y, 255, 100, 50, 50, "GUI\menu_image.png", self.btn_tabla_click, "Any") 
        self.btn_niveles = Button_Image(self._slave, x, y, 355, 100, 50, 50, "GUI\start.png", self.btn_niveles_click, "Any")
        #---------------------------------------------------------------------------#

        #Agrego controles a lista
        self.lista_widgets.append(self.txtbox)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.cadena_play)
        self.lista_widgets.append(self.label_volume)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.btn_tabla)
        self.lista_widgets.append(self.btn_niveles)

        pygame.mixer.music.load("GUI\Metal Gear Rising REVENGEANCE MainMenu.mp3")

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
        # self._slave.fill(self._color_background)
        self._slave.blit(self.window, (0,0))

    def btn_cadena_click(self, texto):
        nombre = "?"
        nombre = self.txtbox.get_text()
        retorno = generar_dato_json("archivo_nombre.json", nombre)
        if retorno != -1:
            print("\nSe cargaron correctamente los datos")
        else:
            print("Algo salio mal al generar el json")
            
        # print(nombre)

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

    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volume.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)

    def btn_tabla_click(self, texto):
        score_dict = leer_json("archivo_score.json")
        
        form_puntaje = Form_Menu_Score(self._master, 250, 25, 500, 550, (220,0,220), "White", True, "GUI\\board_menu.jpg",
                                       score_dict, 100, 100, 10)
        
        self.show_dialog(form_puntaje)

    def btn_niveles_click(self, texto):
        niveles_dict = [{"Nivel":"", "Dificultad":"Easy"},
                        {"Nivel":"", "Dificultad":"Normal"},
                        {"Nivel":"", "Dificultad":"Hard"}
                        ]
        
        form_niveles = Form_Menu_Niveles(self._master, 250, 25, 500, 550, (220,0,220), "White", True, "GUI\\board_menu.jpg",
                                       niveles_dict, 100, 100, 10)

        self.show_dialog(form_niveles)
