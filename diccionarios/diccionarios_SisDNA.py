

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

if __name__ == "__main__":
    diccionarios_SisDNA()