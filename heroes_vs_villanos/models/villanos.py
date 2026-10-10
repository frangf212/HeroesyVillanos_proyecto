import random

from models.personajes import Personaje


class Villano(Personaje):
    def __init__(self,nombre,apellidos,fecha_nacimiento):
        super().__init__(nombre,apellidos,fecha_nacimiento)
        self.cualidades = {
            "chagepeteador" : random.randint(0,100),
            "entregador_tardio" : random.randint(0,100),
            "ausencias" : random.randint(0,100),
            "hablador" : random.randint(0,100)

        }
        self.puntuacion_total=self.calcular_puntuacion()

    def calcular_puntuacion(self):
        media_puntuacion = sum(self.cualidades.values())/len(self.cualidades)
        return media_puntuacion