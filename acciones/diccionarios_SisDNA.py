

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
    diccionario_ventanas={"DNA":DNA,"REGISTRO DNA":REGISTRO_DNA, "ACTUALIZACION DNA":ACTUALIZACION_DNA, "INTEGRANTE DNA":INTEGRANTE_DNA}
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
    INTEGRANTE_DNA = {

        "ingresar_datos":{"Funcion responsable":{"By":"ID",
                              "elemento_web":"frmPersona:nidFuncion_label",
                              "tipo":"choose"},
                "DNI":{"By":"ID",
                              "elemento_web":"frmPersona:documento",
                              "tipo":"send"},
                "Edad":{"By":"ID",
                              "elemento_web":"frmPersona:txtEdad_input",
                              "tipo":"send"},
                "Telefono":{"By":"ID",
                              "elemento_web":"frmPersona:telefono",
                              "tipo":"send"},
                "Correo":{"By":"ID",
                              "elemento_web":"frmPersona:correo",
                              "tipo":"send"},
                "Tipo de instrucción":{"By":"ID",
                              "elemento_web":"frmPersona:txtTipoInstruccion",
                              "tipo":"send"},
                "Sexo":{"By":"ID",
                              "elemento_web":"frmPersona:sexo_label",
                              "tipo":"choose"},                                                            
                "Nivel de instrucción":{"By":"ID",
                              "elemento_web":"frmPersona:txtInstruccion_label",
                              "tipo":"choose"},
                "Profesión":{"By":"ID",
                              "elemento_web":"frmPersona:txtProfesion_label",
                              "tipo":"choose"},
                "Colegio profesional":{"By":"ID",
                              "elemento_web":"frmPersona:txtColegio_label",
                              "tipo":"choose"},
                "Nro colegiatura":{"By":"ID",
                              "elemento_web":"frmPersona:txtColegiatura",
                              "tipo":"send"},
                "Equipo interdisciplinar":{"By":"ID",
                              "elemento_web":"frmPersona:txtColegiatura",
                              "tipo":"check"}
                },

        "funcionales_DNA":{"Guardar":{"By":"ID",
                                "elemento_web":'frmPersona:j_idt267',
                                "tipo":"click"},
                        "Cerrar":{"By":"ID",
                                "elemento_web":'frmPersona:j_idt269',
                                "tipo":"click"}
                        }

    }

    return diccionario_ventanas[nombre_ventana]

