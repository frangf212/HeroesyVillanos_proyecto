
from datetime import date

from services.busqueda import buscarpersonaje
from services.emparejamineto import emparejamineto
from utils.logger import logger
from models.heroes import Heroe
from models.personajes import Personaje
from models.villanos import Villano
from services.regsitro import crear_heroe, heroes, crear_villano, villanos

def mostrar_menu():
    print("1. Crear héroe")
    print("2. Crear villano")
    print("3. Buscar")
    print("4. Emparejar")
    print("5. Listar todos")
    print("0. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese su opcion: ")

        if opcion == "1":
            try:
                numeroheroes = int(input("¿Cuántos héroes quieres crear? "))
            except ValueError:
                logger.warning("Cantidad no válida al crear héroes")
                print("Introduce un número")
                continue
            for i in range(numeroheroes):
                    crear_heroe()


        elif opcion == "2":
            try:
                numerovillanos = int(input("¿Cuántos villanos quieres crear? "))
            except ValueError:
                logger.warning("Cantidad no válida al crear villanos")
                print("Introduce un número")
                continue
            for i in range(numerovillanos):
                crear_villano()

        elif opcion == "3":
            pedirpersonaje=input("1. Héroes  2. Villanos: ")
            atributo = input("Atributo o cualidad: ")
            operador = input("Operador (=, >, <, >=, <=, !=): ")
            valor = input("Valor: ")
            if pedirpersonaje == "1":
                resultados = buscarpersonaje(heroes, atributo, operador, valor)
            elif pedirpersonaje == "2":
                resultados = buscarpersonaje(villanos, atributo, operador, valor)
            else:
                logger.warning("Opcion no valida")
                continue

        elif opcion == "4":
            resultado=emparejamineto(heroes,villanos)

        elif opcion == "5":
            for v in villanos.values():
                print(v)

            for h in heroes.values():
                print(h)

        elif opcion == "0":
            logger.info("Saliendo")
            break

        else:
            logger.warning(f"Opcion no valida {opcion}")


if __name__ == "__main__":
        main()


