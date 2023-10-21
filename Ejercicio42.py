import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Datos del problema
P = 0.2222  # Proporción muestral de estudiantes que habilitan asignaturas
p0 = 0.25  # Proporción poblacional bajo H0
n = 36  # Tamaño de la muestra
alpha = 0.05  # Nivel de significancia

# Cálculo de Z
Z = (P - p0) / np.sqrt((p0 * (1 - p0)) / n)

# Gráfica de la distribución normal Z
x = np.linspace(-3, 3, 400)
y = stats.norm.pdf(x, 0, 1)

plt.plot(x, y, 'b-', label='Distribución normal Z')

# Calcular el valor crítico Z (unilateral a la izquierda)
z_critical = stats.norm.ppf(alpha)
lower_critical = -z_critical

# Rellenar la región crítica
plt.fill_between(x, 0, y, where=x <= lower_critical, color='red', alpha=0.5, label='Región crítica')

# Marcar el valor calculado de Z
plt.axvline(Z, color='purple', linestyle='--', label=f'Valor calculado de Z = {Z:.2f}')

plt.legend()
plt.title('Prueba de Hipótesis con Distribución Normal Z')
plt.xlabel('Valor de Z')
plt.ylabel('Densidad de probabilidad')
plt.show()
