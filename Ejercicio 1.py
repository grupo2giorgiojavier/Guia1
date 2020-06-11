# -*- coding: utf-8 -*-
"""
Ejercicio 1 : Diseñe un algoritmo y programa para calcular el area de un
circulo dado su radio
"""
import math
# Solicitud al usuario del radio, en caso de que no sea un numero se le solicitara de nuevo al usuario a ingresar el radio correcto
while True:
    try:
        radio=float(input("Escriba el radio del circulo: "))
        break
    except ValueError:
        print("Lo ingresado no es numero, favor de ingresar un numero correcto!")   
# Calculo del area
area=2*math.pi*radio
#impresion del numero obtenido
print("El area de la circunferencia es: " + str(area))