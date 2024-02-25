import numpy as np
from scipy.optimize import linprog

# Koeffizientenmatrix der Ungleichungen
A = np.array([[1, 1, -2, -2],
              [0, -1, 0, -1],
              [0, -1, -1, 3]])

# Rechte Seite der Ungleichungen
b = np.array([2, 3, 4])

# Koeffizienten der Zielfunktion
c = np.array([1, 2, -3, 1])

# Grenzen für Variablen (x1, x2, x3, x4)
x0_bounds = (0, None)
x1_bounds = (0, None)
x2_bounds = (0, None)
x3_bounds = (0, None)

# lineares Programm lösen
res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds, x2_bounds, x3_bounds], method='highs')

# Ergebnisse ausgeben
print("Status:", res.message)
print("Optimale Werte der Variablen:", res.x)
print("Optimaler Wert der Zielfunktion:", res.fun)