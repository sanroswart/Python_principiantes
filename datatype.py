
# class 'Strings' (str) (cadenas)
# es una cadena de caracteres en secuencia o uno detras de otro, 
# es conocido como string
# puedes decirles funciones
# puedes utlizar distintos tipos de comillas:
#  ('') ("") (''' ''') (""" """)
print("Hello world")
print('Hello world')
print('''Hello World''')
print("""Hello world""")


# (esta salida que me devuelve la funcion 'type', 
# se la pasas a otra funcion llamada 'print')
# el 'print' devuelve texto, 
# el 'type' obtiene informacion de un texto para saber que tipo de dato es
print(type("hello world"))


# '+' concatenation (concatenación) ( se usa para unir strings)
#  '+' con letras se concadena,
#  con numeros se suma (obvio)
print("bye" + "world") # (this still a 'string' tho)


# Numbers
# it's pretty self explanatory lol

# class 'Integer' (int) (entero in spanish)
print(type(30))
print(30) 

# class 'Float' (float) (decimal in spanish)
print(type(30.5))
print(30.5)


# class 'Boolean' (bool) (boleanos in spanish) 
# (tipos de datos logicos)
# sirve para definir tipos de estado
print(type(False))
print(type(True))
True 
False 


# class 'List' '[]'
# se utilza pa guardar una lista de datos
# puedes almacenar cualquier tipo de datos. examples below
# esta conformada por distintos items o elementos
# (puedes cambiarle los datos)
print(type([1, 2]))
[10, 20, 30, 50]
['hello', 'bye', 'Adios']
[10, 'hello', True, 20.5]
[]


# class 'Tuple' '()' (tuplas in spanish) 
# son listas con la diferencia de que lo que esta 
# dentro de las tuplas no puede cambiar
(10, 20, 30, 55)
()


# class Dictionaries (dict) '{}'
# te deja agrupar datos de la misma entidad
# cada elemento esta definido por un nombre y un valor
# puedes poner cualquier nombre y cualquier valor 
# y las separas con comas es como una especie de lista
# cada dato debe ir con :
# ("key": "value") actual names y forma de escribirlo
print(type({
    "name": "Ryan",
    "lastname": "Ray",
    "nickname": "san",
    }))



# class 'NoneType' ('None')
# es es para definir un tipo de dato que no tiene nada
# es como decirle que lo que vamos a utilizar 
# no esta definido aun por un tipo de dato

