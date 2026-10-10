
from datetime import date

from models.heroes import Heroe
from models.personajes import Personaje
from models.villanos import Villano
from services.regsitro import crear_heroe, heroes, crear_villano, villanos

h = Heroe("Ana", "López", date(2000, 5, 3))
print(h)
print(h.cualidades)

v= Villano("Fernando", "Ruiz", date(1999, 1, 20))
print(v)
print(v.cualidades)


for i in range(50):
    crear_heroe()
    crear_villano()
print(len(heroes), len(villanos))

