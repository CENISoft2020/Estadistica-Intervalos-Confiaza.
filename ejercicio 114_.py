import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Parámetros del problema
alpha = 0.01
p_llamada = 0.7
p_carta = 0.625
n_llamada = 20
n_carta = 16

# Estadístico de prueba (Z)
p = (p_llamada * n_llamada + p_carta * n_carta) / (n_llamada + n_carta)
std_error = np.sqrt(p * (1 - p) * (1 / n_llamada + 1 / n_carta))
Z = (p_llamada - p_carta) / std_error

# Valor crítico
critical_value = stats.norm.ppf(1 - alpha)

# Gráfica
x = np.linspace(-3, 3, 1000)
y = stats.norm.pdf(x, 0, 1)
plt.plot(x, y, label='Campana de Gauss (Distribución Normal)')

plt.fill_between(x, 0, y, where=(x > critical_value), color='red', alpha=0.5, label='Región Crítica')
plt.axvline(Z, color='blue', linestyle='--', label='Estadístico de Prueba')

plt.title('Prueba de Hipótesis de Proporciones')
plt.xlabel('Estadístico de Prueba (Z)')
plt.ylabel('Densidad de Probabilidad')
plt.legend()
plt.show()

# Resultado
if Z > critical_value:
    print("Con un nivel de significancia del", alpha * 100, "%, rechazamos la hipótesis nula.")
else:
    print("Con un nivel de significancia del", alpha * 100, "%, no rechazamos la hipótesis nula.")
