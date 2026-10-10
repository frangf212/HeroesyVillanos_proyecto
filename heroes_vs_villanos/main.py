# This is a sample Python script.
from datetime import date

from models.personajes import Personaje




p = Personaje("Ana", "López", date(2003, 5, 3))
p1 = Personaje("Ana", "López", date(2000, 5, 3))

print(p.identificador,p.nombre, p.fecha_nacimiento)
print(p1.identificador,p1.nombre, p1.fecha_nacimiento)

print(p.edad)
print(p1.edad)

