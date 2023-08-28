import acciones_movimiento
import diccionarios_SisDNA

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
import time


def MoverClick(driver, elemento):
    mover_mouse = webdriver.ActionChains(driver)
    mover_mouse.move_to_element(elemento)
    mover_mouse.perform()
    mover_mouse.move_to_element(elemento).click().perform()
    time.sleep(1)

# Darle click al vacío para que funcione
def click_vacio(driver, elemento_vacio ='j_idt22:j_idt24'):
    elemento_vacio = driver.find_element(By.ID,elemento_vacio)
    MoverClick(driver,elemento_vacio)
    

# Encontrar el ID existente sino retornar nulo.
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



def seleccionar_desplegable_estado(driver, wait, modulo, id_desplegable, diccionario_estados, estado):
    try:
        if estado not in diccionario_estados:
            print(f"El estado {estado} de la DNA en el módulo de {modulo} no es válido, ingrese los siguientes estados:")
            for estado in list(diccionario_estados.keys()):
                print(estado)
        else:
            id_estado=diccionario_estados[estado]
            filtro_estado = driver.find_element(By.ID, id_desplegable)
            MoverClick(driver,filtro_estado)
            estado_click=wait.until(EC.presence_of_element_located((By.ID, id_estado)))
            MoverClick(driver,estado_click)
            print(f"Éxito en el filtrado del estado {estado} de la DNA en el módulo de {modulo}")
    except Exception as e:
        print("Error en seleccionar desplegable estado: ",e)


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

def probar_xpaths(driver, xpaths):
    for xpath in xpaths:
        try:
            elemento=driver.find_element(By.XPATH,xpath)
            return elemento
        except ElementNotInteractableException:
            continue
        except NoSuchElementException:
            continue
        except TimeoutException:
            continue
    return None

def Ingresar_supervision(driver, wait, nueva=False):
    id_supervision_fila =["//*[@id='formularioPrincipal1:tablaSup_data']/tr[1]/td[1]/div/span[1]", 
                          "//*[@id='formularioPrincipal1:tablaSup_data']/tr/td[1]/div/span[1]"]
    existe_supervision_fila = probar_xpaths(driver=driver, xpaths=id_supervision_fila)
    if existe_supervision_fila is None:
        print("No se puede encontrar el id de supervision")
    else:
        MoverClick(driver,existe_supervision_fila)
        print("Se encontró una supervisión")
        if nueva:
            id_nueva_supervision ="//*[@id='formularioPrincipal1:tablaSup:0:j_idt365']/span[1]"
            boton_nueva=driver.find_element(By.XPATH,id_nueva_supervision)
            MoverClick(driver,boton_nueva)
            elemento = wait.until(EC.presence_of_element_located((By.ID, "frmNuevo:j_idt57")))
            print("Se creará una nueva supervisión")


#########################  ACCIONES MODULOS  #########################
def validar_accion(diccionario_accion):
    lista_keys = ["By","elemento_web","tipo"]
    valido = list(diccionario_accion.keys()) == lista_keys
    if valido:
        return valido 
    else:
        print("No es un diccionario con acciones válidas")
        return

def click_send(driver, nombre_campo, ids_input , input):
    id_input_valido = probar_ids(driver,ids_input)
    if id_input_valido is None:
        print(f"El ID del campo {nombre_campo } no fue encontrado")
    else:    
        id_input_valido.clear()
        id_input_valido.send_keys(input)
        click_vacio(driver)
        print(f"Éxito: Enviar {input} al campo '{nombre_campo}'")

def clean_send(driver, campo, valor_campo):
        inicio = time.time()  
        campo.clear()
        campo.send_keys(valor_campo)
        click_vacio(driver)
        fin = time.time()
        tiempo = fin - inicio
        tiempo_formateado = "{:.{}f}".format(tiempo, 5)
        print(f"Éxito: Se envió el '{valor_campo}' al campo '{campo}' en ({tiempo_formateado}) segundos")


def validar_tipo(diccionario, tipo):
    if diccionario["tipo"] !=tipo:
        print(f"Elija un campo tipo {tipo}")
        return
    else:
        pass


def accion_send(driver, diccionario_campo, valor_campo):
    try:
        by = diccionario_campo["By"]
        elemento_web = diccionario_campo["elemento_web"]
        campo = driver.find_element(by,elemento_web)
        clean_send(driver,campo, valor_campo)
    except Exception as e:
        print("Error en 'accion send': ",e)


def elemento_presente(wait, elemento_web, By_name=By.ID):
    try:
        elemento=wait.until(EC.presence_of_element_located((By_name, elemento_web)))
        return elemento
    except:
        return None

def registrar_opciones(driver,wait, diccionario_campo):
    try: 

        opciones = {}

        campo_web = diccionario_campo["elemento_web"]
        by = diccionario_campo["By"]

        #Input: frmPersona:txtColegio_label | Output: frmPersona:txtColegio_ (opcion formato)
        string_eliminado = ["label"]
        texto_cortado = campo_web.split("_")

        opcion_formato= []
        for i in texto_cortado:
            if i not in string_eliminado:
                opcion_formato.append(i)
        opcion_formato = " ".join(opcion_formato)

        #Abrir el desplegable
        filtro_campo = wait.until(EC.presence_of_element_located((by, campo_web)))
        MoverClick(driver, filtro_campo)

        #Input: frmPersona:txtColegio_ | Output: {"Texto 1":frmPersona:txtColegio_1, "Texto 2":frmPersona:txtColegio_2 ... "Texto 3": frmPersona:txtColegio_n} (Diccionario de opciones)
        for i in range(50): # Máximo número de opciones a buscar dentro de un desplegable

            opcion_web = opcion_formato+str(i)
            opcion = elemento_presente(wait, opcion_web, By_name=by)
            if opcion:
                opciones[opcion.text] = {"By":by,"elemento_web":opcion_web,"tipo":"click"}
            else:
                print("No se encontraron más opciones")
                break

        return opciones

    except Exception as e:
        print("Error en 'registrar opciones': ",e)


def accion_choose(driver, wait, diccionario_campo, valor_opcion=1):
    try:
        registrar_opciones(driver, wait, diccionario_campo)
    except Exception as e:
        print("Error en 'accion choose': ",e)

######################################################################

def Prueba(driver,wait):
    acciones_movimiento.Ingresar_Sistema(driver,wait)
    acciones_movimiento.Ingresar_Modulo_Submodulo(driver,wait,modulo_nombre="dna",submodulo_nombre="dna")
    # Si elijo el submodulo "dna" debo jalar inmediatamente el diccionario de las ventanas "diccionarios_DNA"
    diccionario_ventanas_submodulo = ["DNA","ACREDITACION","SUPERVISION","CAPACITACION"]
    # Si elijo una venta de DNA tipo "DNA" debo jalar los campos con las funcionaes que puedo realizar dentro 
    lista_ventanas_DNA= diccionarios_SisDNA.diccionarios_DNA()

    diccionario_ventana = diccionarios_SisDNA.diccionarios_DNA(lista_ventanas_DNA[0])

    lista_operaciones = list(diccionario_ventana.keys())

    diccionario_operaciones = diccionario_ventana[lista_operaciones[0]]

    print(list(diccionario_operaciones.key()))
    acciones_movimiento.Salir_Sistema(driver)

if __name__ == "__main__":
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)
    Prueba(driver,wait)