def diccionarios_ACREDITACION(nombre_ventana):


    ACREDITACION={
        "ingresar_datos":{"Código DNA":{"By":"ID",
                              "elemento_web":"frmBuscar:txtCodigo",
                              "tipo":"send"},
                "Filtrar ubigeo":{"By":"ID",
                                  "elemento_web":{"departamento":"frmBuscar:busDepartamento", 
                                                  "provincia":"frmBuscar:busProvincia"},
                                  "tipo":"choose"},
                "Fecha":{"By":"ID",
                              "elemento_web":"frmBuscar:busFechaIni_input",
                              "tipo":"send"},
                "Estado DNA":{"By":"ID",
                              "elemento_web":"frmBuscar:txtEstadoBus",
                              "tipo":"choose"},
                "Estado proceso":{"By":"ID",
                              "elemento_web":"frmBuscar:selFiltroAcre_label",
                              "tipo":"choose"},
                "Subir PDF":{"By":"ID",
                              "elemento_web":"formularioPrincipal:tablaDocs:{num_row}:j_idt516",
                              "tipo":"upload"}                                                                                        
                },
        "extraer_datos":{"Descargar PDF":{"By":"ID",
                                "elemento_web":'formularioPrincipal:tablaDocs:{num_row}:j_idt515',
                                "tipo":"download"},
                        "Descargar PDF firmado":{"By":"ID",
                                "elemento_web":'formularioPrincipal:tablaDocs:{num_row}:j_idt517',
                                "tipo":"download"}
                        },
        "funcionales_DNA":{"Crear":{"By":"ID",
                                "elemento_web":'formularioPrincipal:j_idt508',
                                "tipo":"click"},
                        "Editar":{"By":"ID",
                                "elemento_web":'formularioPrincipal:tablaDocs:{num_row}:j_idt511',
                                "tipo":"click"},
                        "Evaluar":{"By":"ID",
                                "elemento_web":'formularioPrincipal:tablaDocs:{num_row}:j_idt512',
                                "tipo":"click"},                                
                        "Eliminar":{"By":"ID",
                                "elemento_web":'formularioPrincipal:tablaDocs:{num_row}:j_idt514',
                                "tipo":"click"},
                        "Subsanar":{"By":"ID",
                                "elemento_web":'formularioPrincipal:tablaDocs:{num_row}:j_idt513',
                                "tipo":"click"}
                        }
        }
    
    REGISTRO_ACREDITACION = {
        "ingresar_datos":{"Fecha ingreso":{"By":"ID",
                              "elemento_web":"frmNuevo:txtFechaIngresoMimp_input",
                              "tipo":"send"},
                "Nro expediente":{"By":"ID",
                              "elemento_web":"frmNuevo:txtNroExpediente",
                              "tipo":"send"}, 
                "DNI autoridad":{"By":"ID",
                              "elemento_web":"frmNuevo:txtAutoridadDni",
                              "tipo":"send"},  
                "Institucion autoridad":{"By":"ID",
                              "elemento_web":"frmNuevo:txtAutoridadInstitucion",
                              "tipo":"send"},  
                "Cargo autoridad":{"By":"ID",
                              "elemento_web":"frmNuevo:txtAutoridadCargo",
                              "tipo":"send"},  
                "Código DNA":{"By":"ID",
                              "elemento_web":"frmNuevo:j_idt86",
                              "tipo":"send"},  
                "Nro Ordenanza":{"By":"ID",
                              "elemento_web":"frmNuevo:txtNroOrdenanza",
                              "tipo":"send"},
                "Fecha Ordenanza":{"By":"ID",
                              "elemento_web":"frmNuevo:txtFecOrdenanza_input",
                              "tipo":"send"},                                  
                "Direccion DNA":{"By":"ID",
                              "elemento_web":"frmNuevo:txtDireccion",
                              "tipo":"send"},  
                "Correo DNA":{"By":"ID",
                              "elemento_web":"frmNuevo:txtCorreo",
                              "tipo":"send"},
                "Teléfono DNA":{"By":"ID",
                              "elemento_web":"frmNuevo:txtTelefono",
                              "tipo":"send"},
                "Jefatura DNA":{"By":"ID",
                              "elemento_web":"frmNuevo:txtGerencia",
                              "tipo":"send"},
                "Atención DNA":{"By":"ID",
                              "elemento_web":"frmNuevo:txtDias",
                              "tipo":"send"},
                "Presupuesto DNA":{"By":"ID",
                              "elemento_web":"frmNuevo:txtPresupuesto_input",
                              "tipo":"send"},
                "Nro Ambientes DNA":{"By":"ID",
                              "elemento_web":"frmNuevo:txtAmbientes_input",
                              "tipo":"send"},
                "Nro Ambientes audiencias DNA":{"By":"ID",
                              "elemento_web":"frmNuevo:txtAmbientesPrivadas_input",
                              "tipo":"send"},

                "Nro Ambientes audiencias DNA":{"By":"ID",
                              "elemento_web":"frmNuevo:txtAmbientesPrivadas_input",
                              "tipo":"send"},

                "Nro Ambientes audiencias DNA":{"By":"ID",
                              "elemento_web":"frmNuevo:txtAmbientesPrivadas_input",
                              "tipo":"send"},

                "Tiene ambiente privado":{"By":"ID",
                              "elemento_web":"frmNuevo:j_idt126",
                              "tipo":"check"},

                "Tiene equipo de computo":{"By":"ID",
                              "elemento_web":"frmNuevo:j_idt129",
                              "tipo":"check"},

                "Tiene impresora":{"By":"ID",
                              "elemento_web":"frmNuevo:j_idt131",
                              "tipo":"check"},

                "Tiene internet":{"By":"ID",
                              "elemento_web":"frmNuevo:j_idt133",
                              "tipo":"check"},

                "Ambiente seguro documentos":{"By":"ID",
                              "elemento_web":"frmNuevo:j_idt135",
                              "tipo":"check"},

                "Accesible NNA y discapacitados":{"By":"ID",
                              "elemento_web":"frmNuevo:j_idt137",
                              "tipo":"check"},

                "Tiene espacio de espera":{"By":"ID",
                                "elemento_web":"frmNuevo:j_idt139",
                                "tipo":"check"},

                "Estado conservacion":{"By":"ID",
                              "elemento_web":"frmNuevo:txtEstadoCons:{n_state}",
                              "tipo":"check options"},                     

                "DJ solicitar acreditación":{"By":"ID",
                              "elemento_web":"frmNuevo:j_idt167_input",
                              "tipo":"upload"},

                "DJ integrantes DNA":{"By":"ID",
                              "elemento_web":"frmNuevo:j_idt173_input",
                              "tipo":"upload"},

                "Ordenanza municipal":{"By":"ID",
                              "elemento_web":"frmNuevo:j_idt179_input",
                              "tipo":"upload"},

                "Resolución de alcaldía":{"By":"ID",
                              "elemento_web":"frmNuevo:j_idt185_input",
                              "tipo":"upload"},

                "Documentos integrados":{"By":"ID",
                              "elemento_web":"frmNuevo:j_idt191_input",
                              "tipo":"upload"},

                "Oficio de solicitud de acreditación":{"By":"ID",
                              "elemento_web":"frmNuevo:j_idt197_input",
                              "tipo":"upload"},

                "Otros documentos":{"By":"ID",
                              "elemento_web":"frmNuevo:j_idt203_input",
                              "tipo":"upload"},
                },

        "funcionales_DNA":{"Guardar":{"By":"ID",
                                "elemento_web":'frmNuevo:j_idt474',
                                "tipo":"click"},
                        "Registrar integrante":{"By":"ID",
                                "elemento_web":'frmNuevo:j_idt147',
                                "tipo":"click"}
                        }
    },

    INTEGRANTE_DNA = {
        "ingresar_datos":{"Funcion responsable":{"By":"ID",
                              "elemento_web":"modalNuevoEquipo:nidFuncion_label",
                              "tipo":"choose"},
                "DNI":{"By":"ID",
                              "elemento_web":"modalNuevoEquipo:documento",
                              "tipo":"send"},
                "Edad":{"By":"ID",
                              "elemento_web":"modalNuevoEquipo:txtEdad_input",
                              "tipo":"send"},
                "Telefono":{"By":"ID",
                              "elemento_web":"modalNuevoEquipo:telefono",
                              "tipo":"send"},
                "Correo":{"By":"ID",
                              "elemento_web":"modalNuevoEquipo:correo",
                              "tipo":"send"},
                "Tipo de instrucción":{"By":"ID",
                              "elemento_web":"modalNuevoEquipo:txtTipoInstruccion_label",
                              "tipo":"send"},
                "Sexo":{"By":"ID",
                              "elemento_web":"modalNuevoEquipo:sexo_label",
                              "tipo":"choose"},                                                            
                "Nivel de instrucción":{"By":"ID",
                              "elemento_web":"modalNuevoEquipo:txtInstruccion_label",
                              "tipo":"choose"},
                "Profesión":{"By":"ID",
                              "elemento_web":"modalNuevoEquipo:txtProfesion_label",
                              "tipo":"choose"},
                "Colegio profesional":{"By":"ID",
                              "elemento_web":"modalNuevoEquipo:txtColegio_label",
                              "tipo":"choose"},
                "Nro colegiatura":{"By":"ID",
                              "elemento_web":"modalNuevoEquipo:txtColegiatura",
                              "tipo":"send"},
                "Equipo interdisciplinar":{"By":"ID",
                              "elemento_web":"modalNuevoEquipo:j_idt541_input",
                              "tipo":"check"}
                },
        "funcionales_DNA":{"Guardar":{"By":"ID",
                                "elemento_web":'modalNuevoEquipo:j_idt625',
                                "tipo":"click"},
                        "Cerrar":{"By":"ID",
                                "elemento_web":'modalNuevoEquipo:j_idt627',
                                "tipo":"click"}
                        }
    }

    diccionario_ventanas={"acreditacion":ACREDITACION,
                          "registro acreditacion":REGISTRO_ACREDITACION, 
                          "integrante dna":INTEGRANTE_DNA}
    
    return diccionario_ventanas[nombre_ventana]

