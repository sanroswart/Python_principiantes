# es el control flow 'if' 
# concepto relacionado con el control de flujo de un programa
# operadores de comparacion
# 'if' (si es de tal x forma do this)
# 'else' (caso contrario)
# 'elif' (una especie de intermedio entre 'else' e 'if')
# notas cada operador de comparacion al final de la oracion lleva ':'
# para que siga con la cadena(o mandato) que este da

x = 10

if x == 20:
    print ("x is 20")
else:
    print("x < than 20")

# tambien se puede hacer con strings

color = "blue"

if color == "red":
    print("the colors red")
elif color == "blue":
    print("the color is blue")
else: 
    print("any color")


# puedes hacer lo mas complejo tambien, como if dentro de if y etc
name = "riton"
last_name = "dickens"

if name == "quaksan":
    if last_name == "dickens":
        print("you're a dick lol")
    else: 
        print("you still a dick")
else:
    print("hola soy josue")


# operadores logicos
# 'and'
# 'or'
x = 1 
y = 20

if x > 2 and y < 10:
    print("x greater than 2 and less than or equal to ten")
if x > 2 or y <= 20:
    print("x... i'm honestly tired of typing, dawg")
if not y >= 21:
    print("go go go")



