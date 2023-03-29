# CÓDIGO PROPIO #3.1
# Jan Pablo Castillo Sánchez MCI - A01731507

#PROBLEMA
#Potasio  0.25 A + 0.15 B          = 1.5
#Nitrato  0.45 A + 0.5  B + 0.75 C = 5
#Fosfato  0.3  A + 0.35 B + 0.25 C = 3

# No librerías
# Coeficientes de la matriz aumentada A:B
# indices_Py = [0   , 1   , 2 , 3  ,  4  , 5  , 6   , 7 , 8  , 9   , 10  , 11]
a_b          = [0.25, 0.15, 0 , 1.5, 0.45, 0.5, 0.75, 5 , 0.3, 0.35, 0.25, 3 ]
# posición   = [11  , 12  , 13, 14 , 21  , 22 , 23  , 24, 31 , 32  , 33  , 34]

# Calcular los determinantes del sistema
# Delta (matriz de coeficientes)
delta = a_b[0]*a_b[5]*a_b[10] + a_b[1]*a_b[6]*a_b[8] + \
        a_b[2]*a_b[4]*a_b[9] - a_b[2]*a_b[5]*a_b[8] - \
        a_b[0]*a_b[6]*a_b[9] - a_b[1]*a_b[4]*a_b[10]
# Delta1 (matriz de coeficientes, columna 1 = resultados)
delta1 = a_b[3]*a_b[5]*a_b[10] + a_b[1]*a_b[6]*a_b[11] + \
        a_b[2]*a_b[7]*a_b[9] - a_b[2]*a_b[5]*a_b[11] - \
        a_b[3]*a_b[6]*a_b[9] - a_b[1]*a_b[7]*a_b[10]
# Delta1 (matriz de coeficientes, columna 2 = resultados)
delta2 = a_b[0]*a_b[7]*a_b[10] + a_b[3]*a_b[6]*a_b[8] + \
        a_b[2]*a_b[4]*a_b[11] - a_b[2]*a_b[7]*a_b[8] - \
        a_b[0]*a_b[6]*a_b[11] - a_b[3]*a_b[4]*a_b[10]
# Delta1 (matriz de coeficientes, columna 3 = resultados)
delta3 = a_b[0]*a_b[5]*a_b[11] + a_b[1]*a_b[7]*a_b[8] + \
        a_b[3]*a_b[4]*a_b[9] - a_b[3]*a_b[5]*a_b[8] - \
        a_b[0]*a_b[7]*a_b[9] - a_b[1]*a_b[4]*a_b[11]

print("Resolver sistema no homogéneo por Regla de Cramer")
# Imprimir las Deltas del sistema (redondeo de 4 decimales)
print("Delta:", round(delta, 4), "\t","Delta1:", round(delta1, 4),
      "\t","Delta2:", round(delta2, 4), "\t","Delta3:", round(delta3, 4))

# Imprimir el resultado de cada Delta
print("Soluciones:")
print("Delta A = Delta1/Delta = Fertilizante A = ",
      round(delta1/delta, 4), "Toneladas de potasio")
print("Delta B = Delta2/Delta = Fertilizante B = ",
      round(delta2/delta, 4), "Toneladas de nitrato")
print("Delta C = Delta3/Delta = Fertilizante C = ",
      round(delta3/delta, 4), "Toneladas de fosfato")
