# CÓDIGO PROPIO #1
# Jan Pablo Castillo Sánchez MCI - A01731507

import numpy as np

# KEYWORDS:
# MNPC - Matriz de Números Primos Consecutivos
# MDS - Matriz Diagonal Superior

def matriz_numeros_primos_consecutivos(m):
    n_primos = [] # Inicializar lista "n_primos"
    n = 2 # 2 = Primer número primo
    # Hacer "n_primos" de tamaño mxm (dimensión de la matriz).
    while len(n_primos) < m*m:
        residuo = True
        # Evaluar cada "n" hasta llenar m*m veces la lista "n_primos"
        for i in range(2, n):
            if n % i == 0: # Residuo de n/i
                residuo = False # "n" actual no es un número primo
                break
        if residuo: # "n" actual es un número primo
            n_primos.append(n) # Añadir la "n" actual a "n_primos"
        n += 1 # Actualizar posible número primo
    # Llamar función para construir la MNPC
    return armar_matriz(n_primos, dim)

def armar_matriz(n_primos, m):
    mat = np.zeros((m,m), dtype=int) # Matriz de ceros mxm
    idx = 0 # Inicializar índice "idx"
    # A partir de "n_primos" y "m" construir la matriz A
    for i in range(m):
        for j in range(m):
            # Sobreescribir "mat" con "n_primos"
            mat[i][j] = str(n_primos[idx])
            # Actualizar el índice "idx" de "n_primos"
            idx += 1
    # Imprimir la matriz A (MNPC)
    print("A =")
    for f in mat:
        # Imprimir el arreglo "mat" como str
        print("\t".join([str(int(e)) for e in f]))
    # Llamar función para evaluar los elementos de la MDS
    return matriz_diagonal_superior(mat)

def matriz_diagonal_superior(mat):
    elementos_mds = [] # Inicializar lista "elementos_mds"
    suma = 0 # Inicializar variable "suma"
    # Escanear los elementos de la MDS
    for i in range(dim):
        for j in range(i, dim):
            # Juntar los elementos de la MDS en "elementos_mds"
            elementos_mds.append(mat[i][j])
            # Acumular el resultado de la suma de los elementos
            suma += mat[i][j]
    # Retornar la lista de elementos de la MDS y el resultado de su suma
    return elementos_mds, suma

# Establecer la dimensión "m" de la matriz A (mxm)
while True:
    dim = int(input("Introduzca la dimensión de la matriz A (valor de m): "))
    # Condicionar que la dimensión sea mayor o igual a 3
    if dim < 3:
        print("Introduzca otro número entero (mayor o igual a 3)")
    else:
        break

# Obtener la lista de elementos de la MDS y la suma sus elementos
elementos_mds, suma = matriz_numeros_primos_consecutivos(dim)

# Imprimir la lista de elementos de la MDS
print("Los elementos de la matriz diagonal superior son: ", elementos_mds, "\t")
# Imprimir la suma de los elementos de la MDS
print("La suma de los elementos es: ", suma)