'''
Mas documentacion en los archivos png sobre distintas formas de graficar o en la pagina del propio matplotlib
'''

def run():
    import matplotlib.pyplot as plt
    import numpy as np

    x = np.linspace(0,5,10)
    y =x**2
    print(f"\nPrimer arreglo: {x}\n\nSegundo arreglo: {y}")

    plt.hexbin(x,y) #"r" de red "o" de circulos y "-" de unir con lineas continuas
    plt.show()

if __name__ == "__main__":
    run()