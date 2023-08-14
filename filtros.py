import json
import acciones_comunes

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException


import time


def Filtrar_ubigeo(driver, wait, departamento="Amazonas",provincia=None, distrito=None, ubigeo_file='ubigeo.json'):
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
            acciones_comunes.MoverClick(driver,filtro_departamento)
            for id in range(n_departamentos):
                departamento = wait.until(EC.presence_of_element_located((By.ID, "frmBuscar:busDepartamento_"+str(id))))
                if departamento.text == departamento_buscar:
                    print(departamento.text)
                    acciones_comunes.MoverClick(driver,departamento)
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
            acciones_comunes.MoverClick(driver,filtro_departamento)
            for id in range(n_departamentos):
                departamento = wait.until(EC.presence_of_element_located((By.ID, "frmBuscar:busDepartamento_"+str(id))))
                if departamento.text == departamento_buscar:
                    print(departamento.text)
                    acciones_comunes.MoverClick(driver,departamento)
                    break

            filtro_provincia = wait.until(EC.presence_of_element_located((By.ID, id_frm_provincia)))
            acciones_comunes.MoverClick(driver,filtro_provincia)
            for id in range(n_provincias):
                provincia = wait.until(EC.presence_of_element_located((By.ID, "frmBuscar:busProvincia_"+str(id))))
                if provincia.text == provincia_buscar:
                    print(provincia.text)
                    acciones_comunes.MoverClick(driver,provincia)
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
            acciones_comunes.MoverClick(driver,filtro_departamento)
            for id in range(n_departamentos):
                departamento = wait.until(EC.presence_of_element_located((By.ID, "frmBuscar:busDepartamento_"+str(id))))
                if departamento.text == departamento_buscar:
                    print(departamento.text)
                    acciones_comunes.MoverClick(driver,departamento)
                    break
                       
            filtro_provincia = wait.until(EC.presence_of_element_located((By.ID, id_frm_provincia)))
            acciones_comunes.MoverClick(driver,filtro_provincia)
            for id in range(n_provincias):
                provincia = wait.until(EC.presence_of_element_located((By.ID, "frmBuscar:busProvincia_"+str(id))))
                if provincia.text == provincia_buscar:
                    print(provincia.text)
                    acciones_comunes.MoverClick(driver,provincia)
                    break

            filtro_distrito = wait.until(EC.presence_of_element_located((By.ID, id_frm_distrito)))
            acciones_comunes.MoverClick(driver,filtro_distrito)
            for id in range(n_distritos):
                distrito = wait.until(EC.presence_of_element_located((By.ID, "frmBuscar:busDistrito_"+str(id))))
                if distrito.text == distrito_buscar:
                    print(distrito.text)
                    acciones_comunes.MoverClick(driver,distrito)
                    break
    except TimeoutException:
        print("El submódulo no tiene el filtro de distrito")
        pass

# Filtrado del código de la DNA

def Filtrar_codigo(driver, codigo_DNA="'01001"):
    id_frm_Codigo = ["frmBuscar:txtCodigo","frmBuscar:busCodigo"]
    input_ID_DNA = acciones_comunes.probar_ids(driver,id_frm_Codigo)
    if input_ID_DNA is None:
        print("El ID del filtro de codigo DNA no fue encontrado")
    else:    
        input_ID_DNA.clear()
        input_ID_DNA.send_keys(codigo_DNA)
        acciones_comunes.click_vacio(driver)
        print("Codigo de DNA encontrado")


# Borrar todos los filtros

