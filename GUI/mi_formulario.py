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
from GUI.GUI_menu_settings import *
from Levels.archivo_json import *
from Levels.manejador_niveles import *

class Form_Prueba(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border="Black", border_size=-1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.volumen = 0.2
        self.flag_play = True
        
        pygame.mixer.init()

        self.window = pygame.image.load("GUI\\window_galaxy.png")
        self.window = pygame.transform.scale(self.window,(w,h))     

        #-------------------------------CONTROLES-----------------------------------#
        self.txtbox_usuario = TextBox(self._slave, x, y, 150, 120, 230, 50, "Grey", "White", "Red", "Green", 2, font="Comic Sans", font_size=20, font_color="Black")
        self.txtbox_edad = TextBox(self._slave, x, y, 150, 190, 230, 50, "Grey", "White", "Red", "Green", 2, font="Comic Sans", font_size=20, font_color="Black")
        self.txtbox_mail = TextBox(self._slave, x, y, 150, 260, 230, 50, "Grey", "White", "Red", "Green", 2, font="Comic Sans", font_size=20, font_color="Black")
        self.txtbox_ingreso_usuario = TextBox(self._slave, x, y, 150, 460, 230, 50, "Grey", "White", "Red", "Green", 2, font="Comic Sans", font_size=20, font_color="Black")
        self.registrar_play = Button(self._slave, x, y, 425, 120, 160, 50, "Grey", "Blue", self.btn_registrar_click, "Nombre", "Registrar", font="Comic Sans", font_size=20, font_color="Black")
        self.ingresar_play = Button(self._slave, x, y, 425, 460, 160, 50, "Grey", "Blue", self.btn_ingresar_click, "Nombre", "Ingresar", font="Comic Sans", font_size=20, font_color="Black")
        self.settings = Button_Image(self._slave, x, y, 735, 45, 240, 75, "GUI\settings_image.png", self.btn_settings, "Any")
        self.btn_tabla = Button_Image(self._slave, x, y, 845, 130, 130, 60, "GUI\score_image.png", self.btn_tabla_click, "Any") 
        self.btn_niveles = Button_Image(self._slave, x, y, 685, 452, 300, 130, "GUI\start_image.png", self.btn_niveles_click, "Any")
        #---------------------------------------------------------------------------#
 
        #Agrego controles a lista
        self.lista_widgets.append(self.txtbox_usuario)
        self.lista_widgets.append(self.txtbox_edad)
        self.lista_widgets.append(self.txtbox_mail)
        self.lista_widgets.append(self.txtbox_ingreso_usuario)
        self.lista_widgets.append(self.registrar_play)
        self.lista_widgets.append(self.ingresar_play)
        self.lista_widgets.append(self.settings)
        self.lista_widgets.append(self.btn_tabla)
        self.lista_widgets.append(self.btn_niveles)

        # self.texto = "Nombre"

        pygame.mixer.music.load("GUI\Metal Gear Rising REVENGEANCE MainMenu.mp3")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)

        self.render()

    def update(self, lista_eventos):
        if self.verificar_dialog_result():            
            if self.active:
                self.draw()
                self.render()

                # self._master.blit(self.texto, (22,120))
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                # self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos)

    def render(self):   
        self._slave.blit(self.window, (0,0))

    def btn_registrar_click(self, texto):
        nombre = "?"
        nombre = self.txtbox_usuario.get_text()
        retorno = generar_dato_json("archivo_nombre.json", nombre)
        if retorno != -1:
            print("\nSe cargaron correctamente los datos")
        else:
            print("Algo salio mal al generar el json")

    def btn_ingresar_click(self, texto):
        pass

    def btn_tabla_click(self, texto):
        score_dict = leer_json("archivo_score.json")
        
        form_puntaje = Form_Menu_Score(self._master, 450, 100, 1000, 600, (220,0,220), "White", True, "GUI\\board_menu.jpg",
                                       score_dict, 100, 100, 10)
        
        self.show_dialog(form_puntaje)

    def btn_niveles_click(self, texto):
        niveles_dict = [{"Nivel":"", "Dificultad":"Easy"},
                        {"Nivel":"", "Dificultad":"Normal"},
                        {"Nivel":"", "Dificultad":"Hard"}
                        ]
        
        form_niveles = Form_Menu_Niveles(self._master, 450, 100, 1000, 600, (220,0,220), "White", True, "GUI\\background_levels.png",
                                       niveles_dict, 100, 100, 10)

        self.show_dialog(form_niveles)

    def btn_settings(self, texto):
        settings_dict = []
        
        form_settings = Form_Settings(self._master, 450, 100, 1000, 600, (220,0,220), "White", True, "GUI\\background_settings.png",
                                       settings_dict, 100, 100, 10, self.volumen)

        self.show_dialog(form_settings)