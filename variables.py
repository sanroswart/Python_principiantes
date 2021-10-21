
# Variables 
# es un nombre simbolico para un valor
# utilizado para almacenar el valor de un dato
# se utliza para guardar las clases (class) examples below
# ojo: las variables no pueden empezar por un numero
# (variable = valor ) actual way of type it
name = "el napo"
print(name) 

x = 69
print(x)

# 'case sensitive'
# si creo otra variable aunque tengan el mismo nombre
# si hay una un caracter diferente en minuscula o mayuscula
# esto hace la variable totalmente diferente
book = "movie dick"
Book = "fifty shades darker"
print(book)
print(Book)

# puedes definir tus variables en una sola linea
y, booK = 4, "I robot"
print(y, booK)


# si el nombre de la variable es muy largo
# puedes usar diferentes tipos de formas para escribirlos
# esto ayuda a que pueda entenderse mejor
book_name = "puto"
BookName = "el que"
bookName = "lo lea"
print(book_name)
print(BookName)
print(bookName)

# Convenciones
# son formas para definir variables. examples below
your_name = "Johnny" #Snake Case
yourLastname = "Bravo" #Camel Case
FavoriteMovie = "Friday The 13th" #Pascal Case
print(your_name)
print(yourLastname)
print(FavoriteMovie)

#Snake Case: separar las palabras via '_'
#Camel Case: separar las palabras con mayuscula 
# despues de empezar con minuscula
#Pascal Case: separarlas via mayusculas

# Variable Constante (convencion)
# escrita toda en mayuscula 
# ese valor no va a cambiar
PI = 3.1416
MY_NAME = "tu cuco"
print(PI, MY_NAME)

# si yo quiero cambiarle en valor a la variable 
# mas tarde en el codigo, lo puedo hacer
# en python pueden ser reasignadas
# (no aplica con las constantes)
saludo = "hola"
saludo = "hi"
print(saludo)
