from sections_utils import analizar_rectangulo
from analysis import (
    momento_maximo_carga_central,
    esfuerzo_flexion,
    modulo_seccion
)


# --------------------------------------------------
# DATOS DE LA VIGA
# --------------------------------------------------

longitud = 6       # m
carga = 20         # kN


# --------------------------------------------------
# DEFINICIÓN DE LAS SECCIONES
# --------------------------------------------------

seccion_a = analizar_rectangulo(300, 500)
seccion_b = analizar_rectangulo(300, 600)


# --------------------------------------------------
# MOMENTO MÁXIMO DE LA VIGA
# --------------------------------------------------

momento = momento_maximo_carga_central(carga, longitud)


# --------------------------------------------------
# FUNCIÓN PARA ANALIZAR CADA SECCIÓN
# --------------------------------------------------

def calcular_resultados(seccion, alto):
    distancia_fibra = alto / 2

    modulo = modulo_seccion(
        seccion["inercia_x"],
        distancia_fibra
    )

    esfuerzo = esfuerzo_flexion(
        momento,
        seccion["inercia_x"],
        distancia_fibra
    )

    return modulo, esfuerzo


modulo_a, esfuerzo_a = calcular_resultados(seccion_a, 500)
modulo_b, esfuerzo_b = calcular_resultados(seccion_b, 600)


# --------------------------------------------------
# RESULTADOS
# --------------------------------------------------

print()
print("======================================================")
print("             PYCIVIL SECTION ANALYZER")
print("======================================================")

print()
print("DATOS DE LA VIGA")
print("------------------------------------------------------")
print(f"Longitud:             {longitud:.2f} m")
print(f"Carga central:        {carga:.2f} kN")
print(f"Momento máximo:       {momento:.2f} kN·m")


print()
print("COMPARACIÓN DE SECCIONES")
print("------------------------------------------------------")

print()
print("SECCIÓN A")
print(f"Dimensiones:          300 x 500 mm")
print(f"Área:                 {seccion_a['area']:.2f} mm²")
print(f"Ixx:                  {seccion_a['inercia_x']:.2f} mm⁴")
print(f"Módulo de sección:    {modulo_a:.2f} mm³")
print(f"Esfuerzo máximo:      {esfuerzo_a:.2f} MPa")


print()
print("SECCIÓN B")
print(f"Dimensiones:          300 x 600 mm")
print(f"Área:                 {seccion_b['area']:.2f} mm²")
print(f"Ixx:                  {seccion_b['inercia_x']:.2f} mm⁴")
print(f"Módulo de sección:    {modulo_b:.2f} mm³")
print(f"Esfuerzo máximo:      {esfuerzo_b:.2f} MPa")


print()
print("======================================================")
import matplotlib.pyplot as plt


# --------------------------------------------------
# GRÁFICA COMPARATIVA
# --------------------------------------------------

secciones = ["Sección A\n300 × 500 mm", "Sección B\n300 × 600 mm"]
esfuerzos = [esfuerzo_a, esfuerzo_b]

plt.figure(figsize=(8, 5))

plt.bar(secciones, esfuerzos)

plt.title("Comparación del esfuerzo máximo de flexión")
plt.ylabel("Esfuerzo máximo (MPa)")
plt.xlabel("Sección")

for i, valor in enumerate(esfuerzos):
    plt.text(i, valor, f"{valor:.2f} MPa", ha="center", va="bottom")

plt.tight_layout()
plt.show()