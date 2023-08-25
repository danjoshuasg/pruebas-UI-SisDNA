

def diccionarios_SisDNA(nombre_diccionario="modulos"):
    # navegacion_SisDNA[nombre_modulo][url]-> direccion modulo
    # navegacion_SisDNA[nombre_modulo][submodulos][nombre_submodulo][url]-> direccion submodulo
    # navegacion_SisDNA[nombre_modulo][submodulos][nombre_submodulo][css_evidencia]-> evidencia de ingreso a submodulo en modulo
    navegacion_SisDNA ={
                        "home":{"url":"Inicio"},
                        "dna":{
                                "url":"0",
                                "submodulos":{"dna":{"url":"/dna/",
                                                     "css_evidencia":"#frmBuscar\:j_idt155 > div > span"},
                                            "acreditacion":{"url":"/acreditacion/",
                                                            "css_evidencia":"#frmBuscar\:j_idt480 > div > span"},
                                            "supervision":{"url":"/supervision/",
                                                           "css_evidencia":"#frmBuscar\:j_idt301 > div > span"},
                                            "capacitacion programacion":{"url":"/capacitacion/curso/",
                                                                         "css_evidencia":"#frmBuscar\:j_idt181 > div.bctitle.clearfix > span"},
                                            "capacitacion ejecucion":{"url":"/capacitacion/solicitud/",
                                                                      "css_evidencia":"#frmBuscar\:j_idt224 > div > span"},
                                            "reporte":{"url":"/reporte/",
                                                       "css_evidencia":"#j_idt57 > div > div > span"}
                                            }
                               }, 
                        "riesgo":{
                                "url":"1",    
                                "submodulos":{  "recepcion":{"url":"/demuna/recepcion/",
                                                             "css_evidencia":"#frmBuscar\:j_idt155 > div > span"},
                                                "valoracion":{"url":"/demuna/valoracion/",
                                                              "css_evidencia":"#frmBuscar\:j_idt155 > div > span"},
                                                "evaluacion":{"url":"/demuna/evaluacion/",
                                                              "css_evidencia":"#frmBuscar\:j_idt155 > div > span"},
                                                "pti":{"url":"/demuna/pti/",
                                                       "css_evidencia":"#frmBuscar\:j_idt155 > div > span"},
                                                "reportes":{"url":"/demuna/reporte/",
                                                            "css_evidencia":"#j_idt57 > div > div > span"},
                                            }
                                },

                        "mantenimiento":{
                                "url":"2",
                                "submodulos":{"municipalidades":{"url":"/mantenimiento/municipalidad/",
                                                            "css_evidencia":"#frmBuscar\:j_idt95 > div.bctitle.clearfix > span"},
                                              "catalogo":{"url":"/mantenimiento/catalogo/",
                                                            "css_evidencia":"#content > section > div.bctitle.clearfix > span"},
                                              "parametros":{"url":"/mantenimiento/parametro/",
                                                            "css_evidencia":"#content > section > div.bctitle.clearfix > span"},
                                              "colegios":{"url":"/mantenimiento/colegio/",
                                                            "css_evidencia":"#content > section > div.bctitle.clearfix > span"},
                                              "carga inicial":{"url":"/mantenimiento/cargainicial/",
                                                                "css_evidencia":"#frmDna > h1"},
                                        }
                                     },
                        "seguridad":{
                                 "url":"3",
                                 "submodulos":{"usuarios":{"url":"/seguridad/",
                                                           "css_evidencia":"#frmGestion\:j_idt58 > div.bctitle.clearfix > span"}
                                              }
                                    }
                        }
    diccionarios = {"navegacion":navegacion_SisDNA}
    return diccionarios[nombre_diccionario]

