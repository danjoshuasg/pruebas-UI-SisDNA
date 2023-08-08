import prueba_funcional
import time
import filtros
import borrar_filtros

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

#Ingresar al sistema y al modulo
def Prueba():
    inicio=time.time()
    prueba_funcional.Ingresar_Sistema(driver=driver,wait=wait, user_name="72623744", password="123456$$dan") 
    prueba_funcional.Ingresar_Submodulo(driver=driver,wait=wait, modulo_nombre="dna",submodulo_nombre="supervision")

    filtros.Filtrar_ubigeo(driver=driver,wait=wait,departamento="AMAZONAS",provincia="CHACHAPOYAS", distrito="CHACHAPOYAS")
    borrar_filtros.Borrar_filtros(driver=driver,wait=wait,filtro="Filtrar_ubigeo")

    filtros.Filtrar_codigo(driver=driver,codigo_DNA="01002")
    borrar_filtros.Borrar_filtros(driver=driver,wait=wait,filtro="Filtrar_codigo")

    filtros.Filtrar_estado_supervision(driver=driver,wait=wait)
    borrar_filtros.Borrar_filtros(driver=driver,wait=wait,filtro="Filtrar_estado_supervision")

    filtros.Filtrar_fechas_supervision(driver=driver, wait=wait,desde='01/02/2023', hasta='03/07/2023')
    borrar_filtros.Borrar_filtros(driver=driver,wait=wait,filtro="Filtrar_fechas_supervision")

    filtros.Filtrar_supervisores(driver=driver,wait=wait, supervisor="NORA")
    borrar_filtros.Borrar_filtros(driver=driver,wait=wait,filtro="Filtrar_supervisores")

    final=time.time()
    print("Prueba de filtros exitosa, tiempo de ejecución: ",final-inicio," segundos")

if __name__=="__main__":
    Prueba()