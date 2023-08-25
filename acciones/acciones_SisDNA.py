import acciones.acciones_comunes as acciones_comunes
import filtros

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# def filtrar_supervisiones(driver, wait, filtros):



# Ingresa a los filtros de supervisión (Función tipo click)
def ingresar_supervisiones(driver, wait):
    accion = "ingresar supervisiones"
    id_supervision_fila =["//*[@id='formularioPrincipal1:tablaSup_data']/tr[1]/td[1]/div/span[1]",  #Cuando existe más de una DNA filtrada
                            "//*[@id='formularioPrincipal1:tablaSup_data']/tr/td[1]/div/span[1]"] #Caso contrario
    acciones_comunes.Ingresar_click(driver, wait, accion, id_supervision_fila)

# Ingresa a los filtros de supervisión (Función tipo click)
def crear_supervision(driver, wait):
    accion = "crear supervision"
    id_crear_supervision =["//*[@id='formularioPrincipal1:tablaSup:0:j_idt365']/span[1]"]
    acciones_comunes.Ingresar_click(driver, wait, accion, id_crear_supervision)
    