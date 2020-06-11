# -*- coding: utf-8 -*-
"""
Ejercicio 3 : Realice un programa que pida el nombre de un persona y lo muestre por consola o
interprete repetido 1000 veces, pero dejando un espacio de separación entre aparición
del nombre. (utilice operadores de concatenación y repetición).
"""
nombre=str(input("Escriba: "))
#Concatenacion del nombre con el espacio de separacion
nombre=nombre +  ' '
#Repeticion
nombre=nombre*100
print(nombre)