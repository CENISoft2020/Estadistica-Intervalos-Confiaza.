import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Datos del problema
X = 68  # Media muestral
mu = 64  # Media poblacional bajo H0
sigma = 8  # Desviación estándar de la población
n = 64  # Tamaño de la muestra
alpha = 0.05  # Nivel de significancia

# Cálculo de Z
Z = (X - mu) / (sigma / np.sqrt(n))

# Gráfica de la distribución normal estándar
x = np.linspace(-5, 5, 400)
y = norm.pdf(x, 0, 1)

plt.plot(x, y, 'b-', label='Distribución normal estándar')

# Calcular los valores críticos
z_critical = norm.ppf(1 - alpha / 2)
lower_critical = -z_critical
upper_critical = z_critical

# Rellenar la región crítica
plt.fill_between(x, 0, y, where=(x <= lower_critical) | (x >= upper_critical), color='red', alpha=0.5, label='Región crítica')

# Marcar los valores calculados de Z
plt.axvline(Z, color='purple', linestyle='--', label=f'Valor calculado de Z = {Z:.2f}')

plt.legend()
plt.title('Prueba de Hipótesis con Distribución Normal Z')
plt.xlabel('Valor de Z')
plt.ylabel('Densidad de probabilidad')
plt.show()
