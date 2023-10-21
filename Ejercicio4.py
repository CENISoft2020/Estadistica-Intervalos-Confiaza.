import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Datos del problema
X = 27.3  # Media muestral
mu = 25  # Media poblacional bajo H0
s = 6.1  # Desviación estándar de la muestra
n = 100  # Tamaño de la muestra
alpha = 0.05  # Nivel de significancia

# Cálculo de t
t = (X - mu) / (s / np.sqrt(n))

# Gráfica de la distribución t de Student
df = n - 1  # Grados de libertad
x = np.linspace(-5, 5, 400)
y = stats.t.pdf(x, df)

plt.plot(x, y, 'b-', label='Distribución t de Student (n-1)')

# Calcular los valores críticos de t de dos colas
t_critical = stats.t.ppf(1 - alpha / 2, df)
lower_critical = -t_critical
upper_critical = t_critical

# Rellenar la región crítica
plt.fill_between(x, 0, y, where=(x <= lower_critical) | (x >= upper_critical), color='red', alpha=0.5, label='Región crítica')

# Marcar el valor calculado de t
plt.axvline(t, color='purple', linestyle='--', label=f'Valor calculado de t = {t:.2f}')

plt.legend()
plt.title('Prueba de Hipótesis con t de Student')
plt.xlabel('Valor de t')
plt.ylabel('Densidad de probabilidad')
plt.show()

