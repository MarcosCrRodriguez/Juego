from pygame.locals import *

from Levels.nivel_uno import Nivel_Uno
from Levels.nivel_dos import Nivel_Dos

class Manejador_Niveles:
    def __init__(self, pantalla) -> None:
        self._slave = pantalla
        self.niveles = {"nivel_uno": Nivel_Uno,
                        "nivel_dos": Nivel_Dos}
        
    def get_nivel(self, nombre_nivel):
        return self.niveles[nombre_nivel](self._slave)
