import prueba_funcional
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def Borrar_filtros(driver,wait,filtro=None):
    if filtro is None:
        print("Ingrese el filtro")
    
    #Borrar filtro de ubigeo
    elif filtro == "Filtrar_ubigeo":

        id_frm_departamento = ['frmBuscar:busDepartamento_label']
        id_sin_departamento= 'frmBuscar:busDepartamento_0'
        existe_filtro_departamento = prueba_funcional.probar_ids(driver,id_frm_departamento)

        if existe_filtro_departamento is None:
            print("El ID del filtro del departamento no fue encontrado")
        else:
            prueba_funcional.MoverClick(driver,existe_filtro_departamento)
            sin_departamento = wait.until(EC.presence_of_element_located((By.ID, id_sin_departamento)))
            prueba_funcional.MoverClick(driver,sin_departamento)
            print("Filtro del ubigeo limpio")

    #Borrar el filtro del código
    elif filtro == "Filtrar_codigo":
        id_frm_Codigo = ["frmBuscar:txtCodigo","frmBuscar:busCodigo"]
        existe_filtro_codigo = prueba_funcional.probar_ids(driver,id_frm_Codigo)
        if existe_filtro_codigo is None:
            print("El ID del filtro de codigo DNA no fue encontrado")
        else:    
            existe_filtro_codigo.clear()
            prueba_funcional.click_vacio(driver)
            print("Filtro del código limpio")

    #Borrar el estado de la DNA
    elif filtro == "Filtrar_estado_supervision":
        id_frm_estado = ["frmBuscar:busEstado_label","frmBuscar:txtEstadoBus"]
        id_sin_estado = "frmBuscar:busEstado_0"
        existe_estado = prueba_funcional.probar_ids(driver,id_frm_estado)
        if existe_estado is None:
            print("El ID del filtro de estado DNA no fue encontrado")
        else:
            prueba_funcional.MoverClick(driver,existe_estado)
            sin_estado = wait.until(EC.presence_of_element_located((By.ID, id_sin_estado)))
            prueba_funcional.MoverClick(driver,sin_estado)
            print("Filtro del estado limpio")

    #Borrar la fecha de supervision
    elif filtro == "Filtrar_fechas_supervision":
        id_frm_fecha_desde=["frmBuscar:j_idt331_input"]
        id_frm_fecha_hasta=["frmBuscar:j_idt336_input"]
        existe_fecha_desde = prueba_funcional.probar_ids(driver,id_frm_fecha_desde)
        existe_fecha_hasta = prueba_funcional.probar_ids(driver,id_frm_fecha_hasta)

        if existe_fecha_desde is None:
            print("El ID del filtro de fecha 'desde' no fue encontrado")
        else:
            prueba_funcional.MoverClick(driver,existe_fecha_desde)
            existe_fecha_desde.clear()
            print("Filtro de fecha 'desde' limpio")
        
        if existe_fecha_hasta is None:
            print("El ID del filtro de fecha 'hasta' no fue encontrado")
        else:
            prueba_funcional.MoverClick(driver,existe_fecha_hasta)
            existe_fecha_hasta.clear()
            print("Filtro de fecha 'hasta' limpio")

    #Borrar el supervisor
    elif filtro == "Filtrar_supervisores":
        id_frm_supervisor=["frmBuscar:selSupervisor_label"]
        id_sin_supervisor="frmBuscar:selSupervisor_0"
        existe_supervisor = prueba_funcional.probar_ids(driver,id_frm_supervisor)
        if existe_supervisor is None:
            print("El ID del supervisor no fue encontrado")
        else:
            prueba_funcional.MoverClick(driver,existe_supervisor)
            sin_supervisor = wait.until(EC.presence_of_element_located((By.ID, id_sin_supervisor)))
            prueba_funcional.MoverClick(driver,sin_supervisor)
            print("Filtro del supervisor limpio")



