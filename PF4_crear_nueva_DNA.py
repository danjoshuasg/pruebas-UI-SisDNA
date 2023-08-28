import acciones.acciones_unitarias as acciones_unitarias
import acciones.acciones_movimiento as acciones_movimientos
import acciones.diccionarios_SisDNA as diccionarios

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException
import time


## Ingresar al sistema
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

acciones_movimientos.Ingresar_Sistema(driver, wait)
submodulo="acreditacion"
ventana = "acreditacion"
acciones_movimientos.Ingresar_Modulo_Submodulo(driver, wait, modulo_nombre="dna", submodulo_nombre=submodulo)

diccionario=diccionarios.diccionarios_ACREDITACION(ventana) 
for i in list(diccionario['ingresar_datos'].keys()):
    print(i)
    by =diccionario['ingresar_datos'][i]["By"]
    web_elemento = diccionario['ingresar_datos'][i]["elemento_web"]
    
    print(web_elemento)
    elemento = wait.until(EC.visibility_of_element_located((By.ID, web_elemento)))
    print(f"elemento encontrado de {i} con éxito")

# try:

#     # Mover mouse a la Gestión de DNA
#     casita_gestionDNA= wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-tooltip-content="#tc0"]')))
#     acciones.MoverClick(casita_gestionDNA)

#     # Mover a DNA
#     humanito_DNA = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="https://ws01.mimp.gob.pe/sisdna-web/faces/dna/listado.xhtml"]')))
#     acciones.MoverClick(humanito_DNA)

#     # Hacer click en el botón de nueva DNA
#     button_nueva_DNA = wait.until(EC.presence_of_element_located((By.ID, 'formularioPrincipal1:j_idt182')))
#     MoverClick(button_nueva_DNA)

#     # Seleccionar Sede ("Sede Central")
#     filtro_sede = wait.until(EC.presence_of_element_located((By.ID, 'formNuevaDNA:txtTipo_label')))
#     MoverClick(filtro_sede)
#     sede = wait.until(EC.presence_of_element_located((By.ID, 'formNuevaDNA:txtTipo_1'))) 
#     MoverClick(sede)
    
#     # Seleccionar tipo ("Distrital")
#     filtro_tipo = wait.until(EC.presence_of_element_located((By.ID, 'formNuevaDNA:txtOrigen_label')))
#     MoverClick(filtro_tipo)
#     tipo = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li[data-label="DISTRITAL"]')))
#     MoverClick(tipo)

#     # Ingresar el nombre de la entidad responsable
#     casilla_entidad = wait.until(EC.presence_of_element_located((By.ID,'formNuevaDNA:txtEntidad')))
#     MoverClick(casilla_entidad)
#     casilla_entidad.clear()
#     casilla_entidad.send_keys("Municipalidad Distrital de San Carlos - Prueba")

#     # Ingresar el nombre de la defensoría
#     casilla_nombre = wait.until(EC.presence_of_element_located((By.ID,'formNuevaDNA:txtNombre')))
#     MoverClick(casilla_nombre)
#     casilla_nombre.clear()
#     casilla_nombre.send_keys("Defensoría de la Municipalidad Distrital de San Antonio - Prueba")

#     # Seleccionar el departamento
#     filtro_departamento = wait.until(EC.presence_of_element_located((By.ID,'formNuevaDNA:txtDepartamento_label')))
#     MoverClick(filtro_departamento)
#     departamento = wait.until(EC.presence_of_element_located((By.ID, 'formNuevaDNA:txtDepartamento_12')))
#     MoverClick(departamento)

#     # Seleccionar la provincia
#     filtro_provincia = wait.until(EC.presence_of_element_located((By.ID,'formNuevaDNA:txtProvincia_label')))
#     MoverClick(filtro_provincia)
#     provincia = wait.until(EC.presence_of_element_located((By.ID, 'formNuevaDNA:txtProvincia_4'))) #Huancayo
#     MoverClick(provincia)

#     # Seleccionar el distrito
#     filtro_distrito = wait.until(EC.presence_of_element_located((By.ID,'formNuevaDNA:txtDistrito_label')))
#     MoverClick(filtro_distrito)
#     distrito = wait.until(EC.presence_of_element_located((By.ID, 'formNuevaDNA:txtDistrito_13')))
#     MoverClick(distrito)

#     # Guardar
#     button_guardar_DNA = wait.until(EC.presence_of_element_located((By.ID,'formNuevaDNA:j_idt308')))
#     MoverClick(button_guardar_DNA)


    


    

#     time.sleep(10) #Detener por un tiempo
#     print("Elemento encontrado")

# except NoSuchElementException:
#     print("El elemento no fue encontrado en la página")

acciones_movimientos.Salir_Sistema(driver)
driver.quit()