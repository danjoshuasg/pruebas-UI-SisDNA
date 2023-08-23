
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service




from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
import time

##############################################################################################################
#MOVIMIENTOS EN EL SISTEMA:
#   1. Ingresar SisDNA.
#   2. Salir SisDNA.
#   3. Regresar Home.
#   4. Ingresar Módulo.
#   5. Regresar Módulo.
#   6. Ingresar Submódulo.
#   7. Regresar Submódulo.

##############################################################################################################


def MoverClick(driver, elemento_click):
    try:
        mover_mouse = webdriver.ActionChains(driver)
        mover_mouse.move_to_element(elemento_click).click().perform()
    except Exception as e:
        print("Error en mover click: ",e)
    time.sleep(1)

def MoverClick_wait(driver,wait, elemento_click, css_elemento_wait):
    try:
        mover_mouse = webdriver.ActionChains(driver)
        mover_mouse.move_to_element(elemento_click).click().perform()
        start=time.time()
        elemento_wait = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_elemento_wait)))
        time_step=time.time()-start
        return time_step
    except Exception as e:
        print("Error en mover click wait: ",e)
    

# Darle click al vacío para que funcione
def click_vacio(driver, elemento_vacio ='j_idt22:j_idt24'):
    elemento_vacio = driver.find_element(By.ID,elemento_vacio)
    MoverClick(driver,elemento_vacio)

def limpiar_enviar(wait, id_campo, valor):
    input_user = wait.until(EC.visibility_of_element_located((By.ID, id_campo)))
    input_user.clear()
    input_user.send_keys(valor)

def boton_respuesta_lenta(wait, id_boton, xpath_elemento_esperado):
    try:
        buttom = wait.until(EC.visibility_of_element_located((By.ID, id_boton)))
        buttom.click()
        respuesta = wait.until(EC.presence_of_element_located((By.XPATH, xpath_elemento_esperado)))
        return 1, respuesta.text
    except Exception as e:
        print("El error en boton respuesta es: ",e)

def boton_respuesta_css(driver, css_id_buttom, css_confirm_window):
    buttom=driver.find_element(By.CSS_SELECTOR, css_id_buttom)
    buttom.click()
    confirm_message=driver.find_element(By.CSS_SELECTOR, css_confirm_window)
    return 1, confirm_message.text

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

# # Encontrar un boton y confirmar la entrada a una nueva ventana.

def diccionarios_movimientos(nombre_diccionario="modulos"):
    modulos_SisDNA ={"home":"Inicio",
                     "dna":"0",
                     "riesgo":"1",
                     "mantenimiento":"2",
                     "seguridad":"3"}
    submodulos_SisDNA ={
                    "home":{"url":"Inicio","submodulos":{}, "css_evidencia":"#j_idt54 > h3"},
                    "dna":{
                            "url":"0",
                            "submodulos":{"dna":"/dna/",
                                          "acreditacion":"/acreditacion/",
                                          "supervision":"/supervision/",
                                          "capacitacion programacion":"/capacitacion/curso/",
                                          "capacitacion ejecucion":"/capacitacion/solicitud/",
                                          "reportes":"/reporte/"}
                          }, 
                    "riesgo":{"recepcion":"/demuna/recepcion/",
                                "valoracion":"/demuna/valoracion/",
                                "evaluacion":"/demuna/evaluacion/",
                                "pti":"/demuna/pti/",
                                "reportes":"/demuna/reporte/"},
                    "mantenimiento":{"municipalidades":"/mantenimiento/municipalidad/",
                                        "catalogo":"/mantenimiento/catalogo/",
                                        "parametros":"/mantenimiento/parametro/",
                                        "colegios":"/mantenimiento/colegio/",
                                        "cargainicial":"/mantenimiento/cargainicial/"},
                    "seguridad":{"seguridad":"/seguridad/"}}
    
    diccionarios = {"modulos":modulos_SisDNA, "submodulos":submodulos_SisDNA}
    return diccionarios[nombre_diccionario]

