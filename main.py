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
    var = 0
    resultadoFinal = []
    plantillaResultado = {
        }

    #Convertimos a JSON la informacion que se envia desde el cliente, "request.data" es vital para que llegue solo el JSON que envia el cliente
    data = json.loads(request.data)
    #Filtramos las oraciones del JSON
    z = data["oraciones"]

    #Ciclo para evaluar cada oracion por separado
    for i in z:
        #variables que se resetearan por iteración
        entidades = []
        resultadoNuevo = plantillaResultado.copy()
        resultadoNuevo["resultado"] = []
        #Identificador de la oracion en curso con su sumador para pasar a la siguiente
        m = z[var]
        var += 1
        #Variable que almacenara la informacion que utiliza Spacy para poder identificar lo que se desea
        doc = nlp(m)

        for token in doc:
            #Filtro para solo guardar los datos solicitados
            if token.ent_type_ == "LOC" or token.ent_type_ == "ORG":
                print(token.text, token.ent_type_)
                entidades.append("{} : {}".format(token.text, token.ent_type_))

            else:
                None
                
        #Diccionario temporal que se añadira al disccionario final y se resetea con la repeticion
        ultimodic = {
            "óracion" : m,
            "entidades" : entidades
        }
        resultadoNuevo["resultado"].append(ultimodic)

        #Añadimos la información al diccionario final
        resultadoFinal.append(resultadoNuevo)

    #Guardamos el archivo JSON
    with open("myfile.json", "w") as j:
        json.dump(resultadoFinal, j, ensure_ascii=False, indent= 2)

    #Aviso al cliente
    return "salio bien"

#Con esto ejecutamos la api
app.run(debug=True)