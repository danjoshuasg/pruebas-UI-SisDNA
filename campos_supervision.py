import prueba_funcional
import time
import filtros
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import StaleElementReferenceException


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

#Ingresar Colegiatura Responsable

def ingresar_campo_supervision(driver, wait, campo=None, valor =None):
    diccionario_inputs={"Fecha_input":["frmNuevo:txtFecha_input",0],
                        "Hora_input":["frmNuevo:txtHora_input",1],
                        #DNA
                        "Direccion_DNA_input":["frmNuevo:j_idt80",1],
                        "Telefono_DNA_input":["frmNuevo:j_idt92",1],
                        "Correo_DNA_input":["frmNuevo:j_idt95",1],
                        "Horario_DNA_input":["frmNuevo:j_idt98",1],
                        "Autoridad_DNA_input":["frmNuevo:txtAutRes",1],
                        "Direccion_autoridad_DNA_input":["frmNuevo:txtDirResp",1],
                        #RESPONSABLE
                        "DNI_responsable_input":["frmNuevo:j_idt102",1],
                        "Fecha_responsable_input":["frmNuevo:txtFechaCargo_input",0],
                        "Doc_responsable_input":["frmNuevo:txtDocDesignacion",1],
                        "Telefono_responsable_input":["frmNuevo:txtTelefono",1],
                        "Correo_responsable_input":["frmNuevo:txtCorreo",1],
                        #INFRAESTRUCTURA
                        "Ambientes_infraestructura_input":["frmNuevo:txtNumAmb_input",1],
                        #RRHH
                        "Tabla_rrhh_input":["frmNuevo:j_idt162_data",1], #Tratamiento especial
                        #ACTIVIDADES DE LA DNA
                        "Texto_promocion_actividades":["frmNuevo:txtActividades",1],
                        "Texto_otros_actividades":["frmNuevo:txtCoordinadora",1],
                        #COMENTARIOS
                        "Texto_comentarios":["frmNuevo:j_idt261",1],
                        #ENTREVISTADO
                        "DNI_entrevistado_input":["frmNuevo:txtEntDni",1],
                        "Cargo_entrevistado_input":["frmNuevo:txtEntCargo",1],
                        "Correo_entrevistado_input":["frmNuevo:txtEntCorreo",1]
                        }
    try:
        if campo is None:
            print("Ingrese un campo de inserción de datos a la ficha de supervisión")
        else:
            id_frm = diccionario_inputs[campo][0]
            if valor is None:
                print(f"No se modificó el campo {campo}")
            else:
                filtro = wait.until(EC.presence_of_element_located((By.ID, id_frm)))
                prueba_funcional.MoverClick(driver,filtro) #click
                if diccionario_inputs[campo][1] >0:
                    filtro.clear()
                #time.sleep(2)
                filtro.send_keys(valor)
                prueba_funcional.click_vacio(driver)
                print(f"Se cambió el/la {campo} en la ficha de supervisión")
    
    except StaleElementReferenceException:
        print("Error del elemento STALE")

    except Exception as e:
        print("Error en el ingreso de datos: ", e)
        driver.quit()

def seleccionar_campo_supervision(driver, wait, campo=None, valor=None):
    diccionario_campos={}
    if campo is None:
        print('Ingrese campo de supervisión que se seleccionará')
    else:
        if valor is None:
            print('Ingrese un valor al campo')
            

def ingresar_checkbox_supervision(driver, wait, campo, valor):
    print("Elegir campo y valor")


def seleccionar_estado(driver,wait,estado="EN PROCESO"):
    id_frm_estado ="frmNuevo:selEstado_label"
    diccionario_estados={"CONCLUIDO":"frmNuevo:selEstado_1","EN PROCESO":"frmNuevo:selEstado_2"}
    if estado not in diccionario_estados:
        print("El estado del proceso de supervisión no es válido")
    else: 
        id_estado=diccionario_estados[estado]
        filtro_estado = driver.find_element(By.ID, id_frm_estado)
        prueba_funcional.MoverClick(driver,filtro_estado)
        estado=wait.until(EC.presence_of_element_located((By.ID, id_estado)))
        prueba_funcional.MoverClick(driver,estado)
        print("Filtrado del estado de la DNA exitoso")
    
def seleccionar_supervisor(driver, wait, supervisor="NORA"):
    id_frm_supervisor ="frmNuevo:selSupervisor_label"
    diccionario_supervisores ={"DAVID":"frmNuevo:selSupervisor_7",
                               "NORA":"frmNuevo:selSupervisor_8",
                               "MARCOS":"frmNuevo:selSupervisor_21",
                               "CRISTIAN":"frmNuevo:selSupervisor_41"}
    if supervisor not in diccionario_supervisores:
        print("El supervisor no es válido")
    else: 
        id_supervisor=diccionario_supervisores[supervisor]
        filtro_supervisor = driver.find_element(By.ID, id_frm_supervisor)
        prueba_funcional.MoverClick(driver,filtro_supervisor)
        supervisor=wait.until(EC.presence_of_element_located((By.ID, id_supervisor)))
        prueba_funcional.MoverClick(driver,supervisor)
        print("Filtrado del supervisor fue exitoso")

