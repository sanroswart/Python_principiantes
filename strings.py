# que podemos hacer con los 'Strings'?
myStr = " Hello World"

print("you salute ur world as" + myStr)
# unas forma mas simples de hacer una concatenation

# la 'f' es como decirle: voy a imprimir un text, 
# pero dentro de este texto hay una variables
print(f"you salute ur world as {myStr}")
#. format() (es como decirle: en este valor '0' voy a colocar
# la variable que coloque en .format())
print("you salute ur world as {0}".format(myStr))



# 'dir' 
# nos ensena que podemos hacer con cierto tipo de dato. EXAMPLES BELOW
# si corres este codigo de abajo te ensena todo el uso que le puedes dar 
# a ese string (aplicable en otras clases too)
# print(dir(myStr))  

# Algunos Metodos

# .upper() (pone todo en mayuscula)
print(myStr.upper())
# .lower() (pone todo en minuscula)
print(myStr.lower())
# .swapcase() (cambia el tamano de las letras)
print(myStr.swapcase())
# .capitalize() (convierte la primera letra en mayuscula)
print(myStr.capitalize())
# .replace() (reemplaza el texto que le digas con uno que le pongas)
print(myStr.replace('Hello', 'Bye').upper())
# metodo encadenado (meter un metodo dentro de otro)
# forma de decir "un metodo va despues de otro"

# .count() (este metodo cuenta cuantas veces tienes un caracter o letra repetida)
print(myStr.count('l'))
# .startswith() (te dice si tu texto empieza con determinado
# caracter o palabra)
print(myStr.startswith('hola'))
print(myStr.startswith('Hello'))
# .endswith() (lo mismo que startswith pero en vez de empieza,
# termina)
print(myStr.endswith('ld'))
# .split() (separa mi texto a partir de un caracter)
print(myStr.split())
# .find() (busca la posicion de determinado caracter)
print(myStr.find('d'))

# len() (determina el numero de elemetos que hay en el string)
print(len(myStr))
# .index() (busca el indice de un caracter directamente)
print(myStr.index('e'))
# .isnumeric (te dice si tu string es numerico)
print(myStr.isnumeric())
# .isnalpha (te dice si tu string es alfanumerico)
print(myStr.isalpha())
# tambien puedes solo imprimir un solo caracter de tu string,
# si te sabes la posicion
print(myStr[4])
# tambien puedes hacerlo inverso
print(myStr[-1])