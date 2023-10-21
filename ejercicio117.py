import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

# Datos de la tabla de contingencia
observed = np.array([[6, 3], [10, 7]])

# Calculamos los valores esperados (E)
total_observed = observed.sum()
row_totals = observed.sum(axis=1)
col_totals = observed.sum(axis=0)

expected = np.outer(row_totals, col_totals) / total_observed

# Calculamos el estadístico de chi-cuadrado
chi_squared_stat = ((observed - expected) ** 2 / expected).sum()

# Grados de libertad
degrees_of_freedom = (observed.shape[0] - 1) * (observed.shape[1] - 1)

# Nivel de significancia
alpha = 0.05

# Valor crítico
critical_value = chi2.ppf(1 - alpha, degrees_of_freedom)

# Gráfica de la distribución chi-cuadrado
x = np.linspace(0, critical_value + 10, 1000)
y = chi2.pdf(x, degrees_of_freedom)
plt.plot(x, y, label='Distribución Chi-cuadrado')

# Área de la región crítica
plt.fill_between(x, 0, y, where=(x > critical_value), color='red', alpha=0.5, label='Región Crítica')

# Línea vertical para el estadístico de chi-cuadrado
plt.axvline(chi_squared_stat, color='blue', linestyle='--', label='Estadístico de Chi-cuadrado')

plt.title('Prueba de Hipótesis de Independencia')
plt.xlabel('Estadístico de Chi-cuadrado')
plt.ylabel('Densidad de Probabilidad')
plt.legend()
plt.show()

# Resultado
if chi_squared_stat > critical_value:
    print("Con un nivel de significancia del", alpha * 100, "%, rechazamos la hipótesis nula.")
else:
    print("Con un nivel de significancia del", alpha * 100, "%, no rechazamos la hipótesis nula.")
