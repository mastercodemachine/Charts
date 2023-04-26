import seaborn as sns
import matplotlib.pyplot as plt 

print()
print(sns.get_dataset_names()) # Muestra lista de nombre de los data sets de ejemplo
print()

planets = sns.load_dataset('planets')
print(planets)

sns.displot(data=planets, x='mass', y='orbital_period', hue='method', legend=True, kind='kde')
# displot elige el tipo de grafico mas eficiente segun seaborn
# Hue relaciona las dos variables con una tercera asignandole un color y la leyenda
# kind elige el tipo de grafico
# Inicialmente es un grafico de distribucion de una variable, pero al poner 2 automaticamente seaborn elige otra mejor representacion
plt.show()
