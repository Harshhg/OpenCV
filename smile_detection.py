import cv2

smile_cascade=cv2.CascadeClassifier('smile.xml') # Smile haar cascade
face_cascade = cv2.CascadeClassifier('face.xml') # Face haar cascade

cap = cv2.VideoCapture(0)
# Replace the URL with your own IPwebcam shot.jpg IP:port
while True:
    # Now capturing the image..
    status,frame=cap.read()  # It will take first picture
    # Converting the image into gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Now applying face classifier in live frame..
    faces=face_cascade.detectMultiScale(gray,1.3,5)  #  arguments (image, Classifier tuning parameter..)
    for (x, y, w, h) in faces:
        # Drawing rectange around face
        cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)
        # Converting the face part into gray image for further smile detection.
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        # Calling smile casacade and passing the detected face.
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8,20)

        # Drawing rectangle around detected smile.
        for sx,sy,sw,sh in smiles:
            cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(0,0,255),2)

    cv2.imshow('face',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        bre