def Borrar_filtros(driver,wait):

    #Borrar filtro de ubigeo
    id_frm_departamento = ['frmBuscar:busDepartamento_label']
    id_sin_departamento= 'frmBuscar:busDepartamento_0'
    existe_filtro_departamento = acciones_comunes.probar_ids(driver,id_frm_departamento)

    if existe_filtro_departamento is None:
        print("El ID del filtro del departamento no fue encontrado")
    else:
        acciones_comunes.MoverClick(driver,existe_filtro_departamento)
        sin_departamento = wait.until(EC.presence_of_element_located((By.ID, id_sin_departamento)))
        acciones_comunes.MoverClick(driver,sin_departamento)
        print("Filtro del ubigeo limpio")


    #Borrar el filtro del código
    id_frm_Codigo = ["frmBuscar:txtCodigo","frmBuscar:busCodigo"]
    existe_filtro_codigo = acciones_comunes.probar_ids(driver,id_frm_Codigo)
    if existe_filtro_codigo is None:
        print("El ID del filtro de codigo DNA no fue encontrado")
    else:    
        existe_filtro_codigo.clear()
        acciones_comunes.click_vacio(driver)
        print("Filtro del código limpio")

    #Borrar el estado de la DNA
    id_frm_estado = ["frmBuscar:busEstado_label","frmBuscar:txtEstadoBus"]
    id_sin_estado = "frmBuscar:busEstado_0"
    existe_estado = acciones_comunes.probar_ids(driver,id_frm_estado)
    if existe_estado is None:
        print("El ID del filtro de estado DNA no fue encontrado")
    else:
        acciones_comunes.MoverClick(driver,existe_estado)
        sin_estado = wait.until(EC.presence_of_element_located((By.ID, id_sin_estado)))
        acciones_comunes.MoverClick(driver,sin_estado)
        print("Filtro del estado limpio")

    #Borrar la fecha de supervision
    id_frm_fecha_desde=["frmBuscar:j_idt331_input"]
    id_frm_fecha_hasta=["frmBuscar:j_idt336_input"]
    existe_fecha_desde = acciones_comunes.probar_ids(driver,id_frm_fecha_desde)
    existe_fecha_hasta = acciones_comunes.probar_ids(driver,id_frm_fecha_hasta)

    if existe_fecha_desde is None:
        print("El ID del filtro de fecha 'desde' no fue encontrado")
    else:
        acciones_comunes.MoverClick(driver,existe_fecha_desde)
        existe_fecha_desde.clear()
        print("Filtro de fecha 'desde' limpio")
    
    if existe_fecha_hasta is None:
        print("El ID del filtro de fecha 'hasta' no fue encontrado")
    else:
        acciones_comunes.MoverClick(driver,existe_fecha_hasta)
        existe_fecha_hasta.clear()
        print("Filtro de fecha 'hasta' limpio")

    #Borrar el supervisor
    id_frm_supervisor=["frmBuscar:selSupervisor_label"]
    id_sin_supervisor="frmBuscar:selSupervisor_0"
    existe_supervisor = acciones_comunes.probar_ids(driver,id_frm_supervisor)
    if existe_supervisor is None:
        print("El ID del supervisor no fue encontrado")
    else:
        acciones_comunes.MoverClick(driver,existe_supervisor)
        sin_supervisor = wait.until(EC.presence_of_element_located((By.ID, id_sin_supervisor)))
        acciones_comunes.MoverClick(driver,sin_supervisor)
        print("Filtro del supervisor limpio")









## Filtros específicos ##

def Filtrar_estado_DNA(driver, wait, estado="ACREDITADA"): #¿Solo está en el submódulo de la DNA?
    id_frm_estado = "frmBuscar:txtEstadoBus"
    diccionario_estados ={"NO ACREDITADA":"frmBuscar:txtEstadoBus_1", 
                          "NO_OPERATIVA":"frmBuscar:txtEstadoBus_2", 
                          "ACREDITADA":"frmBuscar:txtEstadoBus_3"}
    if estado not in diccionario_estados:
        print("El estado de la DNA no es válido")
    else: 
        id_estado=diccionario_estados[estado]
        filtro_estado = driver.find_element(By.ID, id_frm_estado)
        acciones_comunes.MoverClick(driver,filtro_estado)
        estado=wait.until(EC.presence_of_element_located((By.ID, id_estado)))
        acciones_comunes.MoverClick(driver,estado)
        print("Filtrado del estado de la DNA exitoso")

