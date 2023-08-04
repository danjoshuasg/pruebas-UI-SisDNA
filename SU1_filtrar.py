import prueba_funcional
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

#Ingresar al sistema y al modulo
def Prueba():
    prueba_funcional.Ingresar_Sistema(driver=driver,wait=wait, user_name="72623744", password="123456$$dan") 
    prueba_funcional.Ingresar_Submodulo(driver=driver,wait=wait, modulo_nombre="dna",submodulo_nombre="supervision")
    input_ID_DNA= wait.until(EC.presence_of_element_located((By.ID, 'frmBuscar:busCodigo')))
    input_ID_DNA.clear()
    input_ID_DNA.send_keys("01001")
    time.sleep(5)

#Ubigeo
#def Filtrado(tipo="ubigeo",departamento="Amazonas",provincia="Chachapoyas", distrito="Chachapoyas"):
#    prueba_funcional.



#Codigo 

#Estado

if __name__=="__main__":
    Prueba()
