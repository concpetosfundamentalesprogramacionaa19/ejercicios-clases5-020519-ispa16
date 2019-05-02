""""
    file:misvariables.py
    autor:@reroes

    deseamos obtener el costo de una carrera universitaria . El valor promedio de cada ciclo es de 1200 dolares, el
    valor promedio del seguro educativo por ciclo es de 100 dolares si la edad del estudiante es menor o igual a 20,caso
    contrario si el estudiante tiene una modalidad a distancia el numero de ciclos a seguir es de 10 caso contrario debera
    seguir ocho ciclos , obtener la proyeccion del costo de la carrera de un estudiante
    sera de 150 dolares
"""
from misvariables import *
#uso de condicionales simple
valor_promedio = 1200

#distancia = "distancia"
edad = int(input("ingrese su edad : "))
modalidad = input("ingrese la modalidad a seguir : ")

#calculo de numero de ciclos
if modalidad == "distancia":
    numero_ciclos = 10
elif modalidad == "presencial":
    numero_ciclos = 8

#calculo de valor de seguros
if edad <= 20:
    seguro = 100
else:
    seguro = 150
valor_ciclo_real = valor_promedio + seguro
valor_total = ((valor_promedio + seguro)*numero_ciclos)
print("el valor total a pagar es: %s" % (valor_total))