########################################################################################################
# 1. INGRESAR SISDNA.
def Ingresar_Sistema(driver,wait, url_login = "https://ws01.mimp.gob.pe/sisdna-web/faces/login.xhtml", id_login_buttom = "formularioPrincipal:j_idt34",xpath_home_element = "//div[@id='j_idt54']/h3",  username="admin", password="123456"):
    id_username = "formularioPrincipal:username"
    id_password = "formularioPrincipal:password"
    try:
        driver.get(url_login) #Ingresa al URL
        driver.implicitly_wait(5) #Se le adiciona un tiempo de espera adicional para esperar respuesta del servidor
        limpiar_enviar(wait, id_username, username) #Send  username
        limpiar_enviar(wait, id_password, password) #Send password
        n , respuesta = boton_respuesta_lenta(wait, id_login_buttom, xpath_home_element) #Hacerle click al botón y esperar elemento del Home
        print("Ingreso del sistema exitoso: ", respuesta)
        return n 
    except Exception as e:
        print("Error en el ingreso del sistema: ", e)
        return 0
########################################################################################################


########################################################################################################
# 2. SALIR DEL SISTEMA
def Salir_Sistema(driver, css_logout="#j_idt22\:logout", css_confirm_logout = "#formularioPrincipal > div > div:nth-child(1) > div > h1"):
    try:
        n, confirm_message=boton_respuesta_css(driver, css_logout, css_confirm_logout)
        print("Salida del sistema exitosa: ", confirm_message)
        return n
    except Exception as e:
        print("Error en la salida del Sistema: ",e)
        return 0

########################################################################################################

########################################################################################################
# 3. INGRESAR AL MÓDULO Y SUBMÓDULO
## Ingresar al módulo DNA

def Ingresar_Modulo(driver,wait,modulo_nombre="inicio"):
    try:
        modulos_SisDNA ={"inicio":"Inicio","dna":"0","riesgo":"1","mantenimiento":"2","seguridad":"3"}
        if modulo_nombre not in modulos_SisDNA:
            print(f"No existe el módulo '{modulo_nombre}', Debe elegir entre:")
            for modulo in modulos_SisDNA.keys():
                print(modulo)
            pass
        else:
            modulo= wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-tooltip-content="#tc'+ modulos_SisDNA[modulo_nombre] +'"]')))        
            MoverClick(driver,modulo)
            print(f"Éxito en ingresar al módulo {modulo_nombre}:", modulo.text)
    except Exception as e:
        print(f"Error en el ingreso al módulo {modulo_nombre}:", e)
        return 0
########################################################################################################
# 3. INGRESAR AL MÓDULO Y SUBMÓDULO

def Ingresar_Modulo_Submodulo(driver, wait, modulo_nombre="home", submodulo_nombre=None):
    modulos_SisDNA = diccionarios_movimientos("modulos")
    submodulos_SisDNA = diccionarios_movimientos("submodulos")
    
    # Verificar si el módulo existe
    if modulo_nombre not in modulos_SisDNA:
        print(f"No existe el módulo '{modulo_nombre}'. Debe elegir entre:")
        for modulo in modulos_SisDNA.keys():
            print(modulo)
        return
    
    modulo_selector = f'a[data-tooltip-content="#tc{modulos_SisDNA[modulo_nombre]}"]'
    modulo = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, modulo_selector)))
    MoverClick(driver, modulo)
    print(f"Ingreso al módulo ({modulo_nombre}) exitoso: ", )
    
    # Verificar si el submódulo existe
    if submodulo_nombre and submodulo_nombre not in submodulos_SisDNA.get(modulo_nombre, {}):
        print(f"No existe el submódulo '{submodulo_nombre}' en el módulo '{modulo_nombre}'. Debe elegir entre:")
        for submodulo in submodulos_SisDNA.get(modulo_nombre, {}).keys():
            print(submodulo)
        return
    
    if submodulo_nombre:
        direccion = submodulos_SisDNA[modulo_nombre][submodulo_nombre]
        submodulo_selector = f'a[href="https://ws01.mimp.gob.pe/sisdna-web/faces{direccion}listado.xhtml"]'
        submodulo = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, submodulo_selector)))
        MoverClick(driver, submodulo)
        print(f"Ingreso al submódulo ({submodulo_nombre}) exitoso: ")


