import random

from models.personajes import Personaje


class Heroe(Personaje):
    def __init__(self,nombre,apellidos,fecha_nacimiento):
        super().__init__(nombre,apellidos,fecha_nacimiento)
        self.cualidades={
            "codigolimpio" : random.randint(0,100),
            "bien_documentado" : random.randint(0,100),
            "gitgod" : random.randint(0,100),
            "arquitecto" : random.randint(0,100),
            "detallista" : random.randint(0,100)
        }
        self.puntuacion_total=self.calcular_puntuacion()





    def calcular_puntuacion(self):
        numrandom= sum(self.cualidades.values())/len(self.cualidades)
        return numrandom