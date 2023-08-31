# KosmosChallenge

Aclaraciones:
- Para simular que a un cliente quiera utilizar la API se pueden de diferentes formas, 
    personalmente Utilice Postman por lo cual en esta explicación lo utilizare de ejemplo
 
Para ejecutar el api se realizarán los siguientes pasos:
- Ejecutar el programa de Python: main.py desde la terminal
- Mientras se está ejecutando este proporcionara una dirección IP, a mí me da la siguiente: http://127.0.0.1:5000
- Con Postman copiamos la dirección IP anteriormente mencionada junto con: "challenge" 
    en el apartado "URL or paste text" quedando la nueva direccion de esta forma: http://127.0.0.1:5000/challenge
- Dentro del apartado "Body" elegimos la opción "raw" y aquí dentro de las opciones 
    que aparecen a la derecha verificamos que este seleccionado JSON'
- dentro del cuerpo de esta área debe ir el texto que contiene las oraciones a identificar
- Verificamos que la opción que se utilizara sea POST
- Damos clic a "Send"
- Debe salir un mensaje que dice "Datos analizados y guardados" lo cual nos notifica que el proceso fue exitoso
- Donde se aloje la API se creó un archivo JSON "data analyzed.json" con el resultado correspondiente
