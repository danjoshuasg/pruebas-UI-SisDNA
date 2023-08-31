import acciones_movimiento
import diccionarios_SisDNA

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException

import time
from datetime import datetime


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


#########################  ACCIONES MODULOS  #########################

# Funciones auxiliares
def validar_fecha(fecha_str):
    try:
        # Intentamos convertir la fecha a un objeto datetime
        datetime.strptime(fecha_str, '%d/%m/%Y')
        return True
    except ValueError:
        # Si se genera una excepción, la fecha no es válida
        print("La fecha no es válida.")
        return False

def comparar_fechas(fecha_mayor, fecha_menor):
    try:
        fecha_mayor = datetime.strptime(fecha_mayor, '%d/%m/%Y')
        fecha_menor = datetime.strptime(fecha_menor, '%d/%m/%Y')
        return fecha_mayor > fecha_menor
    except ValueError:
        # Si se genera una excepción, una de las fechas no es válida
        print("La fecha de 'hasta' debe ser mayor a la de 'desde'")
        return False

def click_send(driver, campo_nombre, ids_input , input):
    id_input_valido = probar_ids(driver,ids_input)
    if id_input_valido is None:
        print(f"El ID del campo {campo_nombre } no fue encontrado")
    else:    
        id_input_valido.clear()
        id_input_valido.send_keys(input)
        click_vacio(driver)
        print(f"Éxito: Enviar {input} al campo '{campo_nombre}'")

def clean_send(driver, campo, valor_campo):
        inicio = time.time()  
        campo.clear()
        campo.send_keys(valor_campo)
        click_vacio(driver)
        fin = time.time()
        tiempo = fin - inicio
        tiempo_formateado = "{:.{}f}".format(tiempo, 5)
        return tiempo_formateado



def accion_send(driver,campo_nombre, diccionario_atributos, valor_ingresar):
    try:
        texto_fecha=campo_nombre.split()[0]
        texto_desde_hasta=campo_nombre.split()[1]
        by = diccionario_atributos["By"]
        elemento_web = diccionario_atributos["elemento_web"]

        if texto_fecha == "Fecha":
            #Validar el formato
            if validar_fecha(valor_ingresar):
                campo = driver.find_element(by,elemento_web)
                tiempo_formateado=clean_send(driver,campo, valor_ingresar)


        else:
            campo = driver.find_element(by,elemento_web)
            tiempo_formateado=clean_send(driver,campo, valor_ingresar)

        print(f"Éxito: Se envió el valor '{valor_ingresar}' al campo '{campo_nombre}' en ({tiempo_formateado}) segundos")
        #Elementos tipo fecha
    except Exception as e:
        print("Error en 'accion send': ",e)


def elemento_presente(wait, elemento_web, By_name=By.ID):
    try:
        elemento=wait.until(EC.presence_of_element_located((By_name, elemento_web)))
        return elemento
    except:
        return None

def registrar_opciones(driver,wait, diccionario_atributos):
    try: 

        opciones = {}
        campo_web = diccionario_atributos["elemento_web"]
        by = diccionario_atributos["By"]

        #Input: frmPersona:txtColegio_label | Output: frmPersona:txtColegio_ (opcion formato)
        string_eliminado = ["label"]
        texto_cortado = campo_web.split("_")

        opcion_formato= []
        for i in texto_cortado:
            if i not in string_eliminado:
                opcion_formato.append(i)
        opcion_formato = " ".join(opcion_formato)
        print("Formato: ",opcion_formato)
        #Abrir el desplegable
        filtro_campo = wait.until(EC.presence_of_element_located((by, campo_web)))
        MoverClick(driver, filtro_campo)

        #Input: frmPersona:txtColegio_ | Output: {"Texto 1":frmPersona:txtColegio_1, "Texto 2":frmPersona:txtColegio_2 ... "Texto 3": frmPersona:txtColegio_n} (Diccionario de opciones)
        c=0
        for i in range(30): # Máximo número de opciones a buscar dentro de un desplegable

            opcion_web = opcion_formato+"_"+str(i)
            # print("Opcion: ",opcion_web)
            c+=1
            opcion = elemento_presente(wait, opcion_web, By_name=by)
            if opcion:
                opciones[opcion.text] = {"By":by,"elemento_web":opcion_web,"tipo":"click"}
            else:
                print(f"Se encontraron {c-2} opciones, la opción 0 es nula")
                break

        return opciones

    except Exception as e:
        print("Error en 'registrar opciones': ",e)

def choose_send(driver,opciones, valor_ingresar):
    inicio = time.time()
    opcion = opciones[valor_ingresar]["elemento_web"]  
    elemento=wait.until(EC.presence_of_element_located((By.ID, opcion)))
    MoverClick(driver,elemento)
    click_vacio(driver)
    fin = time.time()
    tiempo = fin - inicio
    tiempo_formateado = "{:.{}f}".format(tiempo, 5)
    return tiempo_formateado

