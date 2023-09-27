"""
Ejercicio nivel 2: Videojuegos
Modulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritméticas.
* Instrucciones básicas y consola.
* Dividir y conquistar: funciones y paso de párametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.

@author: Cupi2

"""


def crear_videojuego(titulo: str, anio_de_lanzamiento: int, generos: str, rating: float,
                     es_multijugador: bool, clasificacion_edad: str, duracion: int) -> dict:
    """
    Función para crear un videojuego en la plataforma.

    Parámetros
    ----------

    titulo : str
        Título del videojuego.
    anio_de_lanzamiento : int
        Año de lanzamiento del videojuego.
    generos : str
        Géneros del videojuego separados por coma
    rating : float
        Rating IGN del videojuego, en el rango [0.0, 10.0].
    es_multijugador : bool
        Indica si el videojuego tiene algún modo multijugador.
    clasificacion_edad : str
        Clasificación de edad del videojuego según la ESRB.
    duracion : int
        Duración del videojuego según el sitio HowLongToBeat.
        El formato es XY, con X como las horas y Y como los minutos, ejemplo: 3221.

    Retorno
    -------
    dict
        Diccionario del videojuego con su información.

    """
    juegos = {
        "titulo": titulo,
        "anio_de_lanzamiento": anio_de_lanzamiento,
        "generos": generos,
        "rating": rating,
        "es_multijugador": es_multijugador,
        "clasificacion_edad": clasificacion_edad,
        "duracion": duracion
    }
    return juegos


def buscar_videojuego_por_titulo(j1: dict, j2: dict, j3: dict, j4: dict, titulo: str) -> dict:
    """
    Busca un videojuego en particular por su título.

    Parámetros
    ----------
    j1 : dict
        Diccionario que contiene la información del primer videojuego.
    j2 : dict
        Diccionario que contiene la información del segundo videojuego.
    j3 : dict
        Diccionario que contiene la información del tercer videojuego.
    j4 : dict
        Diccionario que contiene la información del cuarto videojuego.
    titulo : str
        Título del videojuego que se desea buscar.

    Retorno
    -------
    dict
        Diccionario que contiene la información del videojuego encontrado. Si no se encuentra el videojuego,
        retorna None.

    """
    if titulo == j1["titulo"]:
        return j1
    elif titulo == j2["titulo"]:
        return j2
    elif titulo == j3["titulo"]:
        return j3
    elif titulo == j4["titulo"]:
        return j4
    else:
        return None


def buscar_videojuego_mas_corto(j1: dict, j2: dict, j3: dict, j4: dict) -> dict:
    """
    Busca el videojuego más corto de un grupo de videojuegos.
    En caso de que dos o más videojuegos tengan la misma duración, retorne el primero que encuentre.

    Parámetros
    ----------
    j1 : dict
        Diccionario que contiene la información del primer videojuego.
    j2 : dict
        Diccionario que contiene la información del segundo videojuego.
    j3 : dict
        Diccionario que contiene la información del tercer videojuego.
    j4 : dict
        Diccionario que contiene la información del cuarto videojuego.

    Retorno
    -------
    dict
        Diccionario que contiene la información del videojuego más corto.

    """
    if j1["duracion"] < j2["duracion"] and j1["duracion"] < j3["duracion"] and j1["duracion"] < j4["duracion"]:
        return j1
    elif j2["duracion"] < j1["duracion"] and j2["duracion"] < j3["duracion"] and j2["duracion"] < j4["duracion"]:
        return j2
    elif j3["duracion"] < j1["duracion"] and j3["duracion"] < j2["duracion"] and j3["duracion"] < j4["duracion"]:
        return j3
    elif j4["duracion"] < j1["duracion"] and j4["duracion"] < j2["duracion"] and j4["duracion"] < j3["duracion"]:
        return j4
    else:
        return None


