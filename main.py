import sys
import numpy as np

sys.path.append("pysections")

from sections import Section


coords = np.array([
    [0, 0],
    [1, 0],
    [1, 1],
    [0, 1]
])

section = Section()

print("Área:", section._A(coords))