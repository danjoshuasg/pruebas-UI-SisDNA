from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import acciones.acciones_unitarias as acciones_unitarias
import acciones.acciones_movimiento as acciones_movimiento



class Acciones_Ventanas:
    def __init__(self, ventana, diccionario_ventana):
        if acciones_unitarias.validar_accion(diccionario_ventana):
            self.diccionario_ventana = diccionario_ventana
            self.ventana = ventana 
        else:
            print("Ingrese un diccionario apropiado para las acciones de la ventana")
    def Filtrar(self,campo=None):
        try:
            if campo:
                #Filtrar todos los campos
                print(f"Se filtro el campo {campo} exitosamente")
            else:
                #Filtrar campo especificado
                print(f"Se filtraron todos los campos")

        except Exception as e:
            print("Error en acciones de ventanas:",e)
        # Filtrar

        pass
    def Crear(self):
        pass

    def Funcionalidad_datos(self):
        pass



    


def filtrar():
    print("hola")

def crear():
    print("hola")

def editar():
    print("hola")

def Prueba(driver,wait):
    acciones_movimiento.Ingresar_Sistema(driver,wait)
    acciones_movimiento.Ingresar_Modulo_Submodulo(driver,wait, modulo_nombre="dna",submodulo_nombre="dna")

if __name__ == "__main__":
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver,15)
    Prueba(driver,wait)