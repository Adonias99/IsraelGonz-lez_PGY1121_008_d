import numpy
import os
import time
import msvcrt

import funciones_et as fn

arreglo_concierto = numpy.zeros((10,10),int)

lista_ruts = []
lista_entradas_total = []

lista_nombre1 = []
lista_nombre2 = []
lista_apellido1 = []
lista_apellido2 = []

valor_total = 0
total_p = 0
total_g = 0
total_s = 0

cantidad_total = 0
cantidad_p = 0
cantidad_g = 0
cantidad_s = 0

platinum = 120000
gold = 80000
silver = 50000




os.system('cls')
while True:
    fn.menu()
    opc = fn.validar_opc() 
    print()
    if opc == 1:
        nombre1 = fn.validar_pnombre()
        nombre2 = fn.validar_snombre()
        apellido1 = fn.validar_appaterno()
        apellido2 = fn.validar_apmaterno()
        print()
        rut = fn.validar_rut()
        lista_ruts.append(rut)
        print()
        cantidad = fn.validar_cant()
        print()
        print(arreglo_concierto)
        print()
        for x in range(cantidad):
            fila = fn.filas()
            if fila == 1 or fila == 2:
                total_p = total_p + platinum
                cantidad_p = cantidad_p + cantidad
            
            elif fila == 3 or  fila == 4 or fila == 5:
                total_g = total_g + gold
                cantidad_g = cantidad_g +cantidad
            else:
                total_s = total_s + silver   
                cantidad_s = cantidad_s + cantidad   
        for x in range(cantidad): 
            columna = fn.columnas()
            
            print("Compra exitosa!")

    elif opc == 2:
        
        print("            _____________"  )
        print("           | ESCENARIO   |")
        print("           |_____________|")
        fn.mostrar_escenario()
    elif opc == 3:
        print("Listado de Asistentes por RUN:")
        print(lista_ruts)
    elif opc == 4:
        print("  Tipo Entrada     |  Cantidad    |         Total")
        print("---------------------------------------------------------")
        print(f"Platinum $120.000  | {cantidad_p}            | {total_p*cantidad_p} ")
        print("---------------------------------------------------------")
        print(f"Gold $80.000       | {cantidad_g}            | {total_g*cantidad_g}")
        print("---------------------------------------------------------")
        print(f"Silver $50.000     | {cantidad_s}            | {total_s*cantidad_s}")
        print("---------------------------------------------------------")
        print(f"Total =            | {cantidad_p + cantidad_g + cantidad_s}           |        {total_p*cantidad_p + total_g*cantidad_g + total_s*cantidad_s }")
        print()
    else:
        print(f"Gracias por visitarnos {nombre1} {nombre2} {apellido1} {apellido2}, Adios, 11/07/2023 ")   
        break