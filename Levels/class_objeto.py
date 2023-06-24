#--------------------clase_objeto--------------------#
# incompleto
# poximamente para realizar la clase "cabezera"

from configuraciones import obtener_rectangulos

class Objeto:
    def __init__(self, tamaño, posicion_inicial, clave) -> None:
        #CONFECCION
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #RECTANGULOS
        rectangulo = self.animaciones[clave][0].get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(rectangulo)