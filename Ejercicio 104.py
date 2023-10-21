import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Datos del problema
nA = 20  # Tamaño de la muestra de la solución A
nB = 12  # Tamaño de la muestra de la solución B
xA = 7.5  # Media muestral del pH de la solución A
xB = 7.4  # Media muestral del pH de la solución B
sA = 0.24  # Desviación estándar de la muestra de A
sB = 0.30  # Desviación estándar de la muestra de B
alpha = 0.05  # Nivel de significancia

# Cálculo del valor t
SE = np.sqrt(((sA**2) / nA) + ((sB**2) / nB))
t = (xA - xB) / SE

# Grados de libertad utilizando la fórmula de Welch-Satterthwaite
df = ((sA**2 / nA) + (sB**2 / nB))**2 / (((sA**2 / nA)**2 / (nA - 1)) + ((sB**2 / nB)**2 / (nB - 1)))

# Valor crítico t (bilateral)
critical_value = stats.t.ppf(1 - alpha / 2, df)

# Rango para graficar
x = np.linspace(-4, 4, 1000)

# Crear la figura
plt.figure(figsize=(10, 6))

# Dibujar la distribución t
plt.plot(x, stats.t.pdf(x, df), label="Distribución t (bajo H0)")

# Sombrear la región crítica
plt.fill_between(x, 0, stats.t.pdf(x, df), where=(x > critical_value) | (x < -critical_value), color='red', alpha=0.5, label="Región Crítica")

# Línea vertical para el estadístico t
plt.axvline(t, color='green', linestyle='--', lw=2, label="Estadístico t")

# Etiquetas y leyenda
plt.xlabel("Estadístico t")
plt.ylabel("Densidad de Probabilidad")
plt.title("Prueba de Hipótesis para Diferencia en el pH")
plt.legend()

# Mostrar la gráfica
plt.show()
