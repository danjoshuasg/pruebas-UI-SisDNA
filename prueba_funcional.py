
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

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

## Ingresar al módulo DNA

# dna_link = wait.until(EC.presence_of_element_located((By.XPATH, "//form[@id='j_idt38:0:j_idt40']/div[2]/ul/li[2]/a")))
# print(dna_link.text)

# Verificar si estoy entrando al enlace de DNA correctamente:
try:

    # Mover mouse a la Gestión de DNA
    casita_gestionDNA= wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-tooltip-content="#tc0"]')))
    
    mover_mouse = webdriver.ActionChains(driver)
    mover_mouse.move_to_element(casita_gestionDNA)
    mover_mouse.perform()
    mover_mouse.move_to_element(casita_gestionDNA).click().perform()

    time.sleep(2)

    # Mover a DNA
    humanito_DNA = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="https://ws01.mimp.gob.pe/sisdna-web/faces/dna/listado.xhtml"]')))
    MoverClick(humanito_DNA)

    # Seleccionar un departamento en el filtro ("Amazonas")
    filtro_departamento = wait.until(EC.presence_of_element_located((By.ID, 'frmBuscar:busDepartamento_label')))
    MoverClick(filtro_departamento)

    departamento = wait.until(EC.presence_of_element_located((By.ID, 'frmBuscar:busDepartamento_1')))
    MoverClick(departamento)
    
    # Seleccionar una provincia en el filtro ("Bagua")
    filtro_provincia = wait.until(EC.presence_of_element_located((By.ID, 'frmBuscar:busProvincia_label')))
    MoverClick(filtro_provincia)

    provincia = wait.until(EC.presence_of_element_located((By.ID, 'frmBuscar:busProvincia_1')))
    MoverClick(provincia)
    
     # Seleccionar una provincia en el filtro ("Aramango")
    filtro_distrito = wait.until(EC.presence_of_element_located((By.ID, 'frmBuscar:busDistrito_label')))
    MoverClick(filtro_distrito)

    distrito = wait.until(EC.presence_of_element_located((By.ID, 'frmBuscar:busDistrito_1')))
    MoverClick(distrito)
    
    # Hacer click a la nada para actulizar
    # click_actualizar= driver.find_element(By.TAG_NAME, 'body')
    # click_actualizar.click()

    time.sleep(5) #Detener por un tiempo
    print("Elemento encontrado")





except NoSuchElementException:
    print("El elemento no fue encontrado en la página")


driver.implicitly_wait(5)
driver.quit()