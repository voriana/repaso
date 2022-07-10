listaDDiccionarios=[{

    "nombre":"Oriana",
    "edad": 36,
    "genero": "Femenino",
    "nacionalidad": "venezolana"
},{

    "nombre":"Cristian",
    "edad": 37,
    "genero": "Masculino",
    "nacionalidad": "venezolana"
}]

for elem in listaDDiccionarios:
    elem["apellido"]="familia Rios Varela"
print(listaDDiccionarios)

diccionario={

    "nombre":"Rufus",
    "edad": 39,
    "genero": "Masculino",
    "nacionalidad": "Argentino"
}

# para obtener los valores de una lista
for clave, valor in list(diccionario.items()):
    print(clave, valor)

# anidados
familia={
    "Madre":"Oriana Varela",
    "habilidades":["autodidatacta","perseverante","agil"],
    "residencias":{
        "ResidenciaNac":"Venezolana",
        "ResidenciaHere":"Colombiana",
        "ResidenciaCasa":"Argentina"
    },
    "Comidas":["Arroz", "Pasta", "Pescado"]

    
    
}

indexbuscar=2


print(list(familia.items())[indexbuscar])
print(familia["residencias"]["ResidenciaNac"])
print(familia["Comidas"][1])