from abc import abstractmethod, ABC
from datetime import date

class Personaje(ABC):
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
        if (fecha_actual.month, fecha_actual.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
            anios = anios - 1

        return anios




    @abstractmethod
    def calcular_puntuacion(self):
        pass




    def __str__(self):
        return f"{self.identificador}, {self.nombre}, {self.apellidos},{self.edad} anios,{self.puntuacion_total}"