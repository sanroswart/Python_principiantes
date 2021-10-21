# define un dato o un conjunto de datos que NO VAN A CAMBIAR
x = (1, 2, 3)
print(x)

# tuple() (tambien pueden ser creadas de esta forma)
y= tuple((2, 3, 4))
print(y)

# no tienen tantos modulos como String y List
# aunque si tu tupla solo tiene 1 solo valor, si tiende a tener mas modulos
# un solo elemento no es considerado una tupla, a menos que le insertes ','
z = (1) # no es tupla
a = (2,) # si es tupla
print(a, z)


b = (7, 8, 9)
print(b[0]) # para imprimir un valor especifico de la tupla

# 'del' elimina toda la tupla
del b

#usas tuplas en una aplicacion real
# las usas junto con los diccionarios mayorment '{}'

