import numpy
lista_ruts = []
lista_entradas_total = []

lista_nombre1 = []
lista_nombre2 = []
lista_apellido1 = []
lista_apellido2 = []

entradas_total = 0
total_p = 0
total_g = 0
total_s = 0

cantidad_total = 0
cantidad_p = 0
cantidad_g = 0
cantidad_s = 0

platinum = 0
gold = 0
silver = 0

arreglo_concierto = numpy.zeros((10,10),int)

def menu():
    print("""Menú
    1. Comprar entradas 
    2. Mostrar ubicaciones disponibles
    3. Ver listado asistente
    4. Mostrar ganancias totales
    5. Salir""")

def validar_opc():
    while True:
        try:
            opc = int(input("Ingrese opción: "))    
            if opc in (1,2,3,4,5):
                return opc
            else:
                print("ERROR! debe ingresar una opción del 1 al 5!")
        except:
            print("ERROR! debe ingresar un número entero!")        

def validar_cant():
    while True:
        try:
            cantidad = int(input("Ingrese cantidad de entradas que desea (max 3): "))       
            if cantidad >= 1 and cantidad <=3:
                return cantidad
            else:
                print("ERROR debe ingresar una cantidad permitida!")    
        except:
            print("ERROR! debe ingresar un número entero!")        
        
def validar_rut():
    while True:
        try:
            rut= int(input("Ingrese rut: "))       
            if len(str(rut)) == 8:
                lista_ruts.append(rut)
                return rut
            else:
                print("ERROR debe ingresar un rut de 8 dígitos!")    
        except:
            print("ERROR! debe ingresar un número entero!")             

def mostrar_escenario():
    for x in range(10):
        print(f"Fila {x+1}:" , end=" ")
        for y in range(10):
            print(f"{arreglo_concierto [x][y]}:" , end=" ")     
        print()    

def filas():
    while True:
        try:
            fila = int(input("Ingrese la fila de el asiento deseado: "))    
            if fila >= 1 and fila <=10:
                return fila
            else:
                print("ERROR! debe ingresar una fila del 1 al 10!") 
        except:
            print("ERROR! debe ingresar un número entero!")         
        
def columnas():
    while True:
        try:
            columna = int(input("Ingrese la columna de el asiento deseado: "))    
            if columna >= 1 and columna <=10:
                return columna
            else:
                print("ERROR! debe ingresar una columna del 1 al 10!") 
        except:
            print("ERROR! debe ingresar un número entero!")   

def validar_pnombre():
    while True:
        nombre1 = input("Ingrese su primer nombre: ")
        if len(str(nombre1.strip))>= 3 :
            return nombre1
        else:
            print("ERROR! escriba un nombre con 3 o más letras!")

def validar_snombre():
    while True:
        nombre2 = input("Ingrese su segundo nombre: ")
        if len(str(nombre2.strip)) >= 3  :
            return nombre2
        else:
            print("ERROR! escriba un nombre con 3 o más letras!")            

def validar_appaterno():
    while True:
        apellido1 = input("Ingrese su primer apellido: ")
        if len(str(apellido1.strip)) >= 3 :
            return apellido1
        else:
            print("ERROR! escriba un apellido con 3 o más letras!")

def validar_apmaterno():
    while True:
        apellido2 = input("Ingrese su segundo apellido: ")
        if len(str(apellido2.strip)) > 3 :
            return apellido2
        else:
            print("ERROR! escriba un apellido con 3 o más letras!")                        


    
                