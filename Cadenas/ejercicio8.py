"""Escribir un programa que pregunte por consola el precio de un producto en euros con 
dos decimales y muestre por pantalla el número de euros y el número de céntimos del 
precio introducido."""

precio = input("Introduce el precio del producto en euros (con dos decimales): ")
euros, centimos = precio.split('.')
print(f"Euros: {euros} €")
print(f"Centimos: {centimos} centimos")
