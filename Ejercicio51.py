import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Datos del problema
n_A = 20  # Tamaño de la muestra de la Facultad A
n_B = 28  # Tamaño de la muestra de la Facultad B
X_A = 3.32  # Media muestral de la Facultad A
X_B = 3.50  # Media muestral de la Facultad B
s_A = 0.7  # Desviación estándar de la Facultad A
s_B = 0.86  # Desviación estándar de la Facultad B
alpha = 0.05  # Nivel de significancia

# Cálculo de la diferencia de medias
diferencia_medias = X_A - X_B

# Cálculo del error estándar de la diferencia
error_estandar_diferencia = np.sqrt((s_A**2 / n_A) + (s_B**2 / n_B))

# Cálculo de los grados de libertad
grados_libertad = n_A + n_B - 2

# Cálculo del valor crítico t (una cola izquierda)
t_critical = stats.t.ppf(alpha, df=grados_libertad)

# Gráfica de la distribución t de Student
x = np.linspace(-3, 3, 400)
y = stats.t.pdf(x, df=grados_libertad)

plt.plot(x, y, 'b-', label='Distribución t de Student')

# Calcular la región crítica (una cola izquierda)
region_critica = x[x < -t_critical]

# Rellenar la región crítica
plt.fill_between(region_critica, 0, stats.t.pdf(region_critica, df=grados_libertad), color='red', alpha=0.5, label='Región crítica')

# Marcar el valor calculado de t
plt.axvline(diferencia_medias / error_estandar_diferencia, color='purple', linestyle='--', label=f'Valor calculado de t = {diferencia_medias / error_estandar_diferencia:.2f}')

plt.legend()
plt.title('Prueba de Hipótesis con Distribución t de Student')
plt.xlabel('Valor de t')
plt.ylabel('Densidad de probabilidad')
plt.show()
