
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

    respuesta_home = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='j_idt56']/p")))
    print(respuesta_home.text)


## Ingresar al módulo DNA

# dna_link = wait.until(EC.presence_of_element_located((By.XPATH, "//form[@id='j_idt38:0:j_idt40']/div[2]/ul/li[2]/a")))
# print(dna_link.text)

# Verificar si estoy entrando al enlace de DNA correctamente:

def Ingresar_Modulo(driver,wait,modulo_nombre="inicio"):
    modulos_SisDNA ={"inicio":"Inicio","dna":"0","riesgo":"1","mantenimiento":"2","seguridad":"3"}
    if modulo_nombre not in modulos_SisDNA:
        print("Error al elegir el nombre del módulo, Debe elegir entre:")
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

def Ingresar_Submodulo(driver,wait,modulo_nombre="dna",submodulo_nombre="dna"):
    submodulos_SisDNA ={"dna":{"dna":"/dna/","acreditacion":"/acreditacion/","supervision":"/supervision/","capacitacion_programacion":"/capacitacion/curso/","capacitacion_ejecucion":"/capacitacion/solicitud/","reportes":"/reporte/"}, 
                        "riesgo":{"recepcion":"/demuna/recepcion/","valoracion":"/demuna/valoracion/","evaluacion":"/demuna/evaluacion/","pti":"/demuna/pti/","reportes":"/demuna/reporte/"},
                        "mantenimiento":{"municipalidades":"/mantenimiento/municipalidad/","catalogo":"/mantenimiento/catalogo/","parametros":"/mantenimiento/parametro/","colegios":"/mantenimiento/colegio/","cargainicial":"/mantenimiento/cargainicial/"},
                        "seguridad":"/seguridad/"}
    
    Ingresar_Modulo(driver,wait,modulo_nombre=modulo_nombre)
    if submodulo_nombre not in submodulos_SisDNA[modulo_nombre]:
        print("Error al elegir el nombre del submódulo, Debe elegir entre:")
        for submodulo in submodulos_SisDNA[modulo_nombre].keys():
            print(submodulo)
        pass
    else:
        direccion = submodulos_SisDNA[modulo_nombre][submodulo_nombre]
        submodulo = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="https://ws01.mimp.gob.pe/sisdna-web/faces'+direccion+'listado.xhtml"]')))
        MoverClick(driver,submodulo)


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

def Desplegar():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    Ingresar_Sistema(driver=driver,wait=wait)
    cont=0
    cont+=Prueba_0(driver=driver,wait=wait)
    print("Número de pruebas exitosas: ",cont)
    driver.implicitly_wait(5)
    driver.quit()


if __name__ == "__main__":
    Desplegar()