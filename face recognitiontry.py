import cv2

def recognize_faces():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)
    font = cv2.FONT_HERSHEY_SIMPLEX

    id_1 = "JASHAN"
    id_2 = "JASHAN"
    id_3 = "JASHAN"
    id_4 = "JASHAN"
    id_5 = "JASHAN"
    id_6 = "JASHAN"
    id_7 = "JASHAN"
    id_8 = "JASHAN"
    id_9 = "JASHAN"
    id_10 = "JASHAN"

    names = ['','JASHAN','JAHSAN','JASHAN','JASHAN','JASHAN','JASHAN','JASHAN','JASHAN','JASHAN','JASHAN',]

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 640)
    cam.set(4, 480)

    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    while True:
        ret, img = cam.read()
        converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(converted_image, scaleFactor=1.2, minNeighbors=5, minSize=(int(minW), int(minH)))

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

            id, accuracy = recognizer.predict(converted_image[y:y+h, x:x+w])

            if accuracy < 55:
                id = names[id]
                accuracy = "  {0}%".format(round(100 - accuracy))
            else:
                id = "Unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))

            cv2.putText(img, str(id), (x+5, y-5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(accuracy), (x+5, y+h-5), font, 1, (255, 255, 0), 1)

        cv2.imshow('camera', img)

        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break

    print("Thanks for using this program. Have a good day.")
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    recognize_faces()
