from datetime import date
import random
from utils.logger import logger
from faker import Faker

from models.heroes import Heroe
from models.villanos import Villano

fake = Faker("es_ES")

heroes = {}
villanos = {}


def crear_heroe():
    try:
        nombre = fake.first_name()
        apellido = fake.last_name()
        fecha = fake.date_of_birth(minimum_age=18, maximum_age=70)

        generar_hero = Heroe(nombre, apellido, fecha)
        heroes[generar_hero.identificador] = generar_hero

        logger.info(f"Héroe creado: id={generar_hero.identificador}, "
                f"{generar_hero.nombre} {generar_hero.apellidos}, "
                f"puntuación={generar_hero.puntuacion_total}")

        return generar_hero
    
    except Exception :
        logger.exception("Error al crear Heroe")

def crear_villano():
    try:
        nombre = fake.first_name()
        apellido = fake.last_name()
        fecha = fake.date_of_birth(minimum_age=18, maximum_age=70)

        generar_villano=Villano(nombre, apellido, fecha)
        villanos[generar_villano.identificador] = generar_villano

        logger.info(f"Villano creado: id={generar_villano.identificador}, "
                    f"{generar_villano.nombre} {generar_villano.apellidos}, "
                    f"puntuación={generar_villano.puntuacion_total}")

        return generar_villano

    except Exception :
        logger.exception("Error al crear Villano")







