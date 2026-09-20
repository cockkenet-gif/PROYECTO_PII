# PyCivil Section Analyzer

## Descripción

PyCivil Section Analyzer es una herramienta desarrollada en Python para analizar y comparar secciones rectangulares utilizadas en elementos estructurales tipo viga.

El proyecto utiliza la biblioteca `pysections` como motor para obtener las propiedades geométricas de las secciones y agrega una aplicación orientada al análisis de flexión de vigas.

A partir de una sección y de las condiciones de carga de una viga, el programa calcula el momento flector máximo, el módulo de sección y el esfuerzo máximo de flexión. También permite comparar diferentes alternativas de sección y visualizar los resultados mediante gráficos.

---

## Problema que se busca resolver

En el análisis preliminar de elementos estructurales es necesario conocer cómo las dimensiones de una sección transversal influyen en su comportamiento frente a cargas.

El proyecto busca facilitar una comparación sencilla entre diferentes secciones rectangulares sometidas a las mismas condiciones de carga, permitiendo observar cómo cambian sus propiedades geométricas y el esfuerzo de flexión.

---

## Nuevo uso de pysections

La biblioteca `pysections` está orientada al cálculo de propiedades geométricas de secciones transversales.

En este proyecto se utiliza esa capacidad como base para desarrollar una aplicación adicional:

```text
Pysections
     ↓
Propiedades geométricas
     ↓
Análisis de flexión de vigas
     ↓
Comparación de secciones
     ↓
Visualización de resultados

El aporte desarrollado en este proyecto consiste en utilizar las propiedades calculadas por pysections dentro de un análisis simplificado de una viga simplemente apoyada con una carga puntual en el centro.

De esta manera, la biblioteca no se utiliza únicamente para obtener propiedades geométricas, sino como parte de una herramienta de análisis estructural preliminar.

Funcionalidades

El programa permite:

Analizar secciones rectangulares.
Calcular el área de la sección.
Obtener el centroide.
Obtener los momentos de inercia Ixx e Iyy.
Calcular el momento máximo de una viga simplemente apoyada con carga central.
Calcular el módulo de sección.
Calcular el esfuerzo máximo de flexión.
Comparar dos secciones sometidas a las mismas condiciones de carga.
Generar una gráfica comparativa de los esfuerzos máximos.
Modelo de análisis

Para el análisis se considera una viga simplemente apoyada con una carga puntual ubicada en el centro.

El momento máximo se calcula mediante:

$$ M_{max} = \frac{PL}{4} $$

donde:

P = carga aplicada.
L = longitud de la viga.

El esfuerzo máximo de flexión se calcula mediante:

$$ \sigma_{max} = \frac{Mc}{I} $$

donde:

M = momento flector.
c = distancia desde el eje neutro hasta la fibra extrema.
I = momento de inercia de la sección.

El módulo de sección se calcula mediante:

$$ S = \frac{I}{c} $$
Ejemplo

Para una viga de:

Longitud: 6 m
Carga puntual central: 20 kN

se comparan las siguientes secciones:

Sección	Dimensiones
A	300 × 500 mm
B	300 × 600 mm

Resultados obtenidos:

Propiedad	Sección A	Sección B
Área	150000 mm²	180000 mm²
Ixx	3125000000 mm⁴	5400000000 mm⁴
Módulo de sección	12500000 mm³	18000000 mm³
Esfuerzo máximo	2.40 MPa	1.67 MPa

La comparación permite observar la influencia de las dimensiones de la sección sobre sus propiedades geométricas y el esfuerzo producido por la misma condición de carga.

Requisitos

El proyecto requiere:

Python 3
NumPy
Matplotlib

Las dependencias están especificadas en:

requirements.txt
Instalación

Clonar el repositorio:

git clone https://github.com/cockkenet-gif/PROYECTO_PII.git

Ingresar al directorio:

cd PROYECTO_PII

Crear un entorno virtual:

python -m venv .venv
Windows

Activar el entorno virtual:

.venv\Scripts\activate

Instalar las dependencias:

pip install -r requirements.txt
Ejecución

Con el entorno virtual activado, ejecutar:

python main.py

El programa mostrará los resultados del análisis en la terminal y generará una gráfica comparativa de los esfuerzos máximos.

Estructura del proyecto
PROYECTO_PII/
│
├── main.py
├── analysis.py
├── sections_utils.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── pysections/
    ├── sections.py
    ├── README.org
    └── LICENSE
Descripción de los archivos

main.py

Archivo principal del programa. Define las condiciones de la viga, analiza las secciones, muestra los resultados y genera la gráfica comparativa.

analysis.py

Contiene las funciones desarrolladas para el análisis estructural de la viga, incluyendo momento máximo, esfuerzo de flexión y módulo de sección.

sections_utils.py

Conecta el proyecto con la biblioteca pysections y utiliza sus métodos para obtener las propiedades geométricas de las secciones.

pysections/

Contiene la biblioteca utilizada como base para el cálculo de propiedades geométricas de las secciones.

requirements.txt

Contiene las dependencias necesarias para ejecutar el proyecto.

.gitignore

Evita que archivos temporales y el entorno virtual sean incluidos en el repositorio.

Librería utilizada

Este proyecto utiliza pysections, una biblioteca desarrollada para el cálculo de propiedades geométricas de secciones transversales.

La biblioteca original se mantiene separada de los módulos desarrollados específicamente para este proyecto.

Alcance

El análisis implementado corresponde a un modelo simplificado para fines académicos.

El programa no pretende reemplazar un software de diseño estructural ni realizar un diseño estructural completo. Su objetivo es demostrar una aplicación adicional de una biblioteca de cálculo de propiedades geométricas dentro de un problema relacionado con la ingeniería civil.

Autor

Proyecto académico desarrollado por:

Kenet Cock

Ingeniería Civil