import cv2
# Starting CAMERA
cap=cv2.VideoCapture(0)  # camera number ..
# 0 - means first camera..i.e., internal camera
# 1 - next connected camera.

# Checks if camera is started or not..
while cap.isOpened():   # Until camera is ON.
    status,frame=cap.read()  # It will take first picture

    # Converting image frame into gray scale..
    grayimg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    print(frame.shape)

    # Drawing a rectangle and circle
    cv2.rectangle(frame, (150, 50), (400, 300), (0, 255, 255), 3)
    cv2.circle(grayimg,(200,200), 100, (255,0,255),2)

    # Displaying the images
    cv2.imshow('liveimage',frame)
    cv2.imshow('grayimage',grayimg)
    #cv2.waitKey(0)
    cv2.waitKey(10)  # the image will close every 10 millisecond.. so  you will see live video image..

    # Window will not close automatically here, so we attach key handler to opencv
    if cv2.waitKey(10) & 0xff == ord('q') :
        break
    # Here ord- will get the ascii value of 'q'
    # When we press q, it will get ascii value and hand it to 0xff and break the loop.
    # Now all the below code will be executed..

#cv2.destroyWindow('liveimage')  # To destroy a single window
cv2.destroyAllWindows()  # To destroy all windows

# To close the camera..
cap.release()
