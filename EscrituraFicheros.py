# -*- coding: utf-8 -*-
__author__ = 'Richard'

# Lista con las lineas a escribir en el fichero
lineas = ['Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', '...']

dirFichero = './fichero_escribir.txt'

# Escribo en un fichero el contenido de la lista. Un elemento, una linea
fichero = open(dirFichero, 'w')
for l in lineas:
    fichero.write(l + '\n')
fichero.close()


# Escribo en el fichero el contenido de la lista, sin borrar el contenido del fichero
fichero = open(dirFichero, 'a+')
for l in lineas:
    fichero.write(l + '\n')
fichero.close()
