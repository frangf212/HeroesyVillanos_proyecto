from abc import abstractmethod
from datetime import date

class Personaje:
    _contador = 0
    def __init__(self, nombre, apellidos, fecha_nacimiento):
        Personaje._contador+=1
        self.identificador=Personaje._contador
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.puntuacion_total =0


    @property
    def edad(self):
        fecha_actual = date.today()
        anios=fecha_actual.year-self.fecha_nacimiento.year
        if fecha_actual.month<self.fecha_nacimiento.month and self.fecha_nacimiento.day>fecha_actual.day:
            anios=anios-1
        return anios







# @abstractmethod
# def calcular_puntuacion(self):
#
    #
    #
    #
    #
    # def __str__(self):
    #
    #
