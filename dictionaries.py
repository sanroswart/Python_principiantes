# los dictionaries (dic) (sirven para definir objetos de la vida real
# o tambien poder agrupar ciertos datos colocandoles claves y valores)
# nos permiten definir un dato a partir de claves y valores (x2)
# tambien podemos guardarlo dentro de una variable

from types import prepare_class


product = {
    "name": "book",
    "quantity": 3,
    "price": 4.99
}
print(product)

person = {
    "first_name": "nike",
    "last_name": "arnold"
}
print(person)

# puedes usar modulos como en strings y lists (.clear(), .copy(), .get(), etc)

# .key() (se utiliza solo para obtener las llaves del dictionario)
print(person.keys())

# .items() (el inverso de keys)
print(person.items())

# puedes eliminar con 'del' como en sets, lists, etc
# del person
# print(person)

# tambien en vez de eliminarlo, puedes limpiar sus datos internos
# .clear()
person.clear()
print(person)

# puedes agrupar los dictionaries tambien

Products = [
    {"name": 'book', "price": 10.99},
    {"name": 'laptop', "price": 9.99}
]
print(Products)