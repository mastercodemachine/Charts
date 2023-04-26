'''
set sirve para configurar el estilo, colores, fuente, tamaño, etc de los graficos que se muestran
Buscar en la documentacion todos los estilos
'''
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style='dark', palette='dark', font='Verdana')
sns.barplot(x=['A','B','C'], y=[1,2,3])
plt.show()