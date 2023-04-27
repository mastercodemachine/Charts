import seaborn as sns
import matplotlib.pyplot as plt 
'''
Seaborn esta diseñado sobre matplotlib para trabajar de forma mas eficiente con dataframes de pandas

Seaborn tiene 4 formas de hacer graficos cada uno con sus opciones segun el tipo de informacion a visualizar.
Esta el joinplot() que combina varias clases o kind de graficos en uno solo para mostrar toda la informacion rapidamente (hace graficos chetos)
Esta el replot() que es relationship esta el scatterplot y el lineplot
Esta el displot de distribution con kdeplot, histplot, ecdfplot, rugplot.
y el catplot de categorical con stripplot, swarmplot, boxplot, violinplot, pointplot y barplot

para graficar eligo el tipo de grafico y luego la clase 
'''
print()
print(sns.get_dataset_names()) # Muestra lista de nombre de los data sets de ejemplo
print()

planets = sns.load_dataset('planets')
print(planets)

# Para graficos de una variable
sns.displot(data=planets, x='mass', legend=False, cumulative=False, kind='hist', stat='count', hue='method',multiple='dodge')
sns.displot(data=planets, x='mass', kind='kde', hue='method')
plt.show()

'''
# El cumulative acumula los valores para generar los siguientes
# El stat elige como es la escala del eje y, puede ser 'count', 'percent', 'frequency' o 'probability'
# multiple es la forma en la que se comparan los datos en el eje x, dodge: se pone una columna al lado de la otra, en stack se apilan 
  y en layer se acumulan pero se diferencian
# Hue relaciona las variables con una tercera asignandole un color y la leyenda
# kind elige el tipo de grafico
# Shade = True sirve para graficar el area debajo de la curva en el grafico kde, solo funciona si uso kdeplot especificamente
'''