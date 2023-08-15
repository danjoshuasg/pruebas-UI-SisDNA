import time
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


##############################################################################################################
#FILTROS DISPONIBLES:
#   1. Filtrar ubigeo.
#       Observaciones:
#       - Revisar que la dirección del ubigeo.json sea correcta y esté actualizada. Caso contrario revisar el 
#         ubigeo_excel.xlsx y crear con crear_ubigeo.py
#   2. Filtro código.
#       Observaciones:
#       - 
#   3. Filtrar estados.
#   4. Filtrar fechas.
#   5. Filtrar encargados (personas).
##############################################################################################################


##############################################################################################################
# 1. FILTRAR UBIGEO

### Funciones auxiliares
def cargar_diccionario_json(ubigeo_file='ubigeo.json'):
    with open(ubigeo_file, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)

def validar_ubigeo(diccionario_ubigeo, ubicacion, nivel):
    if ubicacion not in diccionario_ubigeo:
        print(f"El/la {nivel} '{ubicacion}' no se encuentra en el ubigeo")
        exit(1)


def seleccionar_elemento_en_desplegable(driver, wait, id_desplegable, n_ids, elemento_buscado):
    try:
        filtro = wait.until(EC.presence_of_element_located((By.ID, id_desplegable)))
        #Se elimina el string "label" a fin de reusarlo
        string_eliminado = ["label"]
        texto_cortado = id_desplegable.split("_")
        id_elemento_encontrado = []
        for i in texto_cortado:
            if i not in string_eliminado:
                id_elemento_encontrado.append(i)
        id_elemento_encontrado = " ".join(id_elemento_encontrado)

        acciones_comunes.MoverClick(driver,filtro)
        for id in range(n_ids):
            elemento_encontrado = wait.until(EC.presence_of_element_located((By.ID, id_elemento_encontrado+"_"+str(id))))
            if elemento_encontrado.text == elemento_buscado:
                print(elemento_encontrado.text)
                acciones_comunes.MoverClick(driver,elemento_encontrado)
                break
    except TimeoutException:
        print("No se encuentra el filtro de distrito, por favor elimínelo de su búsqueda.")

    except Exception as e:
        print("Se encontró un error en seleccionar desplegable ubigeo: ",e)    
    pass

### Funcion principal

def Filtrar_ubigeo(driver, wait, departamento="Amazonas",provincia=None, distrito=None, ubigeo_file='ubigeo.json'):
    diccionario_ubigeo = cargar_diccionario_json(ubigeo_file)

    id_frm_departamento = 'frmBuscar:busDepartamento_label'
    id_frm_provincia = 'frmBuscar:busProvincia_label'
    id_frm_distrito= 'frmBuscar:busDistrito_label'
    
    try:
        n_departamentos = len(diccionario_ubigeo)

        validar_ubigeo(diccionario_ubigeo, departamento, "departamento")
        seleccionar_elemento_en_desplegable(driver, wait, id_frm_departamento, n_departamentos, departamento)
        
        if provincia is not None:
            n_provincias = len(diccionario_ubigeo[departamento])
            
            validar_ubigeo(diccionario_ubigeo[departamento], provincia, "provincia")
            seleccionar_elemento_en_desplegable(driver, wait, id_frm_provincia, n_provincias, provincia)
            
            if distrito is not None:
                n_distritos = len(diccionario_ubigeo[departamento][provincia])
                
                validar_ubigeo(diccionario_ubigeo[departamento][provincia], distrito, "distrito")
                seleccionar_elemento_en_desplegable(driver, wait, id_frm_distrito, n_distritos, distrito)

    except Exception as e:
        print("Error en filtrar ubigeo:", e)

##############################################################################################################


##############################################################################################################
# 2. FILTRAR CODIGO

# Funciones auxiliares

