""""
    file:misvariables.py
    autor:@reroes

    nota mayor o igujal a 18: sobresaliente
    nota mayor o igual a 16 y menor a 18: muy buena
    nota mayor o igual a 13 y menor a 16: buena
    nota menor a 13: insuficiente 
"""
from misvariables import *
#uso de condicionales simple
nota = int(input("ingrese la nota 1: "))


if nota >= 18:
    print("%s - nota %d" % ("sobresaliente", nota))
else :
    if nota >= 16 and nota < 18 :
        print("%s - nota %d" % ("muy buena",nota))
    else :
        if nota >= 13 and nota < 16:
            print("%s - nota %d" % ("buena", nota))
        else:
            if nota < 13:
                print("%s - nota %d" % ("insuficiente", nota))

