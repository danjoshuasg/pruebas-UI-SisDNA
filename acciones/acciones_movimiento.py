
from selenium import webdriver
from selenium import webdriver

# from pruebas-UI-SisDNA.diccionarios.diccionarios_SisDNA import diccionarios_SisDNA

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
#   4. Ingresar módulo y submódulo.

##############################################################################################################
def diccionarios_SisDNA(nombre_diccionario="modulos"):
    # navegacion_SisDNA[nombre_modulo][url]-> direccion modulo
    # navegacion_SisDNA[nombre_modulo][submodulos][nombre_submodulo][url]-> direccion submodulo
    # navegacion_SisDNA[nombre_modulo][submodulos][nombre_submodulo][css_evidencia]-> evidencia de ingreso a submodulo en modulo
    navegacion_SisDNA ={
                        "home":{"url":"Inicio"},
                        "dna":{
                                "url":"0",
                                "submodulos":{"dna":{"url":"/dna/",
                                                     "css_evidencia":"#frmBuscar\:j_idt155 > div > span"},
                                            "acreditacion":{"url":"/acreditacion/",
                                                            "css_evidencia":"#frmBuscar\:j_idt480 > div > span"},
                                            "supervision":{"url":"/supervision/",
                                                           "css_evidencia":"#frmBuscar\:j_idt301 > div > span"},
                                            "capacitacion programacion":{"url":"/capacitacion/curso/",
                                                                         "css_evidencia":"#frmBuscar\:j_idt181 > div.bctitle.clearfix > span"},
                                            "capacitacion ejecucion":{"url":"/capacitacion/solicitud/",
                                                                      "css_evidencia":"#frmBuscar\:j_idt224 > div > span"},
                                            "reporte":{"url":"/reporte/",
                                                       "css_evidencia":"#j_idt57 > div > div > span"}
                                            }
                               }, 
                        "riesgo":{
                                "url":"1",    
                                "submodulos":{  "recepcion":{"url":"/demuna/recepcion/",
                                                             "css_evidencia":"#frmBuscar\:j_idt155 > div > span"},
                                                "valoracion":{"url":"/demuna/valoracion/",
                                                              "css_evidencia":"#frmBuscar\:j_idt155 > div > span"},
                                                "evaluacion":{"url":"/demuna/evaluacion/",
                                                              "css_evidencia":"#frmBuscar\:j_idt155 > div > span"},
                                                "pti":{"url":"/demuna/pti/",
                                                       "css_evidencia":"#frmBuscar\:j_idt155 > div > span"},
                                                "reportes":{"url":"/demuna/reporte/",
                                                            "css_evidencia":"#j_idt57 > div > div > span"},
                                            }
                                },

                        "mantenimiento":{
                                "url":"2",
                                "submodulos":{"municipalidades":{"url":"/mantenimiento/municipalidad/",
                                                            "css_evidencia":"#frmBuscar\:j_idt95 > div.bctitle.clearfix > span"},
                                              "catalogo":{"url":"/mantenimiento/catalogo/",
                                                            "css_evidencia":"#content > section > div.bctitle.clearfix > span"},
                                              "parametros":{"url":"/mantenimiento/parametro/",
                                                            "css_evidencia":"#content > section > div.bctitle.clearfix > span"},
                                              "colegios":{"url":"/mantenimiento/colegio/",
                                                            "css_evidencia":"#content > section > div.bctitle.clearfix > span"},
                                              "carga inicial":{"url":"/mantenimiento/cargainicial/",
                                                                "css_evidencia":"#frmDna > h1"},
                                        }
                                     },
                        "seguridad":{
                                 "url":"3",
                                 "submodulos":{"usuarios":{"url":"/seguridad/",
                                                           "css_evidencia":"#frmGestion\:j_idt58 > div.bctitle.clearfix > span"}
                                              }
                                    }
                        }
    diccionarios = {"navegacion":navegacion_SisDNA}
    return diccionarios[nombre_diccionario]

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
        inicio=time.time()
        elemento_wait = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_elemento_wait)))
        fin=time.time()
        tiempo = fin - inicio
        tiempo_formateado = "{:.{}f}".format(tiempo, 5)
        return tiempo_formateado
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

def Ingresar_Modulo_Submodulo(driver, wait, modulo_nombre="home", submodulo_nombre=None):
    try:     
        navegacion_SisDNA = diccionarios_SisDNA("navegacion")
        modulos_SisDNA = list(navegacion_SisDNA.keys())
        
        
        # Verificar si el módulo existe
        if modulo_nombre not in modulos_SisDNA:
            print(f"No existe el módulo '{modulo_nombre}'. Debe elegir entre:")
            for modulo in modulos_SisDNA.keys():
                print(modulo)
            return

        modulo_selector = f'a[data-tooltip-content="#tc{navegacion_SisDNA[modulo_nombre]["url"]}"]'
        modulo = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, modulo_selector)))
        MoverClick(driver, modulo)
        #print(f"Ingreso al módulo ({modulo_nombre}) exitoso")

        submodulos_modulo = list(navegacion_SisDNA[modulo_nombre]["submodulos"].keys())
        
        # Verificar si el submódulo existe
        if submodulo_nombre and submodulo_nombre not in submodulos_modulo:
            print(f"No existe el submódulo '{submodulo_nombre}' en el módulo '{modulo_nombre}'. Debe elegir entre:")
            for submodulo in submodulos_modulo:
                print(submodulo)
            return
        
        if submodulo_nombre:
            direccion = navegacion_SisDNA[modulo_nombre]["submodulos"][submodulo_nombre]["url"]
            elemento_evidencia = navegacion_SisDNA[modulo_nombre]["submodulos"][submodulo_nombre]["css_evidencia"]
            submodulo_selector = f'a[href="https://ws01.mimp.gob.pe/sisdna-web/faces{direccion}listado.xhtml"]'
            submodulo = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, submodulo_selector)))
            tiempo = MoverClick_wait(driver, wait, submodulo, elemento_evidencia)
            print(f"Ingreso al submódulo ({submodulo_nombre}) en el módulo ({modulo_nombre}) exitoso: tiempo ({tiempo}) segundos")
    except Exception as e:
        print("Error en Ingresar módulo submódulo: ",e)
        pass

########################################################################################################

def Prueba():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)
    #Ingresar_Sistema(driver,wait,username="72623744",password="123456$$dan")
    Ingresar_Sistema(driver,wait)
    time.sleep(5)
    
    # Ingresar_Modulo_Submodulo(driver,wait,modulo_nombre="riesgo")
    # time.sleep(5)

    # Ingresar_Modulo_Submodulo(driver,wait,modulo_nombre="dna",submodulo_nombre="supervision")
    # time.sleep(5)

    # Ingresar_Modulo_Submodulo(driver,wait,modulo_nombre="dna",submodulo_nombre="dna")
    # time.sleep(5)

    # Ingresar_Modulo_Submodulo(driver,wait,modulo_nombre="dna",submodulo_nombre="acreditacion")
    # time.sleep(5)

    # Ingresar_Modulo_Submodulo(driver,wait,modulo_nombre="dna",submodulo_nombre="capacitacion programacion")
    # time.sleep(5)

    Ingresar_Modulo_Submodulo(driver,wait,modulo_nombre="seguridad",submodulo_nombre="usuarios")
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