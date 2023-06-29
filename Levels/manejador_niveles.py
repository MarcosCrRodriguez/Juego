from pygame.locals import *

from Levels.nivel_uno import Nivel_Uno
from Levels.nivel_dos import Nivel_Dos
from Levels.nivel_tres import Nivel_Tres

class Manejador_Niveles:
    def __init__(self, pantalla) -> None:
        self._slave = pantalla
        self.niveles = {"nivel_uno": Nivel_Uno,
                        "nivel_dos": Nivel_Dos,
                        "nivel_tres": Nivel_Tres}
        self.obtener_nivel = ""
        
    def get_nivel(self, nombre_nivel):
        self.obtener_nivel = nombre_nivel
        return self.niveles[nombre_nivel](self._slave)
    
    def devolver_nivel_actual(self):
        return self.obtener_nivel
