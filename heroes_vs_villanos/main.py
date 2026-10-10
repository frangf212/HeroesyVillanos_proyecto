
from datetime import date

from models.heroes import Heroe
from models.personajes import Personaje




h = Heroe("Ana", "López", date(2000, 5, 3))
print(h)
print(h.cualidades)

