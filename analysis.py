def momento_maximo_carga_central(carga_kn, longitud_m):
    """
    Calcula el momento flector máximo de una viga simplemente apoyada
    con una carga puntual ubicada en el centro.

    Parámetros:
        carga_kn: carga aplicada en kN
        longitud_m: longitud de la viga en metros

    Retorna:
        Momento máximo en kN·m
    """

    momento = (carga_kn * longitud_m) / 4

    return momento


def esfuerzo_flexion(moment_kn_m, inercia_mm4, distancia_mm):
    """
    Calcula el esfuerzo máximo de flexión.

    Parámetros:
        moment_kn_m: momento flector en kN·m
        inercia_mm4: momento de inercia en mm^4
        distancia_mm: distancia desde el eje neutro hasta la fibra extrema en mm

    Retorna:
        Esfuerzo máximo en MPa
    """

    # Conversión de kN·m a N·mm
    moment_n_mm = moment_kn_m * 1_000_000

    esfuerzo = (moment_n_mm * distancia_mm) / inercia_mm4

    return esfuerzo


def modulo_seccion(inercia_mm4, distancia_mm):
    """
    Calcula el módulo resistente de la sección.

    Parámetros:
        inercia_mm4: momento de inercia en mm^4
        distancia_mm: distancia máxima al eje neutro en mm

    Retorna:
        Módulo de sección en mm^3
    """

    return inercia_mm4 / distancia_mm