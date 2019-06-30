import cv2
# Reading the image...
img=cv2.imread('dog.jpg')   # will store the image in numpy form.
print(type(img))  # Image type
print(img.shape)  # Image resolution..(or numpy array size)

# Cropping the image
cv2.imshow('croppedimage',img[30:400,100:400])

# Splitting image in to BGR..
b,g,r=cv2.split(img)
cv2.imshow('blue',b)
cv2.imshow('green',g)
cv2.imshow('red',r)

# inverse the image... Change BGR to RGB
img2=cv2.merge([r,g,b])
cv2.imshow('inverse',img2)

# Drawing a line on the image..
cv2.line(img,(0,0),(300,300), (0,0,255),3)
# arguments -> (image, (starting position), (ending position), (color in RGB format), thickness of line)

# Drawing a rectangle..
cv2.rectangle(img,(400,100),(200,250),(0,255,0),3)

# Drawing a circle..
cv2.circle(img, (500, 300), 100, (255, 0, 0), 2)
# arguments -> (image, (center point), radius, (color in RGB), thickness)

# Displaying the image
cv2.imshow('edited',img)
cv2.waitKey(0)