def click_send(driver, nombre_campo, ids_input , input):
    id_input_valido = acciones_comunes.probar_ids(driver,ids_input)
    if id_input_valido is None:
        print(f"El ID del campo {nombre_campo } no fue encontrado")
    else:    
        id_input_valido.clear()
        id_input_valido.send_keys(input)
        acciones_comunes.click_vacio(driver)
        print(f"Éxito: Enviar {input} al campo '{nombre_campo}'")

# Función principal
def Filtrar_codigo(driver, nombre_campo="codigo",codigo_DNA="'01001"):
    ids_frm_Codigo = ["frmBuscar:txtCodigo","frmBuscar:busCodigo"]
    click_send(driver, nombre_campo, ids_frm_Codigo , codigo_DNA)

##############################################################################################################


##############################################################################################################
# 3. FILTRAR ESTADO

# Funcion principal
def Filtrar_estado(driver, wait, submodulo="acreditacion", estado="ACREDITADA"):
    try:
        diccionario_modulos =["dna","acreditacion","vencer acreditacion","supervision"]
        if submodulo=="dna":
            id_desplegable = "frmBuscar:txtEstadoBus"
            diccionario_estados ={"NO ACREDITADA":"frmBuscar:txtEstadoBus_1", 
                          "NO OPERATIVA":"frmBuscar:txtEstadoBus_2", 
                          "ACREDITADA":"frmBuscar:txtEstadoBus_3"}
            acciones_comunes.seleccionar_desplegable_estado(driver,wait,submodulo,id_desplegable, diccionario_estados, estado)

        elif submodulo=="acreditacion":
            id_desplegable = "frmBuscar:txtEstadoBus"
            diccionario_estados ={"EVALUACIÓN DE EXPEDIENTE":"frmBuscar:txtEstadoBus_1", 
                                "OBSERVADA":"frmBuscar:txtEstadoBus_2", 
                                "EVALUACIÓN DE SUBSANACIÓN":"frmBuscar:txtEstadoBus_3", 
                                "ACREDITADA":"frmBuscar:txtEstadoBus_4", 
                                "DENEGADA":"frmBuscar:txtEstadoBus_5"}
            acciones_comunes.seleccionar_desplegable_estado(driver,wait,submodulo,id_desplegable, diccionario_estados, estado)
        
        elif submodulo=="acreditacion vencer":
            id_desplegable="frmBuscar:selFiltroAcre_label"
            diccionario_estados={"POR VENCER":"frmBuscar:selFiltroAcre_0","TODAS":"frmBuscar:selFiltroAcre_1"}
            acciones_comunes.seleccionar_desplegable_estado(driver,wait,submodulo,id_desplegable, diccionario_estados, estado)
            
        elif submodulo=="supervision proceso":
            id_desplegable = ""
            print("Hola")


        elif submodulo=="supervision proceso":
            id_desplegable = "frmBuscar:busEstado_label"
            diccionario_estados ={"CONCLUIDO":"frmBuscar:busEstado_1", "EN PROCESO":"frmBuscar:busEstado_2"}
            acciones_comunes.seleccionar_desplegable_estado(driver,wait,submodulo,id_desplegable, diccionario_estados, estado)

        

        else:
            print(f"Nombre del módulo {submodulo} no es válido, solo se aceptan los siguientes:")
            for modulos_validos in diccionario_modulos:
                print(modulos_validos)


    except Exception as e:
        print(f"Error en {submodulo}: ",e)
##############################################################################################################



##############################################################################################################
# 4. FILTRAR FECHA

# Funciones auxiliares
def validar_fecha(fecha_str):
    try:
        # Intentamos convertir la fecha a un objeto datetime
        datetime.strptime(fecha_str, '%d/%m/%Y')
        return True
    except ValueError:
        # Si se genera una excepción, la fecha no es válida
        print("La fecha no es válida.")
        return False

def comparar_fechas(fecha_mayor, fecha_menor):
    try:
        fecha_mayor = datetime.strptime(fecha_mayor, '%d/%m/%Y')
        fecha_menor = datetime.strptime(fecha_menor, '%d/%m/%Y')
        return fecha_mayor > fecha_menor
    except ValueError:
        # Si se genera una excepción, una de las fechas no es válida
        print("La fecha de 'hasta' debe ser mayor a la de 'desde'")
        return False

