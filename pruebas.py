import json
import spacy
from spacy.lang.es.examples import sentences

#Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.
#San Francisco considera prohibir los robots de entrega en la acera.

# a Python object (dict):
x = {
    "oraciones": [
        "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
        "San Francisco considera prohibir los robots de entrega en la acera."
 ]
}

y = json.dumps(x, indent=2)
# the result is a JSON string:
#print(y)
var = 0
rep = False
lista = []
resultadoFinal = []

plantillaResultado = {
    }

nlp = spacy.load("es_core_news_sm")
z = x["oraciones"]
for i in z:
    entidades = []
    resultadoNuevo = plantillaResultado.copy()
    resultadoNuevo["resultado"] = []
    print("*********")
    m = z[var]
    var += 1
    doc = nlp(m)

    print(doc.text)
    for token in doc:
        if token.ent_type_ == "LOC" or token.ent_type_ == "ORG":
            print(token.text, token.ent_type_)
            entidades.append("{} : {}".format(token.text, token.ent_type_))
            #token.pos_, token.dep_, token.ent_type_, token.ent_id_}

            rep = True            
        else:
            rep = False 
    ultimodic = {
        "óracion" : m,
        "entidades" : entidades
    }
    
    resultadoNuevo["resultado"].append(ultimodic)
    resultadoFinal.append(resultadoNuevo)


with open("myfile.json", "w") as j:
    json.dump(resultadoFinal, j, ensure_ascii=False, indent= 2)