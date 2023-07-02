import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Crear los datos para el gráfico
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Crear la figura y los ejes
fig, ax = plt.subplots()
line = ax.plot(x, y)

# Función de actualización para el gráfico animado
def update(frame):
    # Actualizar los datos del gráfico
    line.set_ydata(np.sin(x + frame / 10))
    return line

# Crear la animación
ani = animation.FuncAnimation(fig, update, frames=100, interval=50)

# Mostrar el gráfico animado
plt.show()
