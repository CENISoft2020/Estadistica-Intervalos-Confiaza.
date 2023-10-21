import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Datos del problema
mean_A = 905
mean_B = 925
std_A = 25
std_B = 35
nA = 15
nB = 20
alpha = 0.10

# Estadístico de prueba
SE = np.sqrt((std_A**2 / nA) + (std_B**2 / nB))
t = (mean_B - mean_A) / SE

# Grados de libertad (aproximadamente)
df = (std_A**2 / nA + std_B**2 / nB)**2 / ((std_A**4 / (nA**2 * (nA - 1))) + (std_B**4 / (nB**2 * (nB - 1)))

# Valor crítico t (una cola)
critical_value = stats.t.ppf(1 - alpha, df)

# Intervalo de valores de t para graficar
t_values = np.linspace(-3, 3, 400)
# Distribución t-Student bajo la hipótesis nula
pdf_H0 = stats.t.pdf(t_values, df)
# Límite para la región crítica (una cola derecha)
critical_limit = stats.t.ppf(1 - alpha, df)

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(t_values, pdf_H0, label='Distribución t bajo H0')
plt.fill_between(t_values[t_values > critical_limit], 0, pdf_H0[t_values > critical_limit], alpha=0.3, color='red', label='Región Crítica')
plt.axvline(t, color='green', linestyle='--', label='Valor de t')
plt.title('Prueba de Hipótesis - Cables A vs. B')
plt.xlabel('Valor t')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.grid(True)

# Marcar la región crítica
plt.annotate(f'Rechazar H0\n(t={t:.2f})', (t + 0.1, 0.02), color='green')

plt.show()
