# RECONOCIMIENTO-FACIAL-OPEN-CV
Reconococimiento facial mediante OpenCv (este proyecto neceseita varios pasos más que el proyecto hecho en face recognition pero va una mejor velocidad, aunque como parte de sus desventajas es que es complicado intentar detectar más de dos rostros porque se empieza a liar)
El primer paso es hacer un video de la cara con distintos gestos para que podamos reconocer nuestra cara (es mejor grabar dos videos distintos con distinta iluminacion para obtener los parametros adecuados que debemos usar)
Esos rostros se guardan en una carpeta llamada Data en mi caso. Esa imagenes las usamos en el entrenamiento para obtener los parametros aproximados para que a partir de esos paramentros podamos detectar nuestra cara
Además de eso obtenemos esta vez tres archivos .xml distintos: modelo EigenFaces, FisherFace, LBPHFace.
En el ultimo programa de python utilizamos la videocamara y a partir de los archivo que hemos creado llamado LBPHFFace creamos una variable face _recognizer para asi poder reconocer la cara de cada persona que hayamos guardado en el archivo
Una vez hecho el programa se me ocurrió que sería divertido hacer como en Hawaii 5.0 que localizan al sospechoso por reconocimiento facial y después buscan sus datos. Pues algo asi con la funcion class para poner los datos necesarios de cada persona archivada
Asi en el terminal aparece la información de la persona que reconoce.

SIMPLE DETECCION DE ROSTRO:
![Detector de caras](https://user-images.githubusercontent.com/111430658/187043030-d54b3e03-174a-4481-a9ea-00a141f1086e.PNG)

RECONOCIMIENTO FACIAL
![RECONOCIMIENTO FACIAL FINAL](https://user-images.githubusercontent.com/111430658/187043036-eddf4bb1-0be7-4b06-9a98-7e2152f7c9a0.PNG)

RECONOCIMIENTO FACIAL CON INFO SOBRE LA PERSONA:
![RECONOCIMIENTO FACIAL E INFO](https://user-images.githubusercontent.com/111430658/187043034-460afc59-02a9-40c7-b489-3c170023b405.PNG)

# CAMARA VIGILANTE (MOVIL/ DroidCamApp)
Hay que cambiar el index de VideoCapture ya sea 1 o 2. El index original de la camara del ordenador siempre será 0.

![image](https://user-images.githubusercontent.com/111430658/187084009-65495a5d-879d-4a86-b330-125d23054211.png)
