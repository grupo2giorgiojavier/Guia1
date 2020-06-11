# -*- coding: utf-8 -*-
"""
Ejercicio 5 : Diseñe un programa que, dados dos números enteros, muestre por pantalla uno de estos
mensajes: <<El segundo es el cuadrado exacto del primero>>, <<El segundo es menor
que el cuadrado del primero>> o <<El segundo es mayor que el cuadrado del primero>>,
dependiendo de la verificación de la condición correspondiente al significado de cada
mensaje.
"""
while True:
    try:
        num1=int(input("Escriba el primer numero: "))
        num2=int(input("Escriba el segundo numero: "))
        break
    except ValueError:
        print("Error en un numero , vuelva a intentarlo")
        break


if num2==num1^2:
    print("<<El segundo es el cuadrado exacto del primero>>")
elif num2<num1^2:
    print("<<El segundo es menor que el cuadrado del primero>>")
elif num2>num1^2:
    print("<<El segundo es menor que el cuadrado del primero>>")
else:
    print("<<Los numeros no cumplen las condiciones solicitadas!>>")