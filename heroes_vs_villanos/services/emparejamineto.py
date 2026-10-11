import random
from utils.logger import logger

EQUILIBRADO= 10
DESEQUILIBRADO=20



def emparejamineto(heroes,villanos):
    if not heroes or not villanos:
        logger.warning("No se puede emparejar: falta algún héroe o villano")
        return None

    heroe=random.choice(list(heroes.values()))
    villano=random.choice(list(villanos.values()))
    diferencia=abs(heroe.puntuacion_total-villano.puntuacion_total)

    if diferencia<=EQUILIBRADO:
        veredicto="Equlibrado"
    elif diferencia >= DESEQUILIBRADO:
        veredicto = "Alta desviación"
    else:
        veredicto = "Diferencia moderada"

    logger.info(f"Se enfrentan el heroeher {heroe.identificador} {heroe.nombre} y el villano {villano.identificador} {villano.nombre}"
                f"La punruacion del heroe es{heroe.puntuacion_total}  y la del villano es {villano.puntuacion_total}"
                f"el veredicto del comabate es {veredicto}")
    return heroe, villano, veredicto