def seleccionar_modalidad(driver, wait, modalidad="PRESENCIAL"):
    id_frm_modalidad ="frmNuevo:txtModalidad_label"
    diccionario_supervisores ={"PRESENCIAL":"frmNuevo:txtModalidad_1",
                               "VIRTUAL":"frmNuevo:txtModalidad_2"}
    if modalidad not in diccionario_supervisores:
        print("La modalidad no es válida")
    else: 
        id_modalidad=diccionario_supervisores[modalidad]
        filtro_modalidad = driver.find_element(By.ID, id_frm_modalidad)
        prueba_funcional.MoverClick(driver,filtro_modalidad)
        modalidad=wait.until(EC.presence_of_element_located((By.ID, id_modalidad)))
        prueba_funcional.MoverClick(driver,modalidad)
        print("Filtrado de la modalidad fue exitoso")


def seleccionar_modalidad(driver, wait, modalidad="PRESENCIAL"):
    id_frm_modalidad ="frmNuevo:txtModalidad_label"
    diccionario_supervisores ={"PRESENCIAL":"frmNuevo:txtModalidad_1",
                               "VIRTUAL":"frmNuevo:txtModalidad_2"}
    if modalidad not in diccionario_supervisores:
        print("La modalidad no es válida")
    else: 
        id_modalidad=diccionario_supervisores[modalidad]
        filtro_modalidad = driver.find_element(By.ID, id_frm_modalidad)
        prueba_funcional.MoverClick(driver,filtro_modalidad)
        modalidad=wait.until(EC.presence_of_element_located((By.ID, id_modalidad)))
        prueba_funcional.MoverClick(driver,modalidad)
        print("Filtrado de la modalidad fue exitoso")


def guardar_supervision(driver, tiempo_espera=20):
    wait_guardado = WebDriverWait(driver, tiempo_espera)
    id_buttom_guardar ="frmNuevo:j_idt298"
    buttom = driver.find_element(By.ID, id_buttom_guardar)
    prueba_funcional.MoverClick(driver,buttom)
    titulo_tabla = wait_guardado.until(EC.presence_of_element_located((By.ID, "//*[@id='frmBuscar:j_idt301']/div/span")))
    print(titulo_tabla.text)
    print("Se guardó con éxito la ficha")

def Prueba():
    datos = pd.read_excel('campos_supervision_excel.xlsx')
    try:
        inicio = time.time()
        prueba_funcional.Ingresar_Sistema(driver=driver, wait=wait, user_name="72623744", password="123456$$dan") 
        prueba_funcional.Ingresar_Submodulo(driver=driver, wait=wait, modulo_nombre="dna", submodulo_nombre="supervision")

        filtros.Filtrar_supervisores(driver=driver, wait=wait, supervisor="DAVID")
        prueba_funcional.Ingresar_supervision(driver=driver, wait=wait, nueva=True)

        lista_campos_llenar =[#"Fecha_input",
                              #"Hora_input", 
                              #"Direccion_DNA_input",
                              #"Telefono_DNA_input",
                              #"Correo_DNA_input",
                              #"Horario_DNA_input",
                              #"Autoridad_DNA_input",
                              "Direccion_autoridad_DNA_input",
                              "DNI_responsable_input",
                              "Fecha_responsable_input",
                              "Doc_responsable_input",
                              "Telefono_responsable_input",
                              "Correo_responsable_input",
                              "Ambientes_infraestructura_input",
                              "Texto_promocion_actividades",
                              "Texto_otros_actividades",
                              "Texto_comentarios",
                              "DNI_entrevistado_input",
                              "Cargo_entrevistado_input",
                              "Correo_entrevistado_input"]

        

        seleccionar_supervisor(driver, wait, supervisor="DAVID")

        #opcion = wait.until(EC.presence_of_element_located((By.ID, "frmNuevo:rbTipoLocal:0")))
        # wait_i = WebDriverWait(driver, 10)
        # radio_blanco = wait_i.until(EC.element_to_be_clickable((By.ID, "frmNuevo:rbTipoLocal:0")))
        # radio_blanco.click()
        # time.sleep(10)

        valor = "PRIVADO"
        diccionario_tipo = {"PRIVADO":"1", "COMPARTIDO":"2"}

        
        id_tipo_local = "//*[@id='frmNuevo:rbTipoLocal']/tbody/tr/td["+diccionario_tipo[valor]+"]/label"
        tipo_local = driver.find_element(By.XPATH, id_tipo_local)
        print(tipo_local.text)

        elemento_div = driver.find_element(By.XPATH, "//*[@id='frmNuevo:rbTipoLocal']/tbody/tr/td[1]/div/div[2]")
        script = "arguments[0].click();"
        driver.execute_script(script, elemento_div)

        for campo_lista in lista_campos_llenar:
            tiempo_espera = time.sleep(3)
            #Esperar que el PIDE responda
            if campo_lista in ["DNI_entrevistado_input", "DNI_responsable_input"]:
                ingresar_campo_supervision(driver,wait,campo=campo_lista,valor=str(datos[campo_lista][0]))
                tiempo_espera
            #Para evitar el error del elementO STALE
            elif campo_lista in ["Hora_input","Cargo_entrevistado_input"]:
                ingresar_campo_supervision(driver,wait,campo=campo_lista,valor=str(datos[campo_lista][0]))
                ingresar_campo_supervision(driver,wait,campo=campo_lista,valor=str(datos[campo_lista][0]))
            else:
                ingresar_campo_supervision(driver,wait,campo=campo_lista,valor=str(datos[campo_lista][0]))
        
        seleccionar_estado(driver,wait)
        seleccionar_modalidad(driver,wait)
        guardar_supervision(driver,15)
        time.sleep(3)
        final = time.time()
        print("Prueba de llenado exitosa, tiempo de ejecución: ", final - inicio, " segundos")
    except Exception as e:
        print("Error en la prueba: ", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    datos = pd.read_excel('campos_supervision_excel.xlsx')
    print()
    Prueba()