import acciones.acciones_comunes as acciones_comunes
import time
import filtros
import borrar_filtros

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

#Ingresar al sistema y al modulo
def Prueba_AC2():

    try:
        inicio = time.time()
        acciones_comunes.Ingresar_Sistema(driver=driver, wait=wait, user_name="72623744", password="123456$$dan") 
        acciones_comunes.Ingresar_Submodulo(driver=driver, wait=wait, modulo_nombre="dna", submodulo_nombre="acreditacion")

        filtros.Filtrar_vencer_acreditacion(driver, wait)
        filtros.Filtrar_codigo(driver,wait, codigo_DNA="0100")
        acciones_comunes.Ingresar_supervision(driver=driver, wait=wait, nueva=True)

        time.sleep(10)

        final = time.time()
        print("Prueba de filtros exitosa, tiempo de ejecución: ", final - inicio, " segundos")
        return 1
    except Exception as e:
        print("Error en la prueba: ", e)
        return 0
    finally:
        driver.quit()