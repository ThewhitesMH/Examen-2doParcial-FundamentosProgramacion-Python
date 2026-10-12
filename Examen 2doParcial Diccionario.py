marcas_de_celulares = {
    "Marca 1":{
        "Nombre de la marca": "Apple",
        "Cantidad de Modelos": 4,
        "Modelos":["E","Base","Pro","Pro Max"] 
    },
    "Marca 2":{
        "Nombre de la marca": "Samsung",
        "Cantidad de Modelos": 3,
        "Modelos":["Base","Plus","Ultra"]
    },
    "Marca 3":{
        "Nombre de la marca": "Xiaomi",
        "Cantidad de Modelos": 4,
        "Modelos":["Redmi","Note","Mi","Poco"]
    },
    "Marca 4":{
        "Nombre de la marca": "Oppo",
        "Cantidad de Modelos": 2,
        "Modelos":["Reno","Find"]
    },
    "Marca 5":{
        "Nombre de la marca": "Oneplus",
        "Cantidad de Modelos": 2,
        "Modelos":["Nord","Number"]
    }
}
for clave, valor in marcas_de_celulares.items():
    print(clave)
    print(valor['Nombre de la marca'])
    print(valor['Cantidad de Modelos'])
    print(valor['Modelos'])
    for lista in valor['Modelos']:
        print("Modelo:", lista)    
    