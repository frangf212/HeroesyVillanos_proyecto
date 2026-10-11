from utils.logger import logger

def comparar(valor_personaje, operador, valor_buscado):
    if operador == "=":
        return valor_personaje == valor_buscado
    elif operador == ">":
        return valor_personaje > valor_buscado
    elif operador == "<":
        return valor_personaje < valor_buscado
    elif operador == ">=":
        return valor_personaje >= valor_buscado
    elif operador == "<=":
        return valor_personaje <= valor_buscado
    elif operador == "!=":
        return valor_personaje != valor_buscado
    else:
        raise ValueError(f"Operador no válido: {operador}")


def obtener_valor(personje,atrib):
    atrib = atrib.lower()
    try:
        if atrib in personje.cualidades:
            return personje.cualidades[atrib]
        else:
           return getattr(personje,atrib)
    except AttributeError:
        logger.error(f"El atributo {atrib} no existe")
        raise




def buscarpersonaje(dicpersonaje,atrib, operador, valor):
    resultado=[]

    try:
        buscarvalor=float(valor)
    except ValueError:
        buscarvalor=valor.lower()



    for p in dicpersonaje.values():
        try:
            valorp=obtener_valor(p,atrib)

        except AttributeError:
            return []

        if isinstance(valorp,str):
            valorp=valorp.lower()

        try:
            if comparar(valorp,operador,buscarvalor):
                resultado.append(p)
        except (TypeError,ValueError) as e:
            logger.error(f"Búsqueda inválida: {atrib} {operador} {valor} ({e})")
            return  []

    if resultado:
        logger.info(f"Búsqueda {atrib} {operador} {valor}: {len(resultado)} resultados")
    else:
        logger.warning(f"Búsqueda {atrib} {operador} {valor}: sin resultados")

    return resultado



