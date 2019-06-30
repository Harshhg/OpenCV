import cv2

print(cv2.__version__)

# Reading the image..
img=cv2.imread('cat.jpg',1)
#  1  -  means image in same color
#  0  -  means image in Black and White  --- Gray Image
# -1  -  maintain image transparency (in case of image over image)

print(img.shape)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
