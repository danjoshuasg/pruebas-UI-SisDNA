import json
import prueba_funcional

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException

import time


def Buscar_ubigeo(driver, wait, departamento="Amazonas",provincia=None, distrito=None, ubigeo_file='ubigeo.json'):
    with open(ubigeo_file, 'r', encoding='utf-8') as json_file:
        diccionario_ubigeo = json.load(json_file)

    id_frm_departamento = 'frmBuscar:busDepartamento_label'
    id_frm_provincia = 'frmBuscar:busProvincia_label'
    id_frm_distrito= 'frmBuscar:busDistrito_label'
    
    departamento_buscar = departamento
    provincia_buscar = provincia
    distrito_buscar = distrito
    try:
        if provincia is None and distrito is None:

            if departamento_buscar not in diccionario_ubigeo:
                print(f"El departamento '{departamento_buscar}' no se encuentra en el ubigeo")
                exit(1)
            else:
                n_departamentos=len(diccionario_ubigeo)
                
            filtro_departamento = wait.until(EC.presence_of_element_located((By.ID, id_frm_departamento)))
            prueba_funcional.MoverClick(driver,filtro_departamento)
            for id in range(n_departamentos):
                departamento = wait.until(EC.presence_of_element_located((By.ID, "frmBuscar:busDepartamento_"+str(id))))
                if departamento.text == departamento_buscar:
                    print(departamento.text)
                    prueba_funcional.MoverClick(driver,departamento)
                    break
        
        elif distrito is None:
            if departamento_buscar not in diccionario_ubigeo:
                print(f"El departamento '{departamento_buscar}' no se encuentra en el ubigeo")
                exit(1)
            else:
                n_departamentos=len(diccionario_ubigeo)
                if provincia_buscar not in diccionario_ubigeo[departamento_buscar]:
                    print(f"El departamento '{provincia_buscar}' no se encuentra en el ubigeo")
                    exit(1)
                else:
                    n_provincias=len(diccionario_ubigeo[departamento_buscar])
            
            filtro_departamento = wait.until(EC.presence_of_element_located((By.ID, id_frm_departamento)))
            prueba_funcional.MoverClick(driver,filtro_departamento)
            for id in range(n_departamentos):
                departamento = wait.until(EC.presence_of_element_located((By.ID, "frmBuscar:busDepartamento_"+str(id))))
                if departamento.text == departamento_buscar:
                    print(departamento.text)
                    prueba_funcional.MoverClick(driver,departamento)
                    break

            filtro_provincia = wait.until(EC.presence_of_element_located((By.ID, id_frm_provincia)))
            prueba_funcional.MoverClick(driver,filtro_provincia)
            for id in range(n_provincias):
                provincia = wait.until(EC.presence_of_element_located((By.ID, "frmBuscar:busProvincia_"+str(id))))
                if provincia.text == provincia_buscar:
                    print(provincia.text)
                    prueba_funcional.MoverClick(driver,provincia)
                    break

            
        else:
            if departamento_buscar not in diccionario_ubigeo:
                print(f"El departamento '{departamento_buscar}' no se encuentra en el ubigeo")
                exit(1)
            else:
                n_departamentos=len(diccionario_ubigeo)
                if provincia_buscar not in diccionario_ubigeo[departamento_buscar]:
                    print(f"La provincia '{provincia_buscar}' no se encuentra en el ubigeo")
                    exit(1)
                else:
                    n_provincias=len(diccionario_ubigeo[departamento_buscar])
                    if distrito_buscar not in diccionario_ubigeo[departamento_buscar][provincia_buscar]:
                        print(f"El distrito '{distrito_buscar}' no se encuentra en el ubigeo")
                        exit(1)
                    else:
                        n_distritos=len(diccionario_ubigeo[departamento_buscar][provincia_buscar])

            filtro_departamento = wait.until(EC.presence_of_element_located((By.ID, id_frm_departamento)))
            prueba_funcional.MoverClick(driver,filtro_departamento)
            for id in range(n_departamentos):
                departamento = wait.until(EC.presence_of_element_located((By.ID, "frmBuscar:busDepartamento_"+str(id))))
                if departamento.text == departamento_buscar:
                    print(departamento.text)
                    prueba_funcional.MoverClick(driver,departamento)
                    break
                       
            filtro_provincia = wait.until(EC.presence_of_element_located((By.ID, id_frm_provincia)))
            prueba_funcional.MoverClick(driver,filtro_provincia)
            for id in range(n_provincias):
                provincia = wait.until(EC.presence_of_element_located((By.ID, "frmBuscar:busProvincia_"+str(id))))
                if provincia.text == provincia_buscar:
                    print(provincia.text)
                    prueba_funcional.MoverClick(driver,provincia)
                    break

            filtro_distrito = wait.until(EC.presence_of_element_located((By.ID, id_frm_distrito)))
            prueba_funcional.MoverClick(driver,filtro_distrito)
            for id in range(n_distritos):
                distrito = wait.until(EC.presence_of_element_located((By.ID, "frmBuscar:busDistrito_"+str(id))))
                if distrito.text == distrito_buscar:
                    print(distrito.text)
                    prueba_funcional.MoverClick(driver,distrito)
                    break
    except TimeoutException:
        print("El submódulo no tiene el filtro de distrito")
        pass

