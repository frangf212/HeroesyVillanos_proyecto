
from datetime import date

from models.heroes import Heroe
from models.personajes import Personaje
from models.villanos import Villano

h = Heroe("Ana", "López", date(2000, 5, 3))
print(h)
print(h.cualidades)

v= Villano("Fernando", "Ruiz", date(1999, 1, 20))
print(v)
print(v.cualidades)

