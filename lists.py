# puedes guardar todo en una lista (literalmente)

demo_list = [69, 'popola', 69.420, True, ["soy dora"], 69]
colors = ['red', 'blue', 'green', 'yellow']
print(demo_list + colors)



# list() (otra forma de crear una lista)
# solo te puedes pasar un argumento.
# asegurate de usar tuples '()'
# de esa forma puedes agregarle mas de 1 argumento agrupandolos en la tupla
# lo va a leer como si fuese uno
numbers_list = list((1, 2, 3, 4))
print(numbers_list)

# range() (lista basada en un rango, o sea de un punto a otro punto)
# ojo el comando solo llega al ultimo numero y/o caracter
# que le pongas al final eje en esta si le pongo del 1 - 11 va a llegar hasta el 10
r = list(range(1, 11))
print(r)

# i just wanted to know que comandos puedes usar con una lista lol
# pretty much los mismos que en string
# print(dir(type(colors)))

# 'in' esto funciona para saber si un elemento esta
# dentro de una lista
print('green' in colors)

# puedes reasignar las listas too (lo que esta dentro de ellas) 
# recuerda la maquina cuenta del 0 en adelante
Colors = ['black', 'white', 'brown']
print(Colors)
Colors[2] = 'purple'
print(Colors)

# algunos metodos de las lists

# .append() sirve para agregar argumentos a la lista
# recuerda usar tuples() para agregar mas de dos argumentos
Colors.append('violet')
print(Colors)
# .extend (extinde la lista con los elementos agregados)
# si es mas de uno agregalos en modo lista '[]'
# tambien puedes copiar el .extend() abajo y agregarle mas argumentos
Colors.extend(['red', 'blue'])
Colors.extend(['yaNoMas', 'colores'])
print(Colors)

# .insert() (sirve para insertar un elemento en una posicion dada)
cosas = ['tv', 'phone', 'pc']
cosas.insert(1, 'mic')
# y si quieres posicionarlo al final puedes hacer con len()
cosas.insert(len(cosas), 'mirror')
print(cosas)

# .pop() (quita el ultimo elementos que esta en la lista)
# a menos que le des un indice
cosas.pop()
print(cosas)
# .remove() (elimina el elemento que quieras de la lista)
cosas.remove('tv')
print(cosas)
# .clear () (quita todos los elemntos y deja la lista vacia)
#cosas.clear()
#print(cosas)

# .sort () (ordena la lista alfabeticamente)
# .sort (reverse) (lo pone de manera inversa)
cosas.sort()
print(cosas)

# .index() (te dice el indice de una palabra en la lista (posicion))
print(cosas.index('phone'))

# .count() (cuenta cuantas veces esta un argumento en una lista)
print(demo_list.count(69))
