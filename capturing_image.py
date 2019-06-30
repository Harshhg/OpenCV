import cv2
# Starting CAMERA
cap=cv2.VideoCapture(0)  # camera number ..
# 0 - means first camera..i.e., internal camera
# 1 - next connected camera.

# Checks if camera is started or not..
if cap.isOpened():
    print("Camera is ready to take Pictures")
else:
    print("Camera not found")

# Now we can take read input from camera
status,img=cap.read()  # It will take first picture
status1,img1=cap.read()  # It will take second picture
# cap.read() will give two outputs
# status = camera is on or not
# img = Actual image

# Printing the image size..
print(img.shape)

# Now showing the image
cv2.imshow('liveimage',img)
cv2.imshow('liveimage1',img1)
cv2.waitKey(0)  # Holds the window for infinite time.

# To close the camera..
cap.release()