def diccionarios_SUPERVISION(nombre_ventana):
    diccionario_ventanas={"SUPERVISIÓN":SUPERVISION,
                          "REGISTRO SUPERVISIÓN":REGISTRO_SUPERVISION}
    SUPERVISION={
        "ingresar_datos":{"Código DNA":{"By":"ID",
                              "elemento_web":"frmBuscar:busCodigo",
                              "tipo":"send"},

                "Fecha desde":{"By":"ID",
                              "elemento_web":"frmBuscar:j_idt331_input",
                              "tipo":"send"},

                "Fecha hasta":{"By":"ID",
                              "elemento_web":"frmBuscar:j_idt336_input",
                              "tipo":"send"},

                "Estado supervisado":{"By":"ID",
                              "elemento_web":"frmBuscar:selFiltro_label",
                              "tipo":"choose"},

                "Estado proceso":{"By":"ID",
                              "elemento_web":"frmBuscar:busEstado_label",
                              "tipo":"choose"},

                "Seleccionar supervisor":{"By":"ID",
                                          "elemento_web":"frmBuscar:selSupervisor_label",
                                          "tipo":"choose"},

                "Seleccionar supervisor":{"By":"ID",
                                          "elemento_web":"frmBuscar:selSupervisor_label",
                                          "tipo":"choose"},


                "Seleccionar supervisor":{"By":"ID",
                                          "elemento_web":"frmBuscar:selSupervisor_label",
                                          "tipo":"choose"},

                "Filtrar ubigeo":{"By":"ID",
                                  "elemento_web":{"departamento":"frmBuscar:busDepartamento_label", 
                                                  "provincia":"frmBuscar:busProvincia_label",
                                                  "distrito":"frmBuscar:busDistrito_label"},
                                  "tipo":"choose"}

                },
        "funcionales_DNA":{"Crear":{"By":"ID",
                                "elemento_web":'formularioPrincipal1:tablaSup:{n_DNA_row}:j_idt365',
                                "tipo":"click"},
                        "Editar":{"By":"ID",
                                "elemento_web":'formularioPrincipal1:tablaSup:{n_DNA_row}:tablaSup:{n_supervision_row}:j_idt369',
                                "tipo":"click"},

                        "Enviar":{"By":"ID",
                                "elemento_web":'formularioPrincipal1:tablaSup:{n_DNA_row}:tablaSup:{n_supervision_row}:j_idt370',
                                "tipo":"click"},

                        "Eliminar":{"By":"ID",
                                "elemento_web":'formularioPrincipal1:tablaSup:{n_DNA_row}:tablaSup:{n_supervision_row}:j_idt371',
                                "tipo":"click"},
                        "Ingresar supervisiones ":{"By":"XPATH",
                                "elemento_web":'//*[@id="formularioPrincipal1:tablaSup_data"]/tr[{n_row}]/td[1]/div',
                                "tipo":"click"},
                        }
        }
    
    num_preguntas = 84
    respecto_lista=["la entidad Responsable","la DNA y sus integrantes","los expedientes de atención de casos"]
    preguntas_xpath = {f"Pregunta {i}": {"By":"XPATH",
                                         "elemento_web": f'//*[@id="frmNuevo:j_idt233:{i-1}:j_idt235/tbody/tr/td[n_option]/div/div[2]"]' ,
                                         "tipo":"check options"} for i in range(1, num_preguntas + 1)}
    
    REGISTRO_SUPERVISION ={

        "ingresar_datos":{"Fecha":{"By":"ID",
                                "elemento_web":"frmNuevo:txtFecha_input",
                                "tipo":"send"},

                        "Hora":{"By":"ID",
                                "elemento_web":"frmNuevo:txtHora_input",
                                "tipo":"send"},

                        "Supervisor":{"By":"ID",
                                "elemento_web":"frmNuevo:selSupervisor_label",
                                "tipo":"choose"},

                        "Teléfono DNA":{"By":"ID",
                                "elemento_web":"frmNuevo:j_idt92",
                                "tipo":"send"},

                        "Correo DNA":{"By":"ID",
                                "elemento_web":"frmNuevo:j_idt95",
                                "tipo":"send"},

                        "Horario DNA":{"By":"ID",
                                "elemento_web":"frmNuevo:j_idt92",
                                "tipo":"send"},


                        "DNI Responsable":{"By":"ID",
                                "elemento_web":"frmNuevo:j_idt92",
                                "tipo":"send"},

                        "Fecha Responsable":{"By":"ID",
                                "elemento_web":"frmNuevo:j_idt95",
                                "tipo":"send"},

                        "Documento Responsable":{"By":"ID",
                                "elemento_web":"frmNuevo:j_idt92",
                                "tipo":"send"},


                        "Teléfono Responsable":{"By":"ID",
                                "elemento_web":"frmNuevo:j_idt95",
                                "tipo":"send"},

                        "Correo Responsable":{"By":"ID",
                                "elemento_web":"frmNuevo:j_idt92",
                                "tipo":"send"},


                        "Instruccion Responsable":{"By":"ID",
                                "elemento_web":"frmNuevo:j_idt92",
                                "tipo":"choose"},

                        "Profesion Responsable":{"By":"ID",
                                "elemento_web":"frmNuevo:j_idt95",
                                "tipo":"choose"},

                        "Colegio Responsable":{"By":"ID",
                                "elemento_web":"frmNuevo:j_idt92",
                                "tipo":"choose"},


                        "Max autoridad Responsable":{"By":"ID",
                                "elemento_web":"frmBuscar:busEstado_label",
                                "tipo":"choose"},

                        "Direccion entidad Responsable":{"By":"ID",
                                                "elemento_web":"frmBuscar:selSupervisor_label",
                                                "tipo":"choose"},

                        "Local DNA":{"By":"ID",
                                                "elemento_web":"frmBuscar:selSupervisor_label",
                                                "tipo":"choose"},

                        "Conservacion DNA":{"By":"ID",
                                                "elemento_web":"frmBuscar:selSupervisor_label",
                                                "tipo":"choose"},


                        "N° ambientes":{"By":"ID",
                                        "elemento_web":"frmBuscar:selSupervisor_label",
                                        "tipo":"choose"},

                        "Matriz RRHH":{
                            
                            "Nro Defensor Derecho M":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:1:j_idt191_input",
                                "tipo":"send"
                            },
                            "Nro Defensor Derecho H":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:1:j_idt193_input",
                                "tipo":"send"

                            },                                

                            "Nro Defensor T. Social M":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:1:j_idt195_input",
                                "tipo":"send"
                            },

                            "Nro Defensor T. Social H":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:1:j_idt197_input",
                                "tipo":"send"
                            },   

                            "Nro Defensor Psicologia M":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:1:j_idt199_input",
                                "tipo":"send"
                            },

                            "Nro Defensor Psicologia H":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:1:j_idt201_input",
                                "tipo":"send"
                            },   

                            "Nro Defensor Eduacion M":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:1:j_idt203_input",
                                "tipo":"send"
                            },

                            "Nro Defensor Eduacion H":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:1:j_idt205_input",
                                "tipo":"send"
                            },

                            "Nro Defensor Otro M":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:1:j_idt207_input",
                                "tipo":"send"
                            },   

                            "Nro Defensor Otro H":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:1:j_idt209_input",
                                "tipo":"send"
                            },

                            "Nro Promotor Derecho M":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:2:j_idt191_input",
                                "tipo":"send"
                            },   

                            "Nro Promotor Derecho H":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:2:j_idt193_input",
                                "tipo":"send"
                            },

                            "Nro Promotor T. Social M":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:2:j_idt195_input",
                                "tipo":"send"
                            }, 

                            "Nro Promotor T. Social H":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:2:j_idt197_input",
                                "tipo":"send"
                            },

                            "Nro Promotor Psicologia M":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:2:j_idt199_input",
                                "tipo":"send"
                            },   

                            "Nro Promotor Psicologia H":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:2:j_idt201_input",
                                "tipo":"send"
                            },

                            "Nro Promotor Eduacion M":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:2:j_idt203_input",
                                "tipo":"send"
                            },   

                            "Nro Promotor Eduacion H":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:2:j_idt205_input",
                                "tipo":"send"
                            },

                            "Nro Promotor Otro M":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:2:j_idt207_input",
                                "tipo":"send"
                            }, 

                            "Nro Promotor Otro H":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:2:j_idt209_input",
                                "tipo":"send"
                            }, 

                            "Nro P. Apoyo Derecho M":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:3:j_idt191_input",
                                "tipo":"send"
                            },

                            "Nro P. Apoyo Derecho M":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:3:j_idt193_input",
                                "tipo":"send"
                            },   

                            "Nro P. Apoyo T. Social M":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:3:j_idt195_input",
                                "tipo":"send"
                            },   

                            "Nro P. Apoyo T. Social H":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:3:j_idt197_input",
                                "tipo":"send"
                            },

                            "Nro P. Apoyo Psicologia M":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:3:j_idt199_input",
                                "tipo":"send"
                            }, 


                            "Nro P. Apoyo Psicologia H":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:3:j_idt201_input",
                                "tipo":"send"
                            },   

                            "Nro P. Apoyo Eduacion M":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:3:j_idt203_input",
                                "tipo":"send"
                            },

                            "Nro P. Apoyo Eduacion H":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:3:j_idt205_input",
                                "tipo":"send"
                            }, 


                            "Nro P. Apoyo Otro M":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:3:j_idt207_input",
                                "tipo":"send"
                            }, 

                            "Nro P. Apoyo Otro H":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:3:j_idt209_input",
                                "tipo":"send"
                            },

                            "Nro P. Administrativo Derecho M":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:4:j_idt191_input",
                                "tipo":"send"
                            },   

                            "Nro P. Administrativo Derecho H":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:4:j_idt193_input",
                                "tipo":"send"
                            },

                            "Nro P. Administrativo T. Social M":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:4:j_idt195_input",
                                "tipo":"send"
                            },   

                            "Nro P. Administrativo T. Social H":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:4:j_idt197_input",
                                "tipo":"send"
                            },

                            "Nro P. Administrativo Psicologia M":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:4:j_idt199_input",
                                "tipo":"send"
                            },

                            "Nro P. Administrativo Psicologia H":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:4:j_idt201_input",
                                "tipo":"send"
                            },   

                            "Nro P. Administrativo Eduacion M":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:4:j_idt203_input",
                                "tipo":"send"
                            },

                            "Nro P. Administrativo Eduacion H":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:4:j_idt205_input",
                                "tipo":"send"
                            },   

                            "Nro P. Administrativo Otro M":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:4:j_idt207_input",
                                "tipo":"send"
                            },

                            "Nro P. Administrativo Otro H":{
                                "By":"ID",
                                "elemento_web":"frmNuevo:j_idt162:4:j_idt209_input",
                                "tipo":"send"
                            }  
                        },

                        "Actividades ejecutadas":{"By":"ID",
                                        "elemento_web":"frmNuevo:txtActividades",
                                        "tipo":"send"},

                        "Actividades ejecutadas":{"By":"ID",
                                        "elemento_web":"frmNuevo:txtActividades",
                                        "tipo":"send"},

                        "COMUDENA":{"By":"XPATH",
                                        "elemento_web":"//*[@id='frmNuevo:rbComudena']/tbody/tr/td[{id_option}]/div/div[2]",
                                        "tipo":"check options"},

                        "COORDINADORA":{"By":"XPATH",
                                        "elemento_web":"//*[@id='frmNuevo:rbCoord']/tbody/tr/td[{id_option}]/div/div[2]",
                                        "tipo":"check options"},

                        "Actividades ejecutadas":{"By":"ID",
                                        "elemento_web":"frmNuevo:txtActividades",
                                        "tipo":"send"},

                        "Otros espacios":{"By":"ID",
                                        "elemento_web":"frmNuevo:txtCoordinadora",
                                        "tipo":"send"},

                        "Preguntas":preguntas_xpath

                        }

        }
    return diccionario_ventanas[nombre_ventana]

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