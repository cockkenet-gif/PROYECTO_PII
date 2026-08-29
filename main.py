import numpy as np

def area(points):
    n = len(points)
    x = points[:, 0]
    y = points[:, 1]

    sumx = 0
    sumy = 0

    for i in range(n):
        sumx = sumx + x[i] * y[(i + 1) % n]
        sumy = sumy + y[i] * x[(i + 1) % n]
    return 1 / 2 * (sumx - sumy)

coords = np.array([[0,0], [1,0], [1,1], [0,1]])
print(area(coords))