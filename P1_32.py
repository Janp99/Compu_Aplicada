# CÓDIGO NumPy #3.2
# Jan Pablo Castillo Sánchez MCI - A01731507

import numpy as np

# Coeficientes de la matriz aumentada A:B (3x4)
a_b = np.array([0.25, 0.15, 0, 1.5, 0.45, 0.5, 0.75, 5, 0.3, 0.35, 0.25, 3]).reshape(3, 4)

d = len(a_b) # Número de incógnitas, tamaño de matriz
red = 4 # Número de ciflas para redondeo

# Calcular los determinantes del sistema

# Delta
# Construcción de matriz de coeficientes
# Calcular el determinante de la de matriz de coeficientes
delta = np.linalg.det(a_b[:, :d])

# Delta 1, 2, 3
# Construcción de matrices Delta
res = np.zeros(d) # Inicializar matriz 3x3 de ceros "res"
det_dn = [] # Inicializar lista "det_dn"
for n in range(d):
    delta_n = np.zeros((d,d))
    for j in range(d):
        # Construcción de matriz de coeficientes
        if j == n:
            # Reemplazar la columna en turno "n" por la columna de resultados
            delta_n[:,j] = a_b[:,d]
        else:
            delta_n[:,j] = a_b[:,j]
    # Calcular el determinante de "delta_n"
    det_delta_n = np.linalg.det(delta_n)
    # Añadir cada determinante "det_delta_n" a "det_dn"
    det_dn.append(det_delta_n)
    # Calcular Delta n
    res[n] = det_delta_n / delta

print("Resolver sistema no homogéneo por Regla de Cramer")
# Imprimir las Deltas del sistema (redondeo de 4 decimales)
print("Delta:", round(delta, red), "\t","Delta1:", round(det_dn[0], red),
      "\t","Delta2:", round(det_dn[1], red), "\t","Delta3:", round(det_dn[2], red))

# Imprimir el resultado de cada Delta
print("Soluciones:")
idx = 0 # Inicializar índice auxiliar "idx"
# Lista de fertilizantes y clases de suministro
fert_sum = ["A", "B", "C", "de potasio", "de nitrato", "de fosfato"]
# Imprimir el resultado de cada Delta
for ton in res:
    print("Delta", fert_sum[idx], " = Delta1/Delta = Fertilizante",
          fert_sum[idx], "=", idx+1, ":", round(ton, red), "Toneladas", fert_sum[idx+3])
    # Actualizar el índice "idx" de "fert_sum"
    idx += 1