def Filtrar_estado_acreditacion(driver, wait, estado="ACREDITADA"): #¿Solo está en el submódulo de la DNA?
    id_frm_estado = "frmBuscar:txtEstadoBus"
    diccionario_estados ={"EVALUACIÓN DE EXPEDIENTE":"frmBuscar:txtEstadoBus_1", 
                          "OBSERVADA":"frmBuscar:txtEstadoBus_2", 
                          "EVALUACIÓN DE SUBSANACIÓN":"frmBuscar:txtEstadoBus_3", 
                          "ACREDITADA":"frmBuscar:txtEstadoBus_4", 
                          "DENEGADA":"frmBuscar:txtEstadoBus_5"}
    if estado not in diccionario_estados:
        print("El estado de la DNA en acreditación no es válido")
    else: 
        id_estado=diccionario_estados[estado]
        filtro_estado = driver.find_element(By.ID, id_frm_estado)
        acciones_comunes.MoverClick(driver,filtro_estado)
        estado=wait.until(EC.presence_of_element_located((By.ID, id_estado)))
        acciones_comunes.MoverClick(driver,estado)
        print("Filtrado del estado de la acreditación exitoso")

def Filtrar_estado_supervision(driver, wait, estado='EN PROCESO'):
    id_frm_estado = "frmBuscar:busEstado_label"
    diccionario_estados ={"CONCLUIDO":"frmBuscar:busEstado_1", "EN PROCESO":"frmBuscar:busEstado_2"}
    if estado not in diccionario_estados:
        print("El estado de la DNA en supervisión no es válido")
    else:
        id_estado=diccionario_estados[estado]
        filtro_estado = driver.find_element(By.ID, id_frm_estado)
        acciones_comunes.MoverClick(driver,filtro_estado)
        estado=wait.until(EC.presence_of_element_located((By.ID, id_estado)))
        acciones_comunes.MoverClick(driver,estado)
        print("Filtrado del estado de la DNA exitoso")


def Filtrar_vencer_acreditacion(driver, wait, estado_vencer="TODAS"):
    id_frm_vencer="frmBuscar:selFiltroAcre_label"
    diccionario_vencer={"POR VENCER":"frmBuscar:selFiltroAcre_0","TODAS":"frmBuscar:selFiltroAcre_1"}
    if estado_vencer not in diccionario_vencer:
        print("El estado de la DNA no es válido, ingrese uno de los siguientes elementos:")
        for estado in list(diccionario_vencer.keys()):
            print(estado)

    else: 
        id_estado=diccionario_vencer[estado_vencer]
        filtro_estado = driver.find_element(By.ID, id_frm_vencer)
        acciones_comunes.MoverClick(driver,filtro_estado)
        estado=wait.until(EC.presence_of_element_located((By.ID, id_estado)))
        acciones_comunes.MoverClick(driver,estado)
        print("Filtrado del estado a vencer de la acreditación exitoso")


def Filtrar_anio_capacitacion(driver,wait, year="2023"):
    id_frm_year="frmBuscar:txtAnio_input"

# Filtrar por fechas
def validar_fecha(fecha_str):
    try:
        # Intentamos convertir la fecha a un objeto datetime
        datetime.strptime(fecha_str, '%d/%m/%Y')
        return True
    except ValueError:
        # Si se genera una excepción, la fecha no es válida
        print("La fecha no es válida.")
        return False

def validar_fecha_posterior(fecha1, fecha2):
    try:
        fecha1 = datetime.strptime(fecha1, '%d/%m/%Y')
        fecha2 = datetime.strptime(fecha2, '%d/%m/%Y')
        return fecha1 > fecha2
    except ValueError:
        # Si se genera una excepción, una de las fechas no es válida
        print("La fecha de 'hasta' debe ser mayor a la de 'desde'")
        return False

