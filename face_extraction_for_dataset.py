import cv2
import os
face_cascade = cv2.CascadeClassifier('face_haar_cascade.xml')
i=0
path='images\harsh'
for img in os.listdir(path):
    img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)

    faces = face_cascade.detectMultiScale(img_array,1.5,5)
    i+=1
    fn=str(i)+".jpg"
    for x,y,h,w in faces:
        roi = img_array[y:y+h,x:x+w]
        new = cv2.resize(roi,(500,500))
        cv2.imwrite(fn,new)
