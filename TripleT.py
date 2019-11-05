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
whidth = len(roi)
height = len(roi[0])
rect_list = list()

rect_list.append(
    cv.rectangle(roi,
                 (0, 0),
                 (int(whidth / 3), int(height / 3)),
                 (0, 255, 0),
                 thickness=10))
rect_list.append(
    cv.rectangle(roi,
                 (int(whidth / 3), 0),
                 (int(whidth * 2 / 3), int(height / 3)),
                 (0, 255, 0),
                 thickness=10))
rect_list.append(
    cv.rectangle(roi,
                 (int(whidth * 2 / 3), 0),
                 (int(whidth), int(height / 3)),
                 (0, 255, 0),
                 thickness=10))
rect_list.append(
    cv.rectangle(roi,
                 (0, int(height / 3)),
                 (int(whidth / 3), int(height * 2 / 3)),
                 (0, 255, 0),
                 thickness=10))
rect_list.append(
    cv.rectangle(roi,
                 (int(whidth / 3), int(height / 3)),
                 (int(whidth * 2 / 3), int(height * 2 / 3)),
                 (0, 255, 0),
                 thickness=10))
rect_list.append(
    cv.rectangle(roi,
                 (int(whidth * 2 / 3), int(height / 3)),
                 (int(whidth), int(height * 2 / 3)),
                 (0, 255, 0),
                 thickness=10))

rect_list.append(
    cv.rectangle(roi,
                 (0, int(height * 2 / 3)),
                 (int(whidth / 3), int(height)),
                 (0, 255, 0),
                 thickness=10))

rect_list.append(
    cv.rectangle(roi,
                 (int(whidth / 3), int(height * 2 / 3)),
                 (int(whidth * 2 / 3), int(height)),
                 (0, 255, 0),
                 thickness=10))

rect_list.append(
    cv.rectangle(roi,
                 (int(whidth * 2 / 3), int(height * 2 / 3)),
                 (int(whidth), int(height)),
                 (0, 255, 0),
                 thickness=10))

# Converting image to a binary image
# (black and white only image)
_, threshold = cv.threshold(roi, 110, 255, cv.THRESH_BINARY)

# Turn into threshold binary
ret, threshold1 = cv.threshold(roi, 127, 255, cv.THRESH_BINARY)

# Detecting shapes in image by selecting region
# with same colors or intensity.
# contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
"""
# Find and draw contours. RETR_EXTERNAL retrieves only the extreme outer contrours.
contours, hierarchy = cv.findContours(threshold1, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(roi, contours, -1, (0, 255, 0), 15)
"""
"""tileCount = 0
for cnt in contours:
    # ignore small contours that are not tiles
    if cv.contourArea(cnt) > 200000:
        tileCount = + 1
        # Use boundingRect to get coordinates of the tile
        x, y, w, h = cv.boundingRect(cnt)
        # Create a new image from binary, for further analysis. Trim of the edges that has a line.
        tile = threshold1[x + 40:x + w - 80, y + 40:y + h - 80]
        # Create a new image from the main image, so we can draw the contours easily
        imgTile = roi[x + 40:x + w - 80, y + 40:y + h - 80]

        # Determine the array indexes of the tile
        # TODO add a function to add the tiles

        # Put a number in each tile. TODO HAVE TO GET IT TO PUT A NUMBER CORRECTLY.
        cv.putText(roi, str(tileCount), (x + 200, y + 300), cv.FONT_HERSHEY_SIMPLEX, 10, (0, 0, 255), 20)


# Print the gamestate
print("Gamestate: ")
for line in GAMESTATE:
    linetxt = ""
    for cel in line:
        linetxt = linetxt + "|" + cel
        print(linetxt)
"""
# Resize the final image
res = cv.resize(roi, None, fx=0.8, fy=0.8, interpolation=cv.INTER_CUBIC)

# Display the final image and release resources when key is pressed
cv.imshow("IMAGE", res)
cv.waitKey(0)
cv.destroyAllWindows()
