
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


def Ingresar_Sistema(driver,wait, url_login = "https://ws01.mimp.gob.pe/sisdna-web/faces/login.xhtml", user_name="admin", password="123456"):
    driver.get(url_login)
    print(driver.title)
    driver.implicitly_wait(5)
    
    input_user = wait.until(EC.visibility_of_element_located((By.ID, "formularioPrincipal:username")))
    input_user.clear()
    input_user.send_keys(user_name)

    input_password = wait.until(EC.visibility_of_element_located((By.ID, "formularioPrincipal:password")))
    input_password.clear()
    input_password.send_keys(password)

    button = wait.until(EC.visibility_of_element_located((By.ID, "formularioPrincipal:j_idt34")))
    button.click()

    respuesta_home = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='j_idt54']/h3")))
    print(respuesta_home.text)


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
            mover_mouse = webdriver.ActionChains(driver)
            mover_mouse.move_to_element(modulo)
            mover_mouse.perform()
            mover_mouse.move_to_element(modulo).click().perform()
            time.sleep(2)
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

def Ingresar_Submodulo(driver,wait,modulo_nombre="dna",submodulo_nombre="dna"):
    submodulos_SisDNA ={"dna":{"dna":"/dna/","acreditacion":"/acreditacion/","supervision":"/supervision/","capacitacion_programacion":"/capacitacion/curso/","capacitacion_ejecucion":"/capacitacion/solicitud/","reportes":"/reporte/"}, 
                        "riesgo":{"recepcion":"/demuna/recepcion/","valoracion":"/demuna/valoracion/","evaluacion":"/demuna/evaluacion/","pti":"/demuna/pti/","reportes":"/demuna/reporte/"},
                        "mantenimiento":{"municipalidades":"/mantenimiento/municipalidad/","catalogo":"/mantenimiento/catalogo/","parametros":"/mantenimiento/parametro/","colegios":"/mantenimiento/colegio/","cargainicial":"/mantenimiento/cargainicial/"},
                        "seguridad":"/seguridad/"}
    
    Ingresar_Modulo(driver,wait,modulo_nombre=modulo_nombre)
    if submodulo_nombre not in submodulos_SisDNA[modulo_nombre]:
        print(f"No existe el submódulo '{submodulo_nombre}' en el módulo '{modulo_nombre}', Debe elegir entre:")
        for submodulo in submodulos_SisDNA[modulo_nombre].keys():
            print(submodulo)
        pass
    else:
        direccion = submodulos_SisDNA[modulo_nombre][submodulo_nombre]
        submodulo = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="https://ws01.mimp.gob.pe/sisdna-web/faces'+direccion+'listado.xhtml"]')))
        MoverClick(driver,submodulo)

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
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)
    Ingresar_Sistema(driver=driver,wait=wait)
    cont=0
    cont+=Prueba_0(driver=driver,wait=wait)
    print("Número de pruebas exitosas: ",cont)
    driver.implicitly_wait(5)
    driver.quit()



if __name__ == "__main__":
    Prueba()