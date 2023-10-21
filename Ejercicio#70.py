import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Datos del problema
n1 = 120  # Tamaño de la muestra de la primera fábrica
n2 = 120  # Tamaño de la muestra de la segunda fábrica
p1 = 12 / n1  # Proporción muestral de ausentismo en la primera fábrica
p2 = 16 / n2  # Proporción muestral de ausentismo en la segunda fábrica
alpha = 0.05  # Nivel de significancia

# Proporción combinada bajo la hipótesis nula (no hay diferencia)
p_combined = (p1 * n1 + p2 * n2) / (n1 + n2)

# Error estándar de la diferencia
SE = np.sqrt(p_combined * (1 - p_combined) * (1 / n1 + 1 / n2))

# Estadístico Z
Z = (p1 - p2) / SE

# Valor crítico (unilateral, ya que estamos comparando si p2 es mayor que p1)
critical_value = stats.norm.ppf(1 - alpha)

# Rango para graficar
x = np.linspace(-3, 3, 1000)

# Crear la figura
plt.figure(figsize=(10, 6))

# Dibujar la distribución Z
plt.plot(x, stats.norm.pdf(x, 0, 1), label="Distribución Z (bajo H0)")

# Sombrear la región crítica
plt.fill_between(x, 0, stats.norm.pdf(x, 0, 1), where=(x > critical_value), color='red', alpha=0.5, label="Región Crítica")

# Línea vertical para el estadístico Z
plt.axvline(Z, color='green', linestyle='--', lw=2, label="Estadístico Z")

# Etiquetas y leyenda
plt.xlabel("Estadístico Z")
plt.ylabel("Densidad de Probabilidad")
plt.title("Prueba de Hipótesis para Diferencia en el Ausentismo")
plt.legend()

# Mostrar la gráfica
plt.show()
