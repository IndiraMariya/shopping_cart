import cv2 as cv

# Read the image
image = cv.imread('./images/cart1.jpg')

# Display the image
cv.imshow('Image', image)

# Wait for a key press and then close the window
cv.waitKey(0)
cv.destroyAllWindows()