def calcular_dias_necesarios_para_terminar_videojuego(juego: dict, horas_disponibilidad: int) -> int:
    """
    Calcula los días necesarios para terminar un videojuego.

    Parámetros
    ----------
    juego : dict
        Diccionario que contiene la información del videojuego.
    horas_disponibilidad : int
        Horas disponibles por día para jugar.

    Retorno
    -------
    int
        Número de días necesarios para terminar el videojuego.

    """
    h_to_m = (juego["duracion"] // 100) * 60
    print(h_to_m)
    min = juego["duracion"] % 100
    duracion_m = h_to_m + min
    horas_d_m = horas_disponibilidad * 60
    dias = duracion_m / horas_d_m

    if duracion_m / horas_d_m != 0 and duracion_m / horas_d_m > 1:
        dias += 1
    dias = int(round(dias))
    return dias


def mostrar_videojuegos_aptos_para_cierta_edad(j1: dict, j2: dict, j3: dict, j4: dict, edad: int) -> str:
    """
    Retorna una cadena con los títulos de los videojuegos aptos para una cierta edad.

    Parámetros
    ----------
    j1 : dict
        Diccionario que contiene la información del primer videojuego.
    j2 : dict
        Diccionario que contiene la información del segundo videojuego.
    j3 : dict
        Diccionario que contiene la información del tercer videojuego.
    j4 : dict
        Diccionario que contiene la información del cuarto videojuego.
    edad : int
        Edad a la que se desea verificar la aptitud de los videojuegos.

    Retorno
    -------
    str
        Cadena con los títulos de los videojuegos aptos para la edad especificada. 
        Si hay más de un juego apto, el formato será "X, Y, Z", con X, Y y Z siendo 
        los nombres de los juegos; En caso de haber un único resultado, el formato 
        será el nombre del juego "X". Además, en caso de no existir ningún juego apto,
        se debe responder con el siguiente mensaje "No hay ningún juego apto para 
        personas de X años”, donde X es la edad.

    """
    clasificacion = {"E": 0, "E10+": 10, "T": 13, "M": 17}
    juegos_aptos = ""
    c_j1 = j1["clasificacion_edad"]
    c_j2 = j2["clasificacion_edad"]
    c_j3 = j3["clasificacion_edad"]
    c_j4 = j4["clasificacion_edad"]

    if edad >= clasificacion[c_j1]:
        juegos_aptos += j1["titulo"] + ", "
    if edad >= clasificacion[c_j2]:
        juegos_aptos += j2["titulo"] + ", "
    if edad >= clasificacion[c_j3]:
        juegos_aptos += j3["titulo"] + ", "
    if edad >= clasificacion[c_j4]:
        juegos_aptos += j4["titulo"] + ", "
    if juegos_aptos.count(" ") == 3:
        j_aptos = juegos_aptos.replace(",", "")
        return j_aptos
    if juegos_aptos == "":
        return "No hay juegos aptos para personas de {0} años.".format(edad)
    return juegos_aptos


def determinar_puntaje_de_un_videojuego(juego: dict) -> float:
    """
    Calcula el puntaje de un videojuego en base a sus características.

    Parámetros:
    - juego (dict): Diccionario que contiene la información del videojuego.

    Retorna:
    - float: Puntaje del videojuego.

    puntos por:

    anio_de_lanzamiento -> mas reciente es mejor | 2020s -> 4 | 2010s -> 3 | 2000s -> 2 | 1990s -> 1 | 1980s -> 0
    generos -> solo suma el mejor genero | carreras o simulacion -> 4 | deportes -> 3 | accion, aventura o plataformas -> 2 | rol o estrategia -> 1
    rating -> mas rating mejor | divida el rating en 2 y restarle 1
    es_multijugador -> si es multijugador sume 5 puntos
    clasificacion_edad -> mas inclusivo mejor | E -> 4 | E10+ -> 3 | T -> 2 | M -> 1
    duracion -> quiero que dure lo justo | entre 1 y 3 hr -> 2 | entre 3 y 10 hr -> 4 | mas de 10 hr -> 2

    """
    final = 0

    if juego["anio_de_lanzamiento"] >= 2020:
        final += 4
    elif juego["anio_de_lanzamiento"] >= 2010:
        final += 3
    elif juego["anio_de_lanzamiento"] >= 2000:
        final += 2
    elif juego["anio_de_lanzamiento"] >= 1990:
        final += 1
    elif juego["anio_de_lanzamiento"] >= 1980:
        final += 0
    print(final)
    if "carreras" in juego["generos"] or "simulacion" in juego["generos"]:
        final += 4
    elif "deportes" in juego["generos"]:
        final += 3
    elif "acción" in juego["generos"] or "aventura" in juego["generos"] or "plataformas" in juego["generos"]:
        final += 2
    elif "rol" in juego["generos"] or "estrategia" in juego["generos"]:
        final += 1
    print(final)
    final += (juego["rating"] / 2) - 1
    print(final)
    if juego["es_multijugador"] == True:
        final += 5
    print(final)
    if juego["clasificacion_edad"] == "E":
        final += 4 
    elif juego["clasificacion_edad"] == "E10+":
        final += 3
    elif juego["clasificacion_edad"] == "T":
        final += 2
    elif juego["clasificacion_edad"] == "M":
        final += 1
    print(final)
    if juego["duracion"] >= 1 and juego["duracion"] <= 3:
        final += 2
    elif juego["duracion"] > 3 and juego["duracion"] <= 10:
        final += 4
    elif juego["duracion"] > 10:
        final += 2
    print(final)
    final = round(final, 2)
    return final


def contar_cantidad_de_juegos_de_un_genero(j1: dict, j2: dict, j3: dict, j4: dict, genero: str) -> int:
    """
    Cuenta la cantidad de juegos de un género específico.

    Parámetros:
    - j1 (dict): Diccionario que contiene la información del primer videojuego.
    - j2 (dict): Diccionario que contiene la información del segundo videojuego.
    - j3 (dict): Diccionario que contiene la información del tercer videojuego.
    - j4 (dict): Diccionario que contiene la información del cuarto videojuego.
    - genero (str): Género de los videojuegos a contar.

    Retorna:
    - int: Cantidad de videojuegos del género especificado.

    """
    cantidad = 0
    if genero in j1["generos"]:
        cantidad += 1
    if genero in j2["generos"]:
        cantidad += 1
    if genero in j3["generos"]:
        cantidad += 1  
    if genero in j4["generos"]:
        cantidad += 1

    return cantidad


def calcular_promedio_de_rating_de_los_videojuegos_de_un_genero(j1: dict, j2: dict, j3: dict, j4: dict, genero: str) -> float:
    """
    Calcula el promedio de rating de los videojuegos de un género específico.

    Parámetros:
    - j1 (dict): Diccionario que contiene la información del primer videojuego.
    - j2 (dict): Diccionario que contiene la información del segundo videojuego.
    - j3 (dict): Diccionario que contiene la información del tercer videojuego.
    - j4 (dict): Diccionario que contiene la información del cuarto videojuego.
    - genero (str): Género de los videojuegos a contar.

    Retorna:
    - float: Promedio de rating de los videojuegos del género especificado. Si no hay videojuegos del género,
    retorna -1.

    """
    p_j1 = j1["rating"]
    p_j2 = j2["rating"] 
    p_j3 = j3["rating"]
    p_j4 = j4["rating"]
    prom = 0
    d = 0
    if genero in j1["generos"]:
        prom += p_j1
        d += 1
    if genero in j2["generos"]:
        prom += p_j2
        d += 1
    if genero in j3["generos"]:
        prom += p_j3
        d += 1
    if genero in j4["generos"]:
        prom += p_j4
        d += 1
    if genero not in j1["generos"] and genero not in j2["generos"] and genero not in j3["generos"] and genero not in j4["generos"]:
        return -1
    final = prom / d
    return final
