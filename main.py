from sections_utils import analizar_rectangulo
from analysis import (
    momento_maximo_carga_central,
    esfuerzo_flexion,
    modulo_seccion
)


# --------------------------------------------------
# DATOS DE LA SECCIÓN
# --------------------------------------------------

ancho = 300       # mm
alto = 500        # mm

seccion = analizar_rectangulo(ancho, alto)


# --------------------------------------------------
# DATOS DE LA VIGA
# --------------------------------------------------

longitud = 6      # m
carga = 20        # kN


# --------------------------------------------------
# ANÁLISIS ESTRUCTURAL
# --------------------------------------------------

momento = momento_maximo_carga_central(carga, longitud)

distancia_fibra = alto / 2

esfuerzo = esfuerzo_flexion(
    momento,
    seccion["inercia_x"],
    distancia_fibra
)

modulo = modulo_seccion(
    seccion["inercia_x"],
    distancia_fibra
)


# --------------------------------------------------
# RESULTADOS
# --------------------------------------------------

print()
print("==============================================")
print("       PYCIVIL SECTION ANALYZER")
print("==============================================")

print()
print("PROPIEDADES DE LA SECCIÓN")
print("----------------------------------------------")
print(f"Ancho:              {ancho:.0f} mm")
print(f"Alto:               {alto:.0f} mm")
print(f"Área:               {seccion['area']:.2f} mm²")
print(f"Centroide X:        {seccion['centroide_x']:.2f} mm")
print(f"Centroide Y:        {seccion['centroide_y']:.2f} mm")
print(f"Ixx:                {seccion['inercia_x']:.2f} mm⁴")
print(f"Iyy:                {seccion['inercia_y']:.2f} mm⁴")

print()
print("ANÁLISIS DE LA VIGA")
print("----------------------------------------------")
print(f"Longitud:           {longitud:.2f} m")
print(f"Carga central:      {carga:.2f} kN")
print(f"Momento máximo:     {momento:.2f} kN·m")
print(f"Distancia extrema:  {distancia_fibra:.2f} mm")
print(f"Módulo de sección:  {modulo:.2f} mm³")
print(f"Esfuerzo máximo:    {esfuerzo:.2f} MPa")

print()
print("==============================================")