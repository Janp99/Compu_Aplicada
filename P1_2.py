# CÓDIGO PROPIO #2
# Jan Pablo Castillo Sánchez MCI - A01731507

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import pandas as pd

# Leer los datos
datos = pd.read_csv("datos_A01731507.txt", delimiter='\t')

# Variables Generales
e = datos.iloc[:,0] # Estatura General
tc = datos.iloc[:,1] # Talla de Calzado General

# Calcular la Media y Desviación Estándar
m_e = np.mean(e)
de_e = np.std(e)
m_tc = np.mean(tc)
de_tc = np.std(tc)

# Obtener la función Gaussiana
# Definir el rango del eje x
ejex_e = np.linspace(e.min(), e.max(), 100)
ejex_tc = np.linspace(tc.min(), tc.max(), 100)
# Calcular la curva de distribución normal
distn_e = norm.pdf(ejex_e, m_e, de_e)
distn_tc = norm.pdf(ejex_tc, m_tc, de_tc)

# Hallar la probabilidad de la primera desviación estándar
p_e = np.sum((e > m_e - de_e) & (e < m_e + de_e))/len(e)
p_tc = np.sum((tc > m_tc - de_tc) & (tc < m_tc + de_tc))/len(tc)

# Imprimir la media, desviación estándar y probabilidad de cada clase
print("Estatura:")
print("Media(\u03BC):", round(m_e, 4), "\t",
      "Desviación Estandar(\u03C3):", round(de_e, 4), "\t",)
print("Probabilidad:", round(p_e, 4))
print("Talla de Calzado:")
print("Media(\u03BC):", round(m_tc, 4), "\t",
      "Desviación Estandar(\u03C3):", round(de_tc, 4), "\t",)
print("Probabilidad:", round(p_tc, 4))

print("\n", "Aproximaciones lineales")
# Determinar la aproximación lineal de la relación estatura / talla de calzado
grupos = ["General","Masculino", "Femenino"] # Etiquetas
# Iterar a través de cada etiqueta y calcular la aproximación lineal
for g in grupos:
    if g == 'General': # Rutina Grupo General
        x_e = e # var dependiente
        y_tc = tc # var independiente
        print("Aproximación Grupo", g, ":")
    else: # Rutina Subgrupos
        # Filtrar los datos según el sexo
        datos_sx = datos[datos.iloc[:, 2] == g]
        x_e = datos_sx.iloc[:, 0] # var dependiente
        y_tc = datos_sx.iloc[:, 1] # var independiente
        print("Aproximación Subgrupo", g, ":")
    # Calcular los coeficientes de la aproximación lineal
    coef = np.polyfit(x_e, y_tc, 1)
    a = coef[0] # Pendiente
    b = coef[1] # Ordenada al orígen
    # Imprimir la aproximación lineal
    print("y =", round(a, 4), "x +", round(b, 4))

# Graficar histogramas y funciones gaussianas
w, graf = plt.subplots(2, 2, figsize=(12,6))
graf[0,0].hist(datos.iloc[:,0], bins=20, density=True)
graf[0,0].plot(ejex_e, distn_e, label='Curva de distribución normal')
graf[0,0].legend()
graf[0,0].set_title("Gráfico de Estatura")
graf[0,0].set_xlabel("Altura (Cm)")
graf[0,0].set_ylabel("f Densidad de probabilidad")
graf[0,1].hist(datos.iloc[:,1], bins=20, density=True)
graf[0,1].plot(ejex_tc, distn_tc, label='Curva de distribución normal')
graf[0,1].legend()
graf[0,1].set_title("Gráfico de Talla de Calzado")
graf[0,1].set_xlabel("Talla (Cm)")
graf[0,1].set_ylabel("f Densidad de probabilidad")
graf[1,0].axis("off")
graf[1,1].axis("off")
plt.tight_layout()
plt.show()