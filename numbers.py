# pretty self explanatory
10
14.5

print(type(10)) #int
print(type(10.4)) #float

# poner '**numero' es basicamente elevar a la potencia del numero que pongas 
# al final eje: 2 al cubo seria asi
print(2**3) 

# poner '//' te da el valor entero de la divion 
# (en caso de que sea decimal el resultado)
print(9//5)

# '%' esto obtiene el residuo de una division
print(9%5)

# input() (toma el caracter de lo que el usuario le escriba en la consola)
age = input("insert your age: ")
# como no puedes sumar una palabra con un numero, utilizas
# 'int ()' o 'float ()' para convertir ese 'variable en un 'numero'
# (aunque en este caso vendria siendo un 'string' porque la variable
# se va a determinar luego de que el 'input()' tome el caracter
# del 'string'
new_age = int(age) + 5
print(new_age)