def probar_ids(driver, ids):
    for id in ids:
        try:
            elemento=driver.find_element(By.ID,id)
            return elemento
        except ElementNotInteractableException:
            continue
        except NoSuchElementException:
            continue
        except TimeoutException:
            continue
    return None

def click_vacio(driver, elemento_vacio ='j_idt22:j_idt24'):
    elemento_vacio = driver.find_element(By.ID,elemento_vacio)
    prueba_funcional.MoverClick(driver,elemento_vacio)
    

def Buscar_codigo(driver, codigo_DNA="'01001"):
    id_frm_Codigo = ["frmBuscar:txtCodigo","frmBuscar:busCodigo"]
    input_ID_DNA = probar_ids(driver,id_frm_Codigo)
    if input_ID_DNA is None:
        print("El ID del filtro de codigo DNA no fue encontrado")
    else:    
        input_ID_DNA.clear()
        input_ID_DNA.send_keys(codigo_DNA)
        click_vacio(driver)
        print("Codigo de DNA encontrado")

## Filtros específicos ##

def Buscar_estado_DNA(driver, wait, estado="ACREDITADA"): #¿Solo está en el submódulo de la DNA?
    id_frm_estado = "frmBuscar:txtEstadoBus"
    diccionario_estados ={"NO ACREDITADA":"frmBuscar:txtEstadoBus_1", "NO_OPERATIVA":"frmBuscar:txtEstadoBus_2", "ACREDITADA":"frmBuscar:txtEstadoBus_3"}
    if estado not in diccionario_estados:
        print("El estado de la DNA no es válido")
    else: 
        id_estado=diccionario_estados[estado]
        filtro_estado = driver.find_element(By.ID, id_frm_estado)
        prueba_funcional.MoverClick(driver,filtro_estado)
        estado=wait.until(EC.presence_of_element_located((By.ID, id_estado)))
        prueba_funcional.MoverClick(driver,estado)
        print("Filtrado del estado de la DNA exitoso")

def Buscar_estado_acreditacion(driver, wait, estado="ACREDITADA"): #¿Solo está en el submódulo de la DNA?
    id_frm_estado = "frmBuscar:txtEstadoBus"
    diccionario_estados ={"EVALUACIÓN DE EXPEDIENTE":"frmBuscar:txtEstadoBus_1", "OBSERVADA":"frmBuscar:txtEstadoBus_2", "ACREDITADA":"frmBuscar:txtEstadoBus_3"}
    if estado not in diccionario_estados:
        print("El estado de la DNA no es válido")
    else: 
        id_estado=diccionario_estados[estado]
        filtro_estado = driver.find_element(By.ID, id_frm_estado)
        prueba_funcional.MoverClick(driver,filtro_estado)
        estado=wait.until(EC.presence_of_element_located((By.ID, id_estado)))
        prueba_funcional.MoverClick(driver,estado)
        print("Filtrado del estado de la DNA exitoso")



def Probar():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 5)
    prueba_funcional.Ingresar_Sistema(driver=driver,wait=wait, user_name="72623744", password="123456$$dan") 
    prueba_funcional.Ingresar_Submodulo(driver=driver,wait=wait, modulo_nombre="dna",submodulo_nombre="dna")
    #Buscar_ubigeo(driver=driver,wait=wait, departamento="AREQUIPA", provincia="AREQUIPA", distrito="QUEQUEÑA")
    #Buscar_codigo(driver=driver, codigo_DNA="20011")
    #Buscar_estado_DNA(driver,wait,estado="NO ACREDITADA")


    time.sleep(2)
    driver.quit()


if __name__=="__main__":
    Probar()
