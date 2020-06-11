# -*- coding: utf-8 -*-
"""
Ejercicio 1 : Diseñe un algoritmo y programa para calcular el area de un
circulo dado su radio
"""
import math
# Solicitud al usuario del radio
radio=float(input("Escriba el radio del circulo: "))   
# Calculo del area
area=2*math.pi*radio
print("El area de la circunferencia es: " + str(area))