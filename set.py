# es una coleccion que es desordenada, por ende no tiene un indice
# los son utilizados para definir una coleccion que no tiene indice

colors = {'red', 'green', 'blue'}
#print(type(colors)) #tipo de dato 'set'

# tambien se puede comprobar 
# si hay un dato dentro de los tipos de datos en el set
# usando 'in'
print('red' in colors)

# .add() (puedes agregar otros datos al set)
# como no tiene un indice lo agrega 'aleatoriamente' (en lugar)
colors.add('violet')
print(colors)
# .remove() (tambien podemos remover elementos)
colors.remove('red')
print(colors)
# .clear (tambien se puede limpiar el set)
colors.clear()
print(colors)
# y tambien podemos eliminarlo como las tuples (con 'del')
del colors
print(colors)

# 'set' sirve muy bien para cuando tienes un 
# conjunto de datos que no quieres ordenarlo
# no quieres estar definiendolos por indice ni reordenandolos
# tan solo quieres tener un conjunto de datos defino
# que puedes acceder a el o puedes agregar mas datos a el y demas
