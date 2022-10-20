'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 10: Excepciones
Archivo Principal
Fecha: 20 De Octubre De 2022

Crear un programa que capture N calificaciones (en una lista) y
muestre un menú con las operaciones básicas de manejo de listas (capturar, promedio, mayor, menor,
buscar una calificación) y haciendo uso del las siguientes excepciones:
    •ZeroDivisionError 
    •IndexError
    •valueError
    •Otra que consideres necesaria.
'''
import pract10Func as pf

opc=1
end=False
while opc==1 or end==True:
    try:
        pf.main()
        print("Si Se Captura Un Dato No Númerico, El Programa Se Cierra Igualmente")
        opc=int(input("Deseas Usar El Programa Otra Vez? (1 Para Continuar) "))
    except Exception:
        end=True
        break
