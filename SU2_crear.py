import prueba_funcional
import time
import filtros
import borrar_filtros

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 6)

#Ingresar al sistema y al modulo
def Prueba():
    try:
        inicio = time.time()
        prueba_funcional.Ingresar_Sistema(driver=driver, wait=wait, user_name="72623744", password="123456$$dan") 
        prueba_funcional.Ingresar_Submodulo(driver=driver, wait=wait, modulo_nombre="dna", submodulo_nombre="supervision")

        filtros.Filtrar_supervisores(driver=driver, wait=wait, supervisor="DAVID")
        prueba_funcional.Ingresar_supervision(driver=driver, wait=wait, nueva=True)

        time.sleep(10)

        final = time.time()
        print("Prueba de filtros exitosa, tiempo de ejecución: ", final - inicio, " segundos")
    except Exception as e:
        print("Error en la prueba: ", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    Prueba()