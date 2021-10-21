# es un concepto que me permite desarrollar aplicaciones reales

# types of modules
# own modules
# third party modules
# python modules

# este solo es una mucho de muchos modulos que hay integrados
# en python
import datetime

print(datetime.date.today())
print(datetime.timedelta(minutes = 70))

# otra forma de importarlos
from datetime import timedelta, date

print(date.today(), timedelta(minutes = 80))

# en fmath.py veran como pueden crear un modulo ustedes mismos
import fmath

fmath.add(1, 2)
fmath.substract(1, 2)

# 'pip' utilizado para instalar modulos externos de python
# tienes que hacerlo desde el cmd

from colorama import Fore, Style, init

init(convert=True)
print(Fore.BLUE, "rosguita")

