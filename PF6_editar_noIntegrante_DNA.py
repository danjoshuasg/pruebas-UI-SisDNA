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
nombre_buscar = "Defensoría de la Municipalidad Distrital de San Antonio - Prueba"
Departamento_buscar = "LIMA"
Provincia_buscar="LIMA"
Distrito_buscar="VILLA MARIA DEL TRIUNFO"

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

    departamento = wait.until(EC.presence_of_element_located((By.ID, 'frmBuscar:busDepartamento_3')))
    MoverClick(departamento)
    
    # Seleccionar una provincia en el filtro ("Bagua")
    filtro_provincia = wait.until(EC.presence_of_element_located((By.ID, 'frmBuscar:busProvincia_label')))
    MoverClick(filtro_provincia)

    provincia = wait.until(EC.presence_of_element_located((By.ID, 'frmBuscar:busProvincia_3')))
    MoverClick(provincia)
    
     # Seleccionar una provincia en el filtro ("Aramango")
    filtro_distrito = wait.until(EC.presence_of_element_located((By.ID, 'frmBuscar:busDistrito_label')))
    MoverClick(filtro_distrito)

    distrito = wait.until(EC.presence_of_element_located((By.ID, 'frmBuscar:busDistrito_3')))
    MoverClick(distrito)

    # Entrar a la ventana de edición
    boton_editar = wait.until(EC.presence_of_element_located((By.ID, 'formularioPrincipal1:tablaDefensoria:0:j_idt185')))
    MoverClick(boton_editar)

    # Editar campos

    # 1. Dirección de la DNA
    input_direccion = wait.until(EC.presence_of_element_located((By.ID,'frmNuevo:txtDireccion')))
    MoverClick(input_direccion)
    input_direccion.clear()
    input_direccion.send_keys("Dirección de prueba 1")

    # 2. frmNuevo:txtNroOrdenanza
    input_NroOrdenanza = wait.until(EC.presence_of_element_located((By.ID,'frmNuevo:txtNroOrdenanza')))
    MoverClick(input_NroOrdenanza)
    input_NroOrdenanza.clear()
    input_NroOrdenanza.send_keys("N° 00000000000")

    # 3. frmNuevo:txtFecOrdenanza  05/08/2016
    input_FecOrdenanza = wait.until(EC.presence_of_element_located((By.ID,'frmNuevo:txtFecOrdenanza_input')))
    MoverClick(input_FecOrdenanza)
    input_FecOrdenanza.clear()
    input_FecOrdenanza.send_keys("05/08/2016")

    # 4. frmNuevo:txtGerencia
    input_Gerencia = wait.until(EC.presence_of_element_located((By.ID,'frmNuevo:txtGerencia')))
    MoverClick(input_Gerencia)
    input_Gerencia.clear()
    input_Gerencia.send_keys("Subgerencia de Pruebas")

    # 5. frmNuevo:txtCorreo
    input_Correo = wait.until(EC.presence_of_element_located((By.ID,'frmNuevo:txtCorreo')))
    MoverClick(input_Correo)
    input_Correo.clear()
    input_Correo.send_keys("sisdna@mimp.gob.pe")

    # 6. frmNuevo:txtTelefono
    input_Telefono = wait.until(EC.presence_of_element_located((By.ID,'frmNuevo:txtTelefono')))
    MoverClick(input_Telefono)
    input_Telefono.clear()
    input_Telefono.send_keys("0000000000")

    # 7. frmNuevo:txtDias
    input_Dias = wait.until(EC.presence_of_element_located((By.ID,'frmNuevo:txtDias')))
    MoverClick(input_Dias)
    input_Dias.clear()
    input_Dias.send_keys("L-V:8 am - 4pm")

    # 8. frmNuevo:txtFecAcreditacion_input
    input_FecAcreditacion = wait.until(EC.presence_of_element_located((By.ID,'frmNuevo:txtFecAcreditacion_input')))
    MoverClick(input_FecAcreditacion)
    input_FecAcreditacion.clear()
    input_FecAcreditacion.send_keys("12/08/2018")

    # 9. frmNuevo:txtResAcreditacion
    input_ResAcreditacion = wait.until(EC.presence_of_element_located((By.ID,'frmNuevo:txtResAcreditacion')))
    MoverClick(input_ResAcreditacion)
    input_ResAcreditacion.clear()
    input_ResAcreditacion.send_keys("RM N° 0000000")

    # 10. frmNuevo:txtFecSupervision_input
    input_FecSupervision = wait.until(EC.presence_of_element_located((By.ID,'frmNuevo:txtFecSupervision_input')))
    MoverClick(input_FecSupervision)
    input_FecSupervision.clear()
    input_FecSupervision.send_keys("15/12/2020")

    # 11. frmNuevo:selEstadoDna_label  frmNuevo:selEstadoDna_1
    input_EstadoDropdown = wait.until(EC.presence_of_element_located((By.ID,'frmNuevo:selEstadoDna_label')))
    MoverClick(input_EstadoDropdown)
    estado = wait.until(EC.presence_of_element_located((By.ID,'frmNuevo:selEstadoDna_3')))
    MoverClick(estado)

    # 12. frmNuevo:txtobservaciones
    input_Observaciones = wait.until(EC.presence_of_element_located((By.ID,'frmNuevo:txtobservaciones')))
    MoverClick(input_Observaciones)
    input_Observaciones.clear()
    input_Observaciones.send_keys("Muchas observaciones.")

    # Guardar
    button_guardar = driver.find_element(By.ID, 'frmNuevo:j_idt153')
    acciones = ActionChains(driver)
    acciones.move_to_element(button_guardar).perform()
    acciones.move_to_element(button_guardar).double_click().perform()

    print("Elemento encontrado")





except NoSuchElementException:
    print("El elemento no fue encontrado en la página")


driver.implicitly_wait(5)
driver.quit()