def validar_tipo_ubigeo(tipo_ubigeo,lista_tipos_ubigeos):
    if tipo_ubigeo in lista_tipos_ubigeos:
        return tipo_ubigeo
    elif tipo_ubigeo in [1,2,3]:
        tipo_ubigeo = lista_tipos_ubigeos[tipo_ubigeo]
        return tipo_ubigeo
    else:
        print("Formato erróneo de tipo de ubigeo: Ingrese un texto ('departamento','provincia','distrito') o un número (1,2,3)")
        return None

def validar_entrada_ubigeo(entrada_ubigeo):
    try:
        lista_tipos_ubigeos =["departamento","provincia","distrito"]
        if isinstance(entrada_ubigeo,dict): #{'departamento':1} {1:'Amazonas'}
            tipo_ubigeo = list(entrada_ubigeo.keys())[0]
            if validar_tipo_ubigeo(tipo_ubigeo,lista_tipos_ubigeos):
                campo = validar_tipo_ubigeo(tipo_ubigeo,lista_tipos_ubigeos)
                valor_ingresado = entrada_ubigeo[tipo_ubigeo]
                return campo, valor_ingresado

        elif isinstance(entrada_ubigeo,list): #['departamento',1] [1,'Amazonas']
            tipo_ubigeo = entrada_ubigeo[0]
            if validar_tipo_ubigeo(tipo_ubigeo,lista_tipos_ubigeos):
                campo = validar_tipo_ubigeo(tipo_ubigeo,lista_tipos_ubigeos)
                valor_ingresado = entrada_ubigeo[tipo_ubigeo]
                return campo, valor_ingresado
        else:
            print("Ingrese un formato válido de entrada ubigeo: {'Departamento':1} o [1,1]")
            return None

    except Exception as e:
        print("Error en validar entrada ubigeo:",e)

def accion_choose(driver, campo_nombre, diccionario_atributos, valor_ingresar=1):
    try:
        wait = WebDriverWait(driver, 15)
        #El valor a ingresar puede ser un número -> Validar si está dentro del rango del índice
        if isinstance(valor_ingresar,int):
            opciones = registrar_opciones(driver, wait, diccionario_atributos)
            lista_opciones=list(opciones.keys())
            rango_indices = list(range(len(lista_opciones)))
            if valor_ingresar in rango_indices:
                valor_ingresar=lista_opciones[valor_ingresar]
                tiempo = choose_send(driver,opciones, valor_ingresar)
                print(f"Éxito: Se envió el valor '{valor_ingresar}' al campo '{campo_nombre}' en ({tiempo}) segundos")
                time.sleep(3) #opcional
            else: 
                print(f"Ingrese un valor numérico entre { rango_indices}")

        #El valor puede ser un string -> Validar si está comprendido en la lista de opciones
        elif isinstance(valor_ingresar,str):
            opciones = registrar_opciones(driver, wait, diccionario_atributos)
            lista_opciones=list(opciones.keys())
            if valor_ingresar in lista_opciones:
                tiempo = choose_send(driver,opciones, valor_ingresar)
                print(f"Éxito: Se envió el valor '{valor_ingresar}' al campo '{campo_nombre}' en ({tiempo}) segundos")
                time.sleep(3) #opcional
                #Elementos simples

        #El valor puede ser un diccionario o una lista-> Validar si está comprendido en la lista de opciones
        elif isinstance(valor_ingresar, dict) or isinstance(valor_ingresar, list):
            #Valor ingresar debe indicar el key:"D"
            campo, valor_ingresado = validar_entrada_ubigeo(valor_ingresar)
            diccionario_ubigeo = diccionario_atributos
            # print(diccionario_ubigeo)
            diccionario_ubigeo["elemento_web"] = diccionario_atributos["elemento_web"][campo]
            accion_choose(driver, campo, diccionario_ubigeo, valor_ingresado)
            diccionario_atributos["elemento_web"] = {'departamento': 'frmBuscar:busDepartamento_label', 
                                                     'provincia': 'frmBuscar:busProvincia_label', 
                                                     'distrito': 'frmBuscar:busDistrito_label'}
            # print(diccionario_atributos)
        else:
            print(f"El tipo de formato del valor a ingresar al campo {campo_nombre} es incorrecto")
        
    except Exception as e:
        print("Error en 'accion choose': ",e)

def acciones_ingresar_datos(driver,campo,diccionario_atributos,valor_ingresar):
    if diccionario_atributos["tipo"] == "send":
       accion_send(driver, campo, diccionario_atributos, valor_ingresar)
       time.sleep(1) #opcional
    elif diccionario_atributos["tipo"] == "choose":
       accion_choose(driver, campo, diccionario_atributos, valor_ingresar)
       time.sleep(1) #opcional
    else:
        print("No se encuentra el 'tipo'")


