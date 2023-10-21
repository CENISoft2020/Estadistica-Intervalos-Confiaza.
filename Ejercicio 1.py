import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Datos del problema
X = 82  # Media muestral
mu = 86  # Media poblacional bajo H0
s = 15  # Desviación estándar de la muestra
n = 25  # Tamaño de la muestra
alpha = 0.05  # Nivel de significancia

# Cálculo de t
t = (X - mu) / (s / np.sqrt(n))

# Gráfica de la distribución t de Student
df = n - 1  # Grados de libertad
x = np.linspace(-5, 5, 400)
y = stats.t.pdf(x, df)

plt.plot(x, y, 'b-', label='Distribución t de Student (n-1)')
plt.fill_between(x, y, where=(x <= -t) | (x >= t), color='red', alpha=0.5, label='Región crítica')
plt.axvline(-t, color='red', linestyle='--', label=f'Valor calculado de t = {t:.2f}')
plt.axvline(t, color='red', linestyle='--')
plt.legend()
plt.title('Prueba de Hipótesis con t de Student')
plt.xlabel('Valor de t')
plt.ylabel('Densidad de probabilidad')
plt.show()