# Funcion principal
def Filtrar_fechas(driver, desde=None, hasta = None):
    try:
        ids_frm_fecha_desde=["frmBuscar:j_idt331_input", "frmBuscar:busFechaIni_input"]
        id_frm_fecha_hasta=["frmBuscar:j_idt336_input"]
        if hasta is None:
            if validar_fecha(desde):
                click_send(driver, nombre_campo="fecha desde", ids_input=ids_frm_fecha_desde , input=desde)

            
        elif desde is None:
            if validar_fecha(hasta):
                click_send(driver, nombre_campo="fecha hasta", ids_input=id_frm_fecha_hasta , input=hasta)

        elif hasta is None and desde is None:
            print("Ingrese una fecha hasta y/o desde")
        
        else:
            
            if validar_fecha(desde) and validar_fecha(hasta) and comparar_fechas(hasta, desde):
                click_send(driver, nombre_campo="fecha desde", ids_input=ids_frm_fecha_desde , input=desde)
                click_send(driver, nombre_campo="fecha hasta", ids_input=id_frm_fecha_hasta , input=hasta)

    except Exception as e:
        print("Error en filtrar fechas: ",e)
##############################################################################################################


##############################################################################################################
# 5. FILTRAR ENCARGADOS


def Filtrar_encargados(driver, wait, encargado="DAVID ARTEAGA RODRÍGUEZ"):
    
    id_frm_supervisor ="frmBuscar:selSupervisor_label"              
    n_ids = 82 # Construir una función que extraiga directamente este número o de un json de usuarios dsld.
    seleccionar_elemento_en_desplegable(driver, wait, id_frm_supervisor, n_ids, encargado)
##############################################################################################################




def get_users_dsld():
    diccionario = {"supervision":["CRISTIAN MARTÍNEZ LUCAS","DAVID ARTEAGA RODRÍGUEZ","MARCOS ERNESTO DELFIN CACHIQUE"], 
                   "acreditacion":["SOLEDAD MERCADO ORELLANA", "LUCÍA MEJÍA DÍAZ"], 
                   "capacitacion":["RUBÉN VERDE CÉSPEDES", "CARMEN HUAMALÍ ROJAS"]}
    return diccionario


def Probar(user = "72623744", password= "123456$$dan", modulo_nombre="dna", submodulo_nombre = "acreditacion", id_encargado=0, test_id=1):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 5)
    diccionario_encargados = get_users_dsld()
    #encargado = diccionario_encargados[submodulo_nombre][id_encargado]
    acciones_comunes.Ingresar_Sistema(driver=driver,wait=wait, user_name=user, password=password) 
    acciones_comunes.Ingresar_Submodulo(driver=driver,wait=wait, modulo_nombre=modulo_nombre,submodulo_nombre=submodulo_nombre)
    if test_id == 1:
        Filtrar_codigo(driver=driver, codigo_DNA="01006")
    elif test_id == 2:
        Filtrar_ubigeo(driver=driver,wait=wait, departamento="LIMA", provincia="LIMA", distrito="SAN JUAN DE MIRAFLORES")
    elif test_id == 3:
        Filtrar_fechas(driver,desde="01/02/2023", hasta="03/04/2023")
    elif test_id == 4:
        Filtrar_estado(driver,wait, submodulo="acreditacion vencer", estado="POR VENCER")
    #elif test_id ==5:
        #Filtrar_encargados(driver,wait,encargado=encargado)
    

    time.sleep(2)
    driver.quit()


if __name__=="__main__":
    # modulos = ["supervision","acreditacion"]
    # for i in range(100):
    #     for m in modulos:
    #         for j in range(5):

    #Probar(submodulo_nombre = "acreditacion", id_encargado=0, test_id=4)
    Probar(submodulo_nombre = "acreditacion", test_id=4)
