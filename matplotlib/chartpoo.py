'''
Los graficos orientados a objetos son un poco mas complejos de escribir pero permiten mucha personalizacion a diferencia de pyplot
'''

import math
import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(0,20,10)
y = np.linspace(0,5,10)
z = np.linspace(0,10,10)

fig = plt.figure()
axes_1 = fig.add_axes([0.1,0.1,0.8,0.9]) # Los primeros dos argumentos manejan la posicion en el eje de la figura
axes_2 = fig.add_axes([0.65,0.17,0.2,0.5]) # Los segundos dos argumentos manejan el tamaño en el eje de la figura
axes_1.plot(x,y,"r")
axes_2.plot(x,z,"b")
axes_2.set_facecolor("grey")
plt.show()