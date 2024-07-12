import random
import csv
from funciones import Menu, AsignaSueldo

def main():
    while True:
        op=Menu()
        if op=="5":
            print("")
            print("Finalizando programa...")
            print("Desarrollado por Ricardo Antonio Galdames Soto")
            print("RUT 12.723.716-6")
            break
        elif op=="1":
            AsignaSueldo()
            

  
if __name__=="__main__":
    main()



