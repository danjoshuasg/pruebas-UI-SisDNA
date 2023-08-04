import pandas as pd
import json

ubigeo_df = pd.read_excel('ubigeo_excel.xlsx')

diccionario_ubigeo = {}

#Iterar sobre las filas del dataframe del ubigeo
for _, row in ubigeo_df.iterrows():
    departamento = row["DEPARTAMENTO"]
    provincia=row["PROVINCIA"]
    distrito=row["DISTRITO"]

    #Si el departamento existe en el diccionario
    if departamento in diccionario_ubigeo:
        #Si la provincia existen en departamento
        if provincia in diccionario_ubigeo[departamento]:
            diccionario_ubigeo[departamento][provincia].append(distrito)
        else:
            #Si la provincia no existe en el departamento crear
            diccionario_ubigeo[departamento][provincia] = [distrito]
    #Si el valor del departamento no existe en el diccionario se crea un nuevo diccionario
    else:
        diccionario_ubigeo[departamento] = {provincia:[distrito]}


# Nombre del archivo JSON de salida
output_file = 'ubigeo.json'

# Guarda el diccionario en el archivo JSON
with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(diccionario_ubigeo, json_file, indent=4, ensure_ascii=False)


