"""Escribir un programa que pregunte el nombre del usuario en la consola y después
de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, 
donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras
que tienen el nombre."""

nombre = input("Introduce tu nombre: ")
n = int(nombre.__len__())
print(f"Tu nombre es {nombre.upper()} y el numero de letras que tiene es de {n}.")