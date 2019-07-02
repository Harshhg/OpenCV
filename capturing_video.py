import cv2
# Starting CAMERA
cap=cv2.VideoCapture(0)  # camera number ..

# Adding the video plugin
plugin=cv2.VideoWriter_fourcc(*'XVID')    # The plugin we want to use - (XVID -supports .avi, .mp4)
# Now saving video
output=cv2.VideoWriter('myvideo.avi', plugin,  30  ,   (640,480))
# Arguments - (filename, frame speed(slow or fast), FRAME Resolution(width,height)

# Checks if camera is started or not..
while cap.isOpened():
    status,frame=cap.read()  # It will take first picture
    # Converting image frame into gray scale..
    grayimg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    print(frame.shape)

    # Sending data to video writer
    output.write(frame)

    cv2.imshow('grayimage',grayimg)
    cv2.waitKey(10)
    #cv2.waitKey(10)  # the image will close every 10 millisecond.. so  you will see live video image..

    # Window will not close automatically here, so we attach key handler to opencv
    if cv2.waitKey(10) & 0xff == ord('q') :
        break

cv2.destroyAllWindows()  # To destroy all windows

# To close the camera..
cap.release()