def acciones_funcionales(driver, campo, diccionario_atributos):
    try:
        inicio = time.time()
        by = diccionario_atributos["By"]
        elemento_nombre = diccionario_atributos["elemento_web"]
        tipo=diccionario_atributos["tipo"]
        elemento = driver.find_element(by,elemento_nombre)
        MoverClick(driver,elemento)
        fin = time.time()
        tiempo = fin - inicio
        tiempo_formateado = "{:.{}f}".format(tiempo, 5)
        print(f"Éxito: funcionó el '{tipo}' en el elemento '{campo}' en ({tiempo_formateado}) segundos")
    except Exception as e:
        print("Error en acciones funcionales:",e)



######################################################################

def Prueba(driver,wait):
    modulo = "dna"
    submodulo = "dna"
    # acciones_movimiento.Ingresar_Sistema(driver,wait)
    # acciones_movimiento.Ingresar_Modulo_Submodulo(driver,wait,modulo_nombre=modulo,submodulo_nombre=submodulo)

    # Se tiene el diccionario de modulos
    diccionario_submodulo = {"dna":diccionarios_SisDNA.diccionarios_DNA,
                             "acreditacion":diccionarios_SisDNA.diccionarios_ACREDITACION,
                             "supervision":diccionarios_SisDNA.diccionarios_SUPERVISION,
                             "capacitacion":diccionarios_SisDNA.diccionarios_CAPACITACION,
                             "mantenimiento":diccionarios_SisDNA.diccionarios_MANTENIMIENTO,
                             "seguridad":diccionarios_SisDNA.diccionarios_SEGURIDAD}
    
    # Se piden todas las ventanas del submodulo elegido como lista
    lista_ventanas= diccionario_submodulo[submodulo]()

    print(lista_ventanas)

    # Se elije la ventana y se piden las operaciones que se pueden hacer en las ventanas como lista
    ventana = lista_ventanas[0] #Para filtrar
    print("Se eligió ventana: ",ventana)
    diccionario_operaciones = diccionario_submodulo[submodulo](ventana)
    lista_operaciones = list(diccionario_operaciones.keys())

    print(lista_operaciones)

    # # Se elije la operación y se piden los campos como lista
    # operacion = lista_operaciones[0]
    # print("Se eligió campo: ",operacion)
    # diccionario_campos = diccionario_operaciones[operacion]

    # lista_campos = list(diccionario_campos.keys())
    
    # # Se elie el campo y se piden los atributos del campo en una lista
    # campo = lista_campos[0]
    # print("Se eligió campo: ",campo)
    # diccionario_atributos = diccionario_campos[campo] #(Por defecto todos, sino mostrar los nombres de los campos)
    # acciones_ingresar_datos(driver, campo, diccionario_atributos, "01001")

    # # Se elie el campo y se piden los atributos del campo en una lista
    # campo = lista_campos[1]
    # print("Se eligió campo: ",campo)
    # diccionario_atributos = diccionario_campos[campo] #(Por defecto todos, sino mostrar los nombres de los campos)
    # acciones_ingresar_datos(driver, campo, diccionario_atributos, 1)

    # # Se elie el campo y se piden los atributos del campo en una lista
    # campo = lista_campos[2]
    # print("Se eligió campo: ",campo)
    # diccionario_atributos = diccionario_campos[campo] #(Por defecto todos, sino mostrar los nombres de los campos)

    # acciones_ingresar_datos(driver, campo, diccionario_atributos, {'departamento':'AMAZONAS'})
    # acciones_ingresar_datos(driver, campo, diccionario_atributos, {'provincia':'BONGARA'})
    # acciones_ingresar_datos(driver, campo, diccionario_atributos, {'distrito':'COROSHA'})

    # Se elije la operación y se piden los campos como lista
    ################# EXTRAER DATOS (1) #################################
    operacion = lista_operaciones[1]
    print("Se eligió operacion: ",operacion)
    diccionario_campos = diccionario_operaciones[operacion]
    lista_campos = list(diccionario_campos.keys())
    campo = lista_campos[0]
    print("Se eligió campo: ",campo)


    ################# FUNCIONALES (2) #################################
    operacion = lista_operaciones[2]
    print("Se eligió operacion: ",operacion)
    diccionario_campos = diccionario_operaciones[operacion]
    lista_campos = list(diccionario_campos.keys())
    ################# Crear (0) #################################
    campo = lista_campos[0]

    print("Se eligió campo: ",campo)
    diccionario_atributos = diccionario_campos[campo] #(Por defecto todos, sino mostrar los nombres de los campos)
    print(diccionario_atributos)



    # acciones_movimiento.Salir_Sistema(driver)

    # acciones_movimiento.Salir_Sistema(driver)

if __name__ == "__main__":
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)
    Prueba(driver,wait)