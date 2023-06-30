#--------------------clase_objeto--------------------#
# incompleto
# poximamente para realizar la clase "cabezera"

class Objeto:
    def __init__(self, tamaño:tuple) -> None:
        #CONFECCION
        self.ancho = tamaño[0]
        self.alto = tamaño[1]