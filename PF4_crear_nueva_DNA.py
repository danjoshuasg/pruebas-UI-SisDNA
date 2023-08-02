from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException
import time

def MoverClick(elemento):
    mover_mouse = webdriver.ActionChains(driver)
    mover_mouse.move_to_element(elemento)
    mover_mouse.perform()
    mover_mouse.move_to_element(elemento).click().perform()
    time.sleep(2)

## Ingresar al sistema
driver = webdriver.Chrome()
driver.get("https://ws01.mimp.gob.pe/sisdna-web/faces/login.xhtml")
print(driver.title)
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
input_user = wait.until(EC.visibility_of_element_located((By.ID, "formularioPrincipal:username")))
input_user.clear()
input_user.send_keys("admin")

input_password = wait.until(EC.visibility_of_element_located((By.ID, "formularioPrincipal:password")))
input_password.clear()
input_password.send_keys("123456")

button = wait.until(EC.visibility_of_element_located((By.ID, "formularioPrincipal:j_idt34")))
button.click()

respuesta_home = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='j_idt56']/p")))
print(respuesta_home.text)

try:

    # Mover mouse a la Gestión de DNA
    casita_gestionDNA= wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-tooltip-content="#tc0"]')))
    MoverClick(casita_gestionDNA)

    # Mover a DNA
    humanito_DNA = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="https://ws01.mimp.gob.pe/sisdna-web/faces/dna/listado.xhtml"]')))
    MoverClick(humanito_DNA)

    # Hacer click en el botón de nueva DNA
    button_nueva_DNA = wait.until(EC.presence_of_element_located((By.ID, 'formularioPrincipal1:j_idt182')))
    MoverClick(button_nueva_DNA)

    # Seleccionar Sede ("Sede Central")
    filtro_sede = wait.until(EC.presence_of_element_located((By.ID, 'formNuevaDNA:txtTipo_label')))
    MoverClick(filtro_sede)
    sede = wait.until(EC.presence_of_element_located((By.ID, 'formNuevaDNA:txtTipo_1'))) 
    MoverClick(sede)
    
    # Seleccionar tipo ("Distrital")
    filtro_tipo = wait.until(EC.presence_of_element_located((By.ID, 'formNuevaDNA:txtOrigen_label')))
    MoverClick(filtro_tipo)
    tipo = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li[data-label="DISTRITAL"]')))
    MoverClick(tipo)

    # Ingresar el nombre de la entidad responsable
    casilla_entidad = wait.until(EC.presence_of_element_located((By.ID,'formNuevaDNA:txtEntidad')))
    MoverClick(casilla_entidad)
    casilla_entidad.clear()
    casilla_entidad.send_keys("Municipalidad Distrital de San Carlos - Prueba")

    # Ingresar el nombre de la defensoría
    casilla_nombre = wait.until(EC.presence_of_element_located((By.ID,'formNuevaDNA:txtNombre')))
    MoverClick(casilla_nombre)
    casilla_nombre.clear()
    casilla_nombre.send_keys("Defensoría de la Municipalidad Distrital de San Antonio - Prueba")

    # Seleccionar el departamento
    filtro_departamento = wait.until(EC.presence_of_element_located((By.ID,'formNuevaDNA:txtDepartamento_label')))
    MoverClick(filtro_departamento)
    departamento = wait.until(EC.presence_of_element_located((By.ID, 'formNuevaDNA:txtDepartamento_12')))
    MoverClick(departamento)

    # Seleccionar la provincia
    filtro_provincia = wait.until(EC.presence_of_element_located((By.ID,'formNuevaDNA:txtProvincia_label')))
    MoverClick(filtro_provincia)
    provincia = wait.until(EC.presence_of_element_located((By.ID, 'formNuevaDNA:txtProvincia_4'))) #Huancayo
    MoverClick(provincia)

    # Seleccionar el distrito
    filtro_distrito = wait.until(EC.presence_of_element_located((By.ID,'formNuevaDNA:txtDistrito_label')))
    MoverClick(filtro_distrito)
    distrito = wait.until(EC.presence_of_element_located((By.ID, 'formNuevaDNA:txtDistrito_13')))
    MoverClick(distrito)

    # Guardar
    button_guardar_DNA = wait.until(EC.presence_of_element_located((By.ID,'formNuevaDNA:j_idt308')))
    MoverClick(button_guardar_DNA)


    


    

    time.sleep(10) #Detener por un tiempo
    print("Elemento encontrado")

except NoSuchElementException:
    print("El elemento no fue encontrado en la página")


driver.implicitly_wait(10)
driver.quit()