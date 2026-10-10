from datetime import date
import random
from faker import Faker

from models.heroes import Heroe
from models.villanos import Villano

fake = Faker("es_ES")

heroes = {}
villanos = {}


def crear_heroe():
    nombre = fake.first_name()
    apellido = fake.last_name()
    fecha = fake.date_of_birth(minimum_age=18, maximum_age=70)

    generar_hero = Heroe(nombre, apellido, fecha)
    heroes[generar_hero.identificador] = generar_hero

    return generar_hero
def crear_villano():
    nombre = fake.first_name()
    apellido = fake.last_name()
    fecha = fake.date_of_birth(minimum_age=18, maximum_age=70)

    generar_villano=Villano(nombre, apellido, fecha)
    villanos[generar_villano.identificador] = generar_villano
    return generar_villano