def Filtrar_fechas_supervision(driver, wait, desde=None, hasta = None):
    id_frm_fecha_desde="frmBuscar:j_idt331_input"
    id_frm_fecha_hasta="frmBuscar:j_idt336_input"    
    if hasta is None:
        if validar_fecha(desde):
            filtro_fecha_desde = wait.until(EC.presence_of_element_located((By.ID, id_frm_fecha_desde)))
            acciones_comunes.MoverClick(driver,filtro_fecha_desde)
            filtro_fecha_desde.clear()
            filtro_fecha_desde.send_keys(desde)
            acciones_comunes.click_vacio(driver)

        
    elif desde is None:
        if validar_fecha(hasta):
            filtro_fecha_hasta= wait.until(EC.presence_of_element_located((By.ID, id_frm_fecha_hasta)))
            acciones_comunes.MoverClick(driver,filtro_fecha_hasta)
            filtro_fecha_hasta.clear()
            filtro_fecha_hasta.send_keys(hasta)
            acciones_comunes.click_vacio(driver)

    elif hasta is None and desde is None:
        print("Ingrese una fecha hasta y/o desde")
    
    else:
        
        if validar_fecha(desde) and validar_fecha(hasta) and validar_fecha_posterior(hasta, desde):
            filtro_fecha_desde = wait.until(EC.presence_of_element_located((By.ID, id_frm_fecha_desde)))
            acciones_comunes.MoverClick(driver,filtro_fecha_desde)
            filtro_fecha_desde.clear()
            filtro_fecha_desde.send_keys(desde)
            acciones_comunes.click_vacio(driver)

            filtro_fecha_hasta= wait.until(EC.presence_of_element_located((By.ID, id_frm_fecha_hasta)))
            acciones_comunes.MoverClick(driver,filtro_fecha_hasta)
            filtro_fecha_hasta.clear()
            filtro_fecha_hasta.send_keys(hasta)
            acciones_comunes.click_vacio(driver)


def Filtrar_supervisores(driver, wait, supervisor="NORA"):
    id_frm_supervisor ="frmBuscar:selSupervisor_label"
    diccionario_supervisores ={"DAVID":"frmBuscar:selSupervisor_7",
                               "NORA":"frmBuscar:selSupervisor_8",
                               "MARCOS":"frmBuscar:selSupervisor_21",
                               "CRISTIAN":"frmBuscar:selSupervisor_41"}
    if supervisor not in diccionario_supervisores:
        print("El supervisor no es válido")
    else: 
        id_supervisor=diccionario_supervisores[supervisor]
        filtro_supervisor = driver.find_element(By.ID, id_frm_supervisor)
        acciones_comunes.MoverClick(driver,filtro_supervisor)
        supervisor=wait.until(EC.presence_of_element_located((By.ID, id_supervisor)))
        acciones_comunes.MoverClick(driver,supervisor)
        print("Filtrado del supervisor fue exitoso")


    #Corregir si la fecha es correcta


        
    

def Probar():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 5)
    acciones_comunes.Ingresar_Sistema(driver=driver,wait=wait, user_name="72623744", password="123456$$dan") 
    acciones_comunes.Ingresar_Submodulo(driver=driver,wait=wait, modulo_nombre="dna",submodulo_nombre="acreditacion")
    #Filtrar_ubigeo(driver=driver,wait=wait, departamento="AREQUIPA", provincia="AREQUIPA", distrito="QUEQUEÑA")
    #Filtrar_codigo(driver=driver, codigo_DNA="20011")
    #Filtrar_estado_DNA(driver,wait,estado="NO ACREDITADA")
    Filtrar_estado_acreditacion(driver,wait,estado="OBSERVADA")
    Filtrar_vencer_acreditacion(driver,wait)

    time.sleep(2)
    driver.quit()


if __name__=="__main__":
    Probar()
