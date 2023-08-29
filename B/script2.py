
from selenium import webdriver


# from pruebas-UI-SisDNA.diccionarios.diccionarios_SisDNA import diccionarios_SisDNA

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from acciones.acciones_movimiento import Ingresar_Sistema

# llamando  a ingresar sistema
def Proof(driver,wait):
    Ingresar_Sistema(driver,wait)
    driver.quit()


driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)
Proof(driver,wait)