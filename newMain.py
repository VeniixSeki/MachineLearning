#Librerias utilizadas
from flask import Flask, jsonify, request
import json
import spacy

#Configuración de la aplicación
app = Flask(__name__)

#Ruta donde se alojara la api
@app.route('/challenge', methods=["POST"])
def user_action():
    #Cargamos la configuración en español de Spacy
    nlp = spacy.load("es_core_news_sm")

    #Variables que utiliza el programa
    numDeOracion = 0
    ContadorLoc = 0
    plantillaResultado = {
        "resultado" : []
        }

    #Convertimos a JSON la informacion que se envia desde el cliente, "request.data" es vital para que llegue solo el JSON que envia el cliente
    data = json.loads(request.data)
    #Filtramos las oraciones del JSON
    listaDeOraciones = data["oraciones"]

    #Ciclo para evaluar cada oracion por separado
    for i in listaDeOraciones:
        #variables que se resetearan por iteración
        entidades = []
        resultadoFinal = plantillaResultado.copy()

        #Identificador de la oracion en curso con su sumador para pasar a la siguiente
        m = listaDeOraciones[numDeOracion]
        numDeOracion += 1
        #Variable que almacenara la informacion que utiliza Spacy para poder identificar lo que se desea
        doc = nlp(m)

        #analizamos palabra por palabra de la oración en curso
        for token in doc:
            #Filtro para solo guardar los datos solicitados
            if  token.ent_type_ == "ORG":
                entidades.append("{} : {}".format(token.text, token.ent_type_))
            
            elif token.ent_type_ == "LOC":
                ContadorLoc += 1
                #este caso es para cuando haya una locación que contenga 2 palabras
                if ContadorLoc > 1:
                    palabraAnterior = "{} {} : {}".format(palabraAnterior, token.text, token.ent_type_)
                    entidades.pop()
                    entidades.append(palabraAnterior)
                else:
                    palabraAnterior = token.text
                    entidades.append("{} : {}".format(token.text, token.ent_type_))
            #reiniciamos el contador de arriba e ignoramos las palabras que no tengan relación con lo solicidado
            else:
                ContadorLoc = 0
                
        #Diccionario temporal que se añadira al disccionario final y se resetea con la repeticion
        ultimodic = {
            "óracion" : m,
            "entidades" : entidades
        }

        #Añadimos la información al diccionario final
        resultadoFinal["resultado"].append(ultimodic)


    #Guardamos el archivo JSON, utilizamos encoding="utf-8" para mantener los caracteres como acentos o la "ñ"
    with open("data analyzed.json", "w", encoding="utf-8") as j:
        json.dump(resultadoFinal, j, ensure_ascii=False, indent= 2)

    #Aviso al cliente
    return "Datos analizados y guardados"

#Ejecutamos la api
app.run(debug=True)