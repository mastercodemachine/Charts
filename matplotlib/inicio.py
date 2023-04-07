'''
Mas documentacion en los archivos png sobre distintas formas de graficar o en la pagina del propio matplotlib
'''

def run():
    import math as ma
    import matplotlib.pyplot as plt
    import numpy as np

    x = np.linspace(0,5,10)
    y =x**2
    z = np.sqrt(x)
    print(f"\nPrimer arreglo: {x}\n\nSegundo arreglo: {y}\n\nTercer arreglo: {z}")

    plt.subplot(2,2,1) # crea una ventana dividida con la cantidad de graficos a mostrar
    plt.plot(x,y,"ro-") #"r" de red "o" de circulos y "-" de unir con lineas continuas
    plt.subplot(2,2,2)
    plt.plot(x,z,"b:")
    plt.subplot(2,2,3)
    plt.plot(x,z,"b:")
    plt.plot(x,y,"r:") 
    plt.subplot(2,2,4)
    x = x.reshape(2,5)
    plt.imshow(x) 
    plt.show()

if __name__ == "__main__":
    run()