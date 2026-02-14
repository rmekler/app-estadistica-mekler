import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Configuración de los datos
mu, sigma = 0, 1
z_start, z_end = 0, 1.21

# Rango de x para la curva completa y para el área sombreada
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x, mu, sigma)
x_fill = np.linspace(z_start, z_end, 100)
y_fill = norm.pdf(x_fill, mu, sigma)

# Crear la gráfica
plt.figure(figsize=(8, 4))
plt.plot(x, y, color='#0077b6', lw=2)
plt.fill_between(x_fill, y_fill, color='#00b4d8', alpha=0.6)

# Etiquetas y formato
plt.axvline(x=0, color='black', lw=1)
plt.xticks([0, z_end], ['0', '$z_0 = 1.21$'])
plt.text(1.3, 0.25, "Área = 0.3869", color='#0077b6', fontweight='bold')
plt.title('Distribución Normal Estándar')
plt.savefig('grafica_normal.png') # Esta línea la guarda
plt.show()                        # ¡Esta línea nueva la muestra en pantalla!