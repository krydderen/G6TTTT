import cv2 as cv
import numpy

x1 = 630
x2 = 1320
y1 = 120
y2 = 790

GAMESTATE = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

IMAGE = 'test_images/test_image.png'

# Reading image
img2 = cv.imread(IMAGE, cv.IMREAD_COLOR)

# Reading same image in another variable
# and converting to grayscale
img = cv.imread(IMAGE, cv.IMREAD_GRAYSCALE)

# Cropping the image with HEIGHTNR1
roi = img2[y1:y2, x1:x2]

# Collect the height and width of the image
height, width = roi.shape[:2]

# Make a list where we can add the following tiles
rect_list = list()

# Tile number #1
rect_list.append(
    cv.rectangle(roi,(0, 0),(int(width / 3), int(height / 3)),(0, 255, 0),thickness=10))
# Tile number #2
rect_list.append(
    cv.rectangle(roi,(int(width / 3), 0),(int(width * 2 / 3), int(height / 3)),(0, 255, 0),thickness=10))
# Tile number #3
rect_list.append(
    cv.rectangle(roi,(int(width * 2 / 3), 0),(int(width), int(height / 3)),(0, 255, 0),thickness=10))
# Tile number #4
rect_list.append(
    cv.rectangle(roi,(0, int(height / 3)),(int(width / 3), int(height * 2 / 3)),(0, 255, 0),thickness=10))
# Tile number #5
rect_list.append(
    cv.rectangle(roi,(int(width / 3), int(height / 3)),(int(width * 2 / 3), int(height * 2 / 3)),(0, 255, 0),thickness=10))
# Tile number #6
rect_list.append(
    cv.rectangle(roi,(int(width * 2 / 3), int(height / 3)),(int(width), int(height * 2 / 3)),(0, 255, 0),thickness=10))
# Tile number #7
rect_list.append(
    cv.rectangle(roi,(0, int(height * 2 / 3)),(int(width / 3), int(height)),(0, 255, 0),thickness=10))
# Tile number #8
rect_list.append(
    cv.rectangle(roi,(int(width / 3), int(height * 2 / 3)),(int(width * 2 / 3), int(height)),(0, 255, 0),thickness=10))
# Tile number #9
rect_list.append(
    cv.rectangle(roi,(int(width * 2 / 3), int(height * 2 / 3)),(int(width), int(height)),(0, 255, 0),thickness=10))

tileCount = 0
x = 50
y = 50
for tile in rect_list:
    tileCount += 1
    cv.putText(roi, str(tileCount), (x, y) , cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), thickness=5)
    x += 50
    y += 50

# Converting image to a binary image
# (black and white only image)
_, threshold = cv.threshold(roi, 110, 255, cv.THRESH_BINARY)

# Turn into threshold binary
ret, threshold1 = cv.threshold(roi, 127, 255, cv.THRESH_BINARY)

# Resize the final image
res = cv.resize(roi, None, fx=0.8, fy=0.8, interpolation=cv.INTER_CUBIC)

# Display the final image and release resources when key is pressed
cv.imshow("IMAGE", res)
cv.waitKey(0)
cv.destroyAllWindows()
