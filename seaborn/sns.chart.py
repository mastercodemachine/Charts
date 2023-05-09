import seaborn as sns
import matplotlib.pyplot as plt 

'''
Seaborn esta diseñado sobre matplotlib para trabajar de forma mas eficiente con dataframes de pandas

Seaborn tiene 4 formas de hacer graficos cada uno con sus opciones segun el tipo de informacion a visualizar.
Esta el jointplot() que combina varias clases o kind de graficos en uno solo para mostrar toda la informacion rapidamente (hace graficos chetos)
Esta el relplot() que es relationship esta el scatterplot y el lineplot
Esta el displot de distribution con kdeplot, histplot, ecdfplot, rugplot.
y el catplot de categorical con stripplot, swarmplot, boxplot, violinplot, pointplot y barplot

para graficar eligo el tipo de grafico y luego la clase 

Hay propiedades que podrian no funcionar si uso el grafico por ejemplo multiple='dodge' en vez de eso uso dodge='True'

Para graficar subgraficos dentro de una figura tengo que usar los graficos especificos como estan abajo. ej: swarmplot etc
'''

print()
print(sns.get_dataset_names()) # Muestra lista de nombre de los data sets de ejemplo
print()

tip = sns.load_dataset('tips')
print(tip)
'''
sns.set_style('darkgrid')
f, axs = plt.subplots(2, 2, figsize=(15,10))
sns.swarmplot(data=tip, x='day', y='tip', hue='sex', dodge='True', ax=axs[0,0])
sns.histplot(data=tip, x='day',y='tip', hue='sex',ax=axs[0,1], multiple='dodge', palette='pastel')
sns.histplot(data=tip, x='tip', hue='sex',ax=axs[1,0], multiple='dodge', palette='pastel')
axs[0,0].set_title("y en funcion de x")
axs[0,0].set_xlabel("X")
axs[0,0].set_ylabel("Y")
f.tight_layout() # Impide que los elementos del grafico se superpongan
plt.show()


# plt.subplots_adjust(wspace=0.3, hspace=0.1) ajustar separacion de grafico

sns.boxplot(data=tip, x='day', y='tip', hue='sex', dodge='True')
sns.swarmplot(data=tip, x='day', y='tip', hue='sex', dodge='True', marker='<', color="0")
plt.show()
sns.catplot(data=tip, x='day', y='tip', hue='sex', col='time', dodge='True', kind='box')
plt.show()
'''


'''
marginal ticks muestra la escala de los graficos secundarios, margina kws se usa para para modificar los graficos secundarios
'''
sns.jointplot(data=tip, x='tip', y='total_bill', hue='sex', kind='hist', marginal_ticks='True', marginal_kws=dict(multiple='dodge'))

plt.show()

sns.pairplot(data=tip, hue='sex')
plt.show()

'''
tip.corr muestra la correlacion entre todas las variables de la base de datos 
annot muestra el numero de relacion en el cuadrante central perteneciente
linecolor y linewidths cambian el color y grosor de las lineas matriciales
cmap es para elegir los colores del heatmap
'''
sns.heatmap(tip.corr(), annot=True)
plt.show()

'''
# si no quiero la leyenda pongo legend = False
# El cumulative acumula los valores para generar los siguientes
# El stat elige como es la escala del eje y, puede ser 'count', 'percent', 'frequency' o 'probability'
# multiple es la forma en la que se comparan los datos en el eje x, dodge: se pone una columna al lado de la otra, en stack se apilan 
#  y en layer se acumulan pero se diferencian
# Hue relaciona las variables con una tercera asignandole un color y la leyenda
# kind elige el tipo de grafico
# Shade = True sirve para graficar el area debajo de la curva en el grafico kde, solo funciona si uso kdeplot especificamente
'''
