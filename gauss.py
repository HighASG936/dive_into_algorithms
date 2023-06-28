import numpy as np
import math
import matplotlib.pyplot as plt

# Datos de la campana de Gauss
mu = 300_007/2  # Media
sigma = mu/4   # Desviación estándar

# Generar valores x en el rango deseado
x = np.linspace(0, 300_007, 100)

# Calcular los valores y correspondientes a la campana de Gauss
y = [1_500_000/(math.sqrt(2*math.pi*sigma)) * math.exp( -0.5 * ((x-mu)/sigma)**2 ) for x in x ]

# Crear la figura y el eje
fig, ax = plt.subplots()

# Graficar la campana de Gauss
ax.plot(x, y)

# Configurar etiquetas y título
ax.set_xlabel('Valores x')
ax.set_ylabel('Valores y')
ax.set_title('Campana de Gauss')

# Mostrar la gráfica
plt.show()