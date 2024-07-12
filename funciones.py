import random
import csv


def Menu():
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
    op=input("Ingrese una opcion :")
    return(op)

def AsignaSueldo():    
    trabajadores=[]
    trabajadores.append (('Juan Perez', random.randint(300000,2500000)))
    trabajadores.append (('María García', random.randint(300000,2500000)))
    trabajadores.append (('Carlos López', random.randint(300000,2500000)))
    trabajadores.append (('Ana Martínez', random.randint(300000,2500000)))
    trabajadores.append (('Pedro Rodríguez', random.randint(300000,2500000)))
    trabajadores.append (('Laura Hernández', random.randint(300000,2500000)))
    trabajadores.append (('Miguel Sánchez', random.randint(300000,2500000)))
    trabajadores.append (('Isabel Gómez', random.randint(300000,2500000)))
    trabajadores.append (('Francisco Díaz', random.randint(300000,2500000)))
    trabajadores.append (('Elena Fernández', random.randint(300000,2500000)))
    
    with open("AsignaSueldos.csv","a",newline="") as AsignaSueldos:
        controlador = csv.writer(AsignaSueldos)
        controlador.writerow(['María García', random.randint(300000,2500000)])        
        controlador.writerow(['Carlos López', random.randint(300000,2500000)])
        controlador.writerow(['Ana Martínez', random.randint(300000,2500000)])
        controlador.writerow(['Pedro Rodríguez', random.randint(300000,2500000)])
        controlador.writerow(['Laura Hernández', random.randint(300000,2500000)])
        controlador.writerow(['Miguel Sánchez', random.randint(300000,2500000)])
        controlador.writerow(['Isabel Gómez', random.randint(300000,2500000)])
        controlador.writerow(['Francisco Díaz', random.randint(300000,2500000)])
        controlador.writerow(['Elena Fernández', random.randint(300000,2500000)])
    
def imprime():
    categoria1 = []
    categoria2 = []
    categoria3 = []
    total_pagado = 0
    with open('AsignaSueldos.csv', 'r', newline='') as ag: 
        leer_archivo = csv.reader(ag)
            
        for row in leer_archivo:
            empleado, monto = row
            print(f"{empleado}           ${monto}")

    
    #for i in trabajadores:
    #    controlador.writerow(trabajadores)
        


