'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 10: Excepciones
Archivo De Funciones
Fecha: 20 De Octubre De 2022
'''


def captura():
    lista=[]
    try:
        n=int(input("Cuantas Calificiones Quieres Capturar? "))
        while n<0:
            n=int(input("Cuantas Calificiones Quieres Capturar (Más De 1)? "))
    except Exception:
        print("Captura Unicamente Números")
        return captura()
    else:
        for x in range(n):
            try:
                cali=float(input("Captura Calificación: "))
                while cali<0 or cali>100:
                    cali=float(input("Captura Una Calificación Válida: "))
            except Exception as ex:
                print(ex)
            else:
                lista.append(cali)
    return lista

def promedio(lista):
    try:
        elementos=len(lista)
    except TypeError as e:
        print(e)
    try:
        suma=0
        for t in lista:
            suma+=t
        prom=suma/elementos
        print("El Promedio De Las Calificaciones Es:",round(prom,2))
    except ZeroDivisionError:
        print("No Existe Una Lista ó Esta No Contiene Elementos ")
        print("Intenta Crear Una Lista Con Al Menos Un Elemento")
        promedio(captura())


def Mayor(lista):
    try:
        mayor=lista[0]
        for y in lista:
            if y>mayor:
                mayor=y
        print("Calificación Mayor",mayor)
    except IndexError:
        print("No Existe Una Lista ó Esta No Contiene Elementos ")
        print("Intenta Crear Una Lista Con Al Menos Un Elemento")
        Mayor(captura())

def Menor(lista):
    try:
        less=lista[0]
        for y in lista:
            if y<less:
                less=y
        print("Calificación Menor",less)
    except IndexError:
        print("No Existe Una Lista ó Esta No Contiene Elementos ")
        print("Intenta Crear Una Lista Con Al Menos Un Elemento")
        Menor(captura())

def buscarCalif(lista,busqueda):
    try:
        for x in range(len(lista)) :
            if lista[x]==busqueda:
                flag=True
                break
            else:
                flag=False
        if flag==True:
            print("Calificación Encontrada")
        else:
            print("Calificación No Encontrada")
    except ValueError as e:
        print(e)

def menu():
    print("           Menu")
    print("1) Capturar Una Lista")
    print("2) Promedio De Una Lista ")
    print("3) Elemento Mayor De Una Lista")
    print("4) Elemento Menor De Una Lista")
    print("5) Buscar Calificación")
    print()

def menuAlt(lista):
    print("           Menu")
    print("1) Promedio De Una Lista ")
    print("2) Elemento Mayor De Una Lista")
    print("3) Elemento Menor De Una Lista")
    print("4) Buscar Calificación")
    print("5) Salir")
    opc=int(input("Selecciona Una Opción: "))
    while opc<1 or opc>5:
        print("Selecciona Una Opción Valida")
        opc=int(input("Selecciona Una Opción: "))
    if opc==1:
        promedio(lista)
    elif opc==2:
        Mayor(lista)
    elif opc==3:
        Menor(lista)
    elif opc==4:
        busqueda=int(input("Calificación a Buscar: "))
        buscarCalif(lista,busqueda)
    else:
        print("Programa Terminado")

def main():
    lista=[]
    listaDefinida=[100,98,87,54,78,65,95, 95, 65, 14, 91, 100, 65, 60, 68, 48, 66, 10, 48]
    menu()
    opc=int(input("Selecciona Una Opción: "))
    while opc<1 or opc>6:
        print("Selecciona Una Opción Valida")
        menu()
        opc=int(input("Selecciona Una Opción: "))
    if opc==1:
        lista=captura()
        menuAlt(lista)
    elif opc==2:
        promedio(lista)
    elif opc==3:
        Mayor(lista)
    elif opc==4:
        Menor(lista)
    elif opc==5:
        busqueda=int(input("Calificación a Buscar: "))
        buscarCalif(listaDefinida,busqueda)
    else:
        print("Programa Terminado")