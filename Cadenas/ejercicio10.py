"""Escribir un programa que pregunte por consola por los productos 
de una cesta de la compra, separados por comas, y muestre por 
pantalla cada uno de los productos en una línea distinta."""


cesta_de_compra = input("Introduce los productos de la cesta, separados por (,): ")
print(cesta_de_compra.replace(", ", "\n"))