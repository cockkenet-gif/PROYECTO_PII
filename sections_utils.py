import sys
import numpy as np

sys.path.append("pysections")

from sections import Section


def analizar_rectangulo(ancho_mm, alto_mm):
    """
    Analiza una sección rectangular utilizando pysections.

    Parámetros:
        ancho_mm: ancho de la sección en milímetros.
        alto_mm: altura de la sección en milímetros.

    Retorna:
        Diccionario con las propiedades geométricas.
    """

    puntos = np.array([
        [0, 0],
        [ancho_mm, 0],
        [ancho_mm, alto_mm],
        [0, alto_mm]
    ])

    seccion = Section()

    area = seccion._A(puntos)
    centroide_x = seccion._x(puntos)
    centroide_y = seccion._y(puntos)
    inercia_x = seccion._Ixx(puntos)
    inercia_y = seccion._Iyy(puntos)

    return {
        "area": area,
        "centroide_x": centroide_x,
        "centroide_y": centroide_y,
        "inercia_x": inercia_x,
        "inercia_y": inercia_y,
        "altura": alto_mm
    }