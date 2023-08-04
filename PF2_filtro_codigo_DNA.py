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

    # Seleccionar input Código de DNA
    input_ID_DNA= wait.until(EC.presence_of_element_located((By.ID, 'frmBuscar:txtCodigo')))
    input_ID_DNA.clear()
    input_ID_DNA.send_keys("01001")

    elemento_click = wait.until(EC.presence_of_element_located((By.ID, 'j_idt22:j_idt24'))) # Observación: Con hacerle click al Logo del SisDNA sale el cuadro
    MoverClick(elemento_click)

    # Hacer click e

    time.sleep(5) #Detener por un tiempo
    print("Elemento encontrado")





except NoSuchElementException:
    print("El elemento no fue encontrado en la página")


driver.implicitly_wait(5)
driver.quit()