import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Datos del problema
p1 = 128 / 200  # Proporción muestral de mujeres que toman café
p2 = 106 / 150  # Proporción muestral de hombres que toman café
n1 = 200  # Tamaño de la muestra de mujeres
n2 = 150  # Tamaño de la muestra de hombres
alpha = 0.05  # Nivel de significancia

# Cálculo de la proporción combinada
p = (p1 * n1 + p2 * n2) / (n1 + n2)

# Cálculo de la desviación estándar de la diferencia de proporciones
std_error = np.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))

# Cálculo del valor Z
Z = (p1 - p2) / std_error

# Cálculo del valor crítico Z (dos colas)
Z_critical = stats.norm.ppf(1 - alpha / 2)

# Gráfica de la distribución normal estándar
x = np.linspace(-3, 3, 400)
y = stats.norm.pdf(x, loc=0, scale=1)

plt.plot(x, y, 'b-', label='Distribución Z (Normal Estándar)')

# Calcular la región crítica (dos colas)
region_critica = x[(x < -Z_critical) | (x > Z_critical)]

# Rellenar la región crítica
plt.fill_between(region_critica, 0, stats.norm.pdf(region_critica, loc=0, scale=1), color='red', alpha=0.5, label='Región crítica')

# Marcar el valor calculado de Z
plt.axvline(Z, color='purple', linestyle='--', label=f'Valor calculado de Z = {Z:.2f}')

plt.legend()
plt.title('Prueba de Hipótesis con Distribución Z (Normal Estándar)')
plt.xlabel('Valor de Z')
plt.ylabel('Densidad de probabilidad')
plt.show()