def Ingresar_click(driver, accion=None, ids_elemento=[], is_xpath=True):
    if accion is None:
        print("Debe ingresar el nombre de la accion")
    else:
        try:
            if is_xpath:
                existe_elemento = probar_xpaths(driver, ids_elemento)
                if existe_elemento is None:
                    print(f"No se puede encontrar el id en {accion}")
                    return 0
                else:
                    MoverClick(driver,existe_elemento)
                    print(f"Éxito en la acción: {accion}")
                    return 1
            else:
                existe_elemento = probar_ids(driver, ids_elemento)
                if existe_elemento is None:
                    print(f"No se puede encontrar el id en {accion}")
                    return 0
                else:
                    MoverClick(driver,existe_elemento)
                    print(f"Éxito en la acción: {accion}")
                    return 1

        except Exception as e:
            print(f"Error en {accion}: ", e)
            return 0
        
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

def Prueba_0(driver,wait):
    
    try:
        # Mover mouse a la Gestión de DNA
        Ingresar_Modulo(driver=driver, wait=wait, modulo_nombre="dna")

        # Mover a DNA
        humanito_DNA = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="https://ws01.mimp.gob.pe/sisdna-web/faces/dna/listado.xhtml"]')))
        MoverClick(driver,humanito_DNA)

        # Seleccionar un departamento en el filtro ("Amazonas")
        filtro_departamento = wait.until(EC.presence_of_element_located((By.ID, 'frmBuscar:busDepartamento_label')))
        MoverClick(driver,filtro_departamento)

        departamento = wait.until(EC.presence_of_element_located((By.ID, 'frmBuscar:busDepartamento_1')))
        texto = departamento.text
        print(texto)
        MoverClick(driver,departamento)
        
        # Seleccionar una provincia en el filtro ("Bagua")
        filtro_provincia = wait.until(EC.presence_of_element_located((By.ID, 'frmBuscar:busProvincia_label')))
        MoverClick(driver,filtro_provincia)

        provincia = wait.until(EC.presence_of_element_located((By.ID, 'frmBuscar:busProvincia_1')))
        MoverClick(driver,provincia)
        
        # Seleccionar una provincia en el filtro ("Aramango")
        filtro_distrito = wait.until(EC.presence_of_element_located((By.ID, 'frmBuscar:busDistrito_label')))
        MoverClick(driver,filtro_distrito)

        distrito = wait.until(EC.presence_of_element_located((By.ID, 'frmBuscar:busDistrito_1')))
        MoverClick(driver,distrito)
        
        # Hacer click a la nada para actulizar
        # click_actualizar= driver.find_element(By.TAG_NAME, 'body')
        # click_actualizar.click()

        time.sleep(5) #Detener por un tiempo
        print("Elemento encontrado")
        return 1
    except ElementNotInteractableException:
        print("El elemento no es interactivo o no está dentro del proceso")
        pass
        return 0
    except TimeoutException:
        print("El elemento no fue encontrado a tiempo")
        pass
        return 0
    
    except NoSuchElementException:
        print("El elemento no fue encontrado en la página")
        return 0

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



def Prueba():
    service = Service()
    # options = webdriver.ChromeOptions()
    # driver = webdriver.Chrome(service=service, options=options)
    
    driver = webdriver.Chrome()
    
    wait = WebDriverWait(driver, 15)
    Ingresar_Sistema(driver,wait,username="72623744",password="123456$$dan")
    time.sleep(5)
    
    Ingresar_Modulo_Submodulo(driver,wait,modulo_nombre="riesgo")
    time.sleep(5)

    Ingresar_Modulo_Submodulo(driver,wait,modulo_nombre="dna",submodulo_nombre="dna")
    time.sleep(5)

    Ingresar_Modulo_Submodulo(driver,wait,modulo_nombre="dna",submodulo_nombre="acreditacion")
    time.sleep(5)

    Salir_Sistema(driver)
    time.sleep(5)
    #Salir_Sistema(driver=driver,wait=wait)
    #time.sleep(5)
    # cont=0
    # cont+=Prueba_0(driver=driver,wait=wait)
    # print("Número de pruebas exitosas: ",cont)
    # driver.implicitly_wait(5)
    driver.quit()



if __name__ == "__main__":
    Prueba()