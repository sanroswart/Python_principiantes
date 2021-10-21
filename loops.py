# bucles o alteradores. (nos permiten hacer una tarea tipica que va 
# relacionada con una lista de datos)
# 'for' 'while'
# puedes usar 'break' para romper con la lista y se pare donde el 
# usuario puso el comando
# puedes hacer lo inverso pero con 'continue'
# rompen y continuan el ciclo de un bucle

foods = {'apples', 'bread', 'cheese'}

for food in foods:
    if food == 'cheese':
        break
    print(food)


for number in range(1, 9):
    print(number)




# ojo: si no colocamos un cierre, se creara un bucle infinito
# y correra por siempre
count = 4
while count <= 10:
    print(count)
    count = count + 1
