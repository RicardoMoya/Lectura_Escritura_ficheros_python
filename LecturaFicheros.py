# -*- coding: utf-8 -*-
__author__ = 'Richard'

dirFichero = './fichero_leer.txt'

# OPCIÓN 1: Lectura del fichero desde el principio
with open(dirFichero, 'r') as reader:
    for line in reader:
        print line


# OPCIÓN 2: Lectura del fichero desde la posición de un byte concreto
print '\nLectura del fichero desde el byte 32'
with open(dirFichero, 'r') as reader:
    reader.seek(32)
    for line in reader:
        print line


# OPCIÓN 3: Lectura del fichero desde el principio y tras leerlo borramos el contenido
with open(dirFichero, 'w+') as reader:
    for line in reader:
        print line