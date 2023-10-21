import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Datos del problema
X = 86  # Media muestral
mu = 80  # Media poblacional bajo H0
s = 16  # Desviación estándar de la muestra
n = 100  # Tamaño de la muestra
alpha = 0.05  # Nivel de significancia

# Cálculo de Z
Z = (X - mu) / (s / np.sqrt(n))

# Gráfica de la distribución normal Z
x = np.linspace(-5, 5, 400)
y = stats.norm.pdf(x, 0, 1)

plt.plot(x, y, 'b-', label='Distribución normal Z')

# Calcular los valores críticos
z_critical = stats.norm.ppf(1 - alpha / 2)
lower_critical = -z_critical
upper_critical = z_critical

# Rellenar la región crítica
plt.fill_between(x, 0, y, where=(x <= lower_critical) | (x >= upper_critical), color='red', alpha=0.5, label='Región crítica')

# Marcar el valor calculado de Z
plt.axvline(Z, color='purple', linestyle='--', label=f'Valor calculado de Z = {Z:.2f}')

plt.legend()
plt.title('Prueba de Hipótesis con Distribución Normal Z')
plt.xlabel('Valor de Z')
plt.ylabel('Densidad de probabilidad')
plt.show()
