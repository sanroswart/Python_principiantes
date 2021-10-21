# una funcion es una porcion de codigo en el que el usuario
# le da un dato, esto internamente procesa algo y esto puede o no
# darnos un resultado
#  (no es la definicion por defecto de una funcion tho)
# some of them I've used:
#print()
#dir()
#type()

# 'def' (hace referencia a una funcion, es una definicion de funcion)
def hello(): 
    print("hello world")

hello()

# estas funciones de tipo 'def' (que lo usas para convertir una palabra
# cualquiera en funcion) 
# no se va a ejecutar hasta
# que lo empiezas a utilizar (llamandolo) (como la forma arriba)

# puedes hacer cosas mas complicadas como ejemplo
# que la funcion salude a alguien
# en ese caso tienes que definir un parametro
def hola(name = 'person'):
    print("hello", name)

hola("alvin")
# en este caso incluso puedes determinar diferentes nombres
hola('walitza')
hola('felix')
# que pasa si llamo hola y no doy un valor? da error, indicale un valor a la variable como lo hice arriba
# en caso de que llames la funcion sin valor
hola()

# esta solo es una funcion que te devuelve el valor de esta suma
def add(n1, n2):
    return n1 + n2

print(add(10, 30))
print(add(20, 40))

# 'lambda' (son funciones anonimas que toman un numero de argumentos
# pero que estas solo pueden ser escritas utilizando una expresion)
add = lambda n1, n2: n1 + n2

print(add(1, 1))