def diccionarios_DNA(nombre_ventana):
    diccionario_ventanas={"DNA":DNA,"REGISTRO DNA":REGISTRO_DNA, "ACTUALIZACION DNA":ACTUALIZACION_DNA}
    DNA={
        "ingresar_datos":{"Código DNA":{"By":"ID",
                              "elemento_web":"frmBuscar:txtCodigo",
                              "tipo":"send"},
                "Estado DNA":{"By":"ID",
                              "elemento_web":"frmBuscar:txtEstadoBus_label",
                              "tipo":"choose"},
                "Filtrar ubigeo":{"By":"ID",
                                  "elemento_web":{"departamento":"frmBuscar:busDepartamento_label", 
                                                  "provincia":"frmBuscar:busProvincia_label",
                                                  "distrito":"frmBuscar:busDistrito_label"},
                                  "tipo":"choose"}
                },
        "extraer_datos":{"Exportar DNA":{"By":"XPATH",
                                "elemento_web":'//*[@id="formularioPrincipal1:j_idt179"]/ul/li[1]/a/span[1]',
                                "tipo":"download"},
                        "Exportar Defensores":{"By":"XPATH",
                                "elemento_web":'//*[@id="formularioPrincipal1:j_idt179"]/ul/li[2]/a/span[1]',
                                "tipo":"download"}
                        },
        "funcionales_DNA":{"Crear":{"By":"ID",
                                "elemento_web":'formularioPrincipal1:j_idt182',
                                "tipo":"click"},
                        "Editar":{"By":"ID",
                                "elemento_web":'formularioPrincipal1:tablaDefensoria:{number_row}:j_idt185',
                                "tipo":"click"},
                        "Eliminar":{"By":"ID",
                                "elemento_web":'formularioPrincipal1:tablaDefensoria:{number_row}:j_idt186',
                                "tipo":"click"},
                        "Ingresar Reporte":{"By":"ID",
                                "elemento_web":'formularioPrincipal1:btnOpciones',
                                "tipo":"click"},
                        }
        }
    REGISTRO_DNA = {
        "ingresar_datos":{"Tipo sede":{"By":"ID",
                              "elemento_web":"formREGISTRODNA:txtTipo_label",
                              "tipo":"choose"},
                "Tipo DNA":{"By":"ID",
                              "elemento_web":"formREGISTRODNA:txtOrigen_label",
                              "tipo":"choose"},
                "Nombre entidad":{"By":"ID",
                              "elemento_web":"formREGISTRODNA:txtEntidad",
                              "tipo":"send"},
                "Nombre DNA":{"By":"ID",
                              "elemento_web":"formREGISTRODNA:txtNombre",
                              "tipo":"send"},
                "Filtrar ubigeo":{"By":"ID",
                                  "elemento_web":{"departamento":"formREGISTRODNA:txtDepartamento_label", 
                                                  "provincia":"formREGISTRODNA:txtProvincia_label",
                                                  "distrito":"formREGISTRODNA:txtDistrito_label"},
                                  "tipo":"choose"},
                },
        "funcionales_DNA":{"Guardar":{"By":"ID",
                                "elemento_web":'formREGISTRODNA:j_idt308',
                                "tipo":"click"},
                        "Cerrar":{"By":"ID",
                                "elemento_web":'formREGISTRODNA:j_idt310',
                                "tipo":"click"}
                        }
    }

    ACTUALIZACION_DNA= {
        "ingresar_datos":{"Número ordenanza":{"By":"ID",
                              "elemento_web":"formREGISTRODNA:txtTipo_label",
                              "tipo":"choose"},
                "Fecha ordenanza":{"By":"ID",
                              "elemento_web":"frmNuevo:txtNroOrdenanza",
                              "tipo":"choose"},
                "Direccion DNA":{"By":"ID",
                              "elemento_web":"frmNuevo:txtDireccion",
                              "tipo":"send"},
                "Correo contacto":{"By":"ID",
                              "elemento_web":"frmNuevo:txtCorreo",
                              "tipo":"send"},
                "Telefono":{"By":"ID",
                              "elemento_web":"frmNuevo:txtTelefono",
                              "tipo":"send"},
                "Jefatura DNA":{"By":"ID",
                              "elemento_web":"frmNuevo:txtGerencia",
                              "tipo":"send"},
                "Atención DNA":{"By":"ID",
                              "elemento_web":"frmNuevo:txtDias",
                              "tipo":"send"},
                "Fecha acreditacion":{"By":"ID",
                              "elemento_web":"frmNuevo:txtFecAcreditacion_input",
                              "tipo":"send"},
                "Doc acreditacion":{"By":"ID",
                              "elemento_web":"frmNuevo:txtResAcreditacion",
                              "tipo":"send"},
                "Fecha supervision":{"By":"ID",
                              "elemento_web":"frmNuevo:txtFecSupervision_input",
                              "tipo":"send"},
                "Estado DNA":{"By":"ID",
                              "elemento_web":"frmNuevo:selEstadoDna_label",
                              "tipo":"choose"},
                "Observaciones":{"By":"ID",
                              "elemento_web":"frmNuevo:txtobservaciones",
                              "tipo":"send"}
                },
        "funcionales_DNA":{"Nuevo integrante DNA":{"By":"ID",
                                "elemento_web":'frmNuevo:j_idt137',
                                "tipo":"click"},
                        "Editar integrante DNA":{"By":"ID",
                                "elemento_web":'frmNuevo:tablaEquipo:{num_row}:j_idt140',
                                "tipo":"click"},
                        "Eliminar integrante DNA":{"By":"ID",
                                "elemento_web":'frmNuevo:tablaEquipo:{num_row}:j_idt141',
                                "tipo":"click"},
                        "Guardar":{"By":"ID",
                                "elemento_web":'frmNuevo:j_idt153',
                                "tipo":"click"}
                        }
    }
    INTEGRANTE_DNA_DNA = {

        "ingresar_datos":{"Funcion responsable":{"By":"ID",
                              "elemento_web":"formREGISTRODNA:txtTipo_label",
                              "tipo":"choose"},
                "DNI":{"By":"ID",
                              "elemento_web":"formREGISTRODNA:txtOrigen_label",
                              "tipo":"choose"},
                "Edad":{"By":"ID",
                              "elemento_web":"formREGISTRODNA:txtEntidad",
                              "tipo":"send"},
                "Telefono":{"By":"ID",
                              "elemento_web":"formREGISTRODNA:txtNombre",
                              "tipo":"send"},
                "Correo":{"By":"ID",
                              "elemento_web":"formREGISTRODNA:txtNombre",
                              "tipo":"send"},
                "Sexo":{"By":"ID",
                              "elemento_web":"formREGISTRODNA:txtNombre",
                              "tipo":"send"},
                "Tipo de instrucción":{"By":"ID",
                              "elemento_web":"formREGISTRODNA:txtNombre",
                              "tipo":"send"},
                "Tipo de instrucción":{"By":"ID",
                              "elemento_web":"formREGISTRODNA:txtNombre",
                              "tipo":"send"},
                "Tipo de instrucción":{"By":"ID",
                              "elemento_web":"formREGISTRODNA:txtNombre",
                              "tipo":"send"},
                "Tipo de instrucción":{"By":"ID",
                              "elemento_web":"formREGISTRODNA:txtNombre",
                              "tipo":"send"},
                "Correo":{"By":"ID",
                                  "elemento_web":{"departamento":"formREGISTRODNA:txtDepartamento_label", 
                                                  "provincia":"formREGISTRODNA:txtProvincia_label",
                                                  "distrito":"formREGISTRODNA:txtDistrito_label"},
                                  "tipo":"choose"},
                },
        "funcionales_DNA":{"Guardar":{"By":"ID",
                                "elemento_web":'formREGISTRODNA:j_idt308',
                                "tipo":"click"},
                        "Cerrar":{"By":"ID",
                                "elemento_web":'formREGISTRODNA:j_idt310',
                                "tipo":"click"}
                        }

    }
        
    return diccionario_ventanas[nombre_ventana]

def diccionarios_acreditacion(nombre_campo):
    print("Diccionario de campos DNA")

def diccionarios_capacitacion(etapa_capacitacion, ):
    print("Diccionario de campos DNA")

def diccionarios_supervision(etapa_capacitacion, ):
    print("Diccionario de campos DNA")

def diccionarios_seguridad(etapa_capacitacion, ):
    print("Diccionario de campos DNA")

def diccionarios_catalogo(etapa_capacitacion, ):
    print("Diccionario de campos DNA")

if __name__ == "__main__":
    diccionarios_SisDNA()