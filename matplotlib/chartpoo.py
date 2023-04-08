'''
Los graficos orientados a objetos son un poco mas complejos de escribir pero permiten mucha personalizacion a diferencia de pyplot
'''

import math
import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(0,20,10)
y = np.linspace(0,5,10)
z = np.linspace(0,10,10)

print(plt.style.available) # Muestra los colores de fondo disponibles


fig = plt.figure()
plt.style.use('dark_background') # elige el estilo de fondo de toda la figura, ademas del color
axes_1 = fig.add_axes([0.1,0.1,0.8,0.9]) # Los primeros dos argumentos manejan la posicion en el eje de la figura
axes_2 = fig.add_axes([0.65,0.17,0.2,0.5]) # Los segundos dos argumentos manejan el tamaño en el eje de la figura
# la siguiente manera es otra forma de especificar mas como quiero los estilos de las lineas
axes_1.plot(x,y,color="red",marker="8",markerfacecolor="blue",markersize=15,linewidth=5,linestyle=":")
axes_2.plot(x,z,"b")
axes_2.set_facecolor("grey")

# Aca abajo esta la manera de hacer varios graficos en una sola figura con subplots (notese la "s" al final de subplots)

fig_2, axes = plt.subplots(2,4) # 2 filas x 2 columnas}
axes[0,0].plot(x,y,"ro",label="y-x")
axes[0,0].set_title("y en funcion de x")
axes[0,0].set_xlabel("X")
axes[0,0].set_ylabel("Y")
axes[0,0].legend()
# en la funcion de arriba agregue todos las decoraciones
axes[0,1].plot(x,z,"bo")
axes[0,2].plot(x,z,"bo")
axes[0,3].plot(x,z,"bo")
axes[1,0].plot(x,z,"bo")
axes[1,1].plot(x,z,"bo")
axes[1,2].plot(y,z,"o:")
axes[1,3].plot(z,y,"y")
plt.subplots_adjust(wspace=0.9, hspace=0.9) # ajusta la distancia de separacion entre graficos

plt.show()