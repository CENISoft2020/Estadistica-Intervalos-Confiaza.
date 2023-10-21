import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Datos del problema
x_diurno = 94.3  # Media muestral del turno diurno
x_nocturno = 89.7  # Media muestral del turno nocturno
s_diurno = 14  # Desviación estándar del turno diurno
s_nocturno = 17  # Desviación estándar del turno nocturno
n_diurno = 80  # Tamaño de la muestra del turno diurno
n_nocturno = 60  # Tamaño de la muestra del turno nocturno
alpha = 0.05  # Nivel de significancia

# Cálculo de la diferencia de medias
diferencia_medias = x_diurno - x_nocturno

# Cálculo del error estándar de la diferencia
error_estandar_diferencia = np.sqrt((s_diurno**2 / n_diurno) + (s_nocturno**2 / n_nocturno))

# Cálculo de los grados de libertad
grados_libertad = ((s_diurno**2 / n_diurno + s_nocturno**2 / n_nocturno)**2) / ((1 / (n_diurno - 1)) * (s_diurno**4 / n_diurno**2) + (1 / (n_nocturno - 1)) * (s_nocturno**4 / n_nocturno**2))

# Cálculo del valor crítico t (dos colas)
t_critical = stats.t.ppf(1 - alpha / 2, df=grados_libertad)

# Gráfica de la distribución t de Student
x = np.linspace(-3, 3, 400)
y = stats.t.pdf(x, df=grados_libertad)

plt.plot(x, y, 'b-', label='Distribución t de Student')

# Calcular la región crítica (dos colas)
region_critica = x[(x < -t_critical) | (x > t_critical)]

# Rellenar la región crítica
plt.fill_between(region_critica, 0, stats.t.pdf(region_critica, df=grados_libertad), color='red', alpha=0.5, label='Región crítica')

# Marcar el valor calculado de t
plt.axvline(diferencia_medias / error_estandar_diferencia, color='purple', linestyle='--', label=f'Valor calculado de t = {diferencia_medias / error_estandar_diferencia:.2f}')

plt.legend()
plt.title('Prueba de Hipótesis con Distribución t de Student')
plt.xlabel('Valor de t')
plt.ylabel('Densidad de probabilidad')
plt.show()
