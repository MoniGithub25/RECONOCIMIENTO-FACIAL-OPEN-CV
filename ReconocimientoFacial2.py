import cv2
import numpy as np
import os

dataPath = 'C:/Users/DESPACHO TORRES/Desktop/RECONOCIMIENTO FACIAL2/Data' #Cambia a la ruta donde hayas almacenado Data
imagePaths = os.listdir(dataPath)
print('imagePaths=',imagePaths)

class Info:
    def __init__(self, name, apellido, alias, fecha_de_nacimiento, origen, objetivo, variable):
        self.name = name
        self.apellido = apellido
        self.alias = alias
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.origen = origen
        self.objetivo = objetivo
        self.variable= variable['VALOR1']

Monica = Info('MÓNICA DE LOURDES', 'GUERRERO TORRES',"Moni", "25/12/2002", "ESPAÑOLA", "VENGANZA", {'VALOR1':0})
Mamasita = Info('MÓNICA DE LOURDES', 'TORRES HIDALGO', "Come pollo","20/01/1972", "ECUATORIANA", "VIVIR", {'VALOR1':0})
Papasito = Info('ANTONIO', 'GUERRERO AMBITE', "Pendejo", "12/01/1958", "ESPAÑOLA", "VIVIR", {'VALOR1':0})
CapitanAmerica = Info('STEVE', 'ROGERS', "El trasero de america", "Muy viejo", "EEUU", "SALVAR AL MUNDO", {'VALOR1':0})

#face_recognizer = cv2.face.EigenFaceRecognizer_create()
#face_recognizer = cv2.face.FisherFaceRecognizer_create()
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Leyendo el modelo
#face_recognizer.read('modeloEigenFace.xml')
#face_recognizer.read('modeloFisherFace.xml')
face_recognizer.read('modeloLBPHFace.xml')



cap = cv2.VideoCapture(2,cv2.CAP_DSHOW)
#cap = cv2.VideoCapture('Monica.mp4')
#cap = cv2.VideoCapture('Monica_original.mp4')
#cap = cv2.VideoCapture('CaptainAmericaPrueba.mp4')


faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

while True:
    ret,frame = cap.read()
    if ret == False: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()

    faces = faceClassif.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
        result = face_recognizer.predict(rostro)

        cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
        
        '''
        # EigenFaces
        if result[1] < 5700:
            cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        else:
            cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
        
        # FisherFace
        if result[1] < 300:
            cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        
        else:
            cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
        '''
        
        # LBPHFace
        if result[1] < 150:
            cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            
            carpeta_str = str(imagePaths[result[0]])
            if carpeta_str == 'Monica' and Monica.variable == 0 and cv2.waitKey(1) == ord('p') :
                print("\n+++++++++++++++++++++++++")
                print ("\nINFORMACIÓN sobre <<Monica>>: ")
                print("NOMBRE: ", Monica.name)
                print("APELLIDO:", Monica.apellido)
                print("ALIAS:", Monica.alias)
                print("FECHA DE NACIMIENTO: ", Monica.fecha_de_nacimiento)
                print("ORIGEN: ", Monica.origen)
                print("OBJETIVO: ", Monica.objetivo)
                print("\n+++++++++++++++++++++++++")
                Monica.variable += 1
        else:
            cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
 
    cv2.imshow('frame',frame)
    k = cv2.waitKey(1)
    if k == ord('s'):
        break

cap.release()
cv2.destroyAllWindows()


   