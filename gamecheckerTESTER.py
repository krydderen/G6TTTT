"""
Object tracking based on a HSV-mask,
and will contour out the wanted red
or blue markers and find its place with
the 3x3 of Tic Tac Toe in mind.

Code by: Kevin Moen Storvik
"""

# Importing packages.
import cv2
import numpy as np
import time


class GameChecker(object):

    def __init__(self, capture, watch):
        self.frame = watch
        self.cap = capture
        # Create the lower and upper boundaries of the color blue
        self.lower_blue = np.array([93, 54, 51])
        self.upper_blue = np.array([135, 216, 255])

        # Create the lower and upper boundaries of the color red
        self.lower_red = np.array([0, 165, 4])
        self.upper_red = np.array([80, 255, 255])

    def getGamestate(self):
        """Find and return the current gamestate"""
        _, frame = self.cap.read()

        # Reset the gamestate for each cycle
        game_state = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

        """Will add the checking of all the tiles here..."""

        # TODO - SCALE DOWN THE FRAME TO FIT WHITEBOARD DIMENSIONS...

        roi = frame[170:330, 275:438]

        # Set up 9 Region Of Interests with the 9 tiles of TTT in mind
        tiles = [roi[0:45, 0:48],
                 roi[0:45, 60:105],
                 roi[0:45, 120:160],
                 roi[55:100, 0:48],
                 roi[55:100, 60:105],
                 roi[55:100, 120:160],
                 roi[115:155, 0:48],
                 roi[115:155, 60:105],
                 roi[115:155, 120:160]]

        index = 0

        for tile in tiles:

            # Convert RGB to HSV
            hsv = cv2.cvtColor(tile, cv2.COLOR_BGR2HSV)

            # Create the masks
            blue_mask = cv2.inRange(hsv, self.lower_blue, self.upper_blue)
            red_mask = cv2.inRange(hsv, self.lower_red, self.upper_red)

            # Enlarge the masks
            kernel = np.ones((5, 5), np.uint8)
            dilation_blue = cv2.dilate(blue_mask, kernel)
            dilation_red = cv2.dilate(red_mask, kernel)

            # Finding the contours
            contours_blue, hierarchy = cv2.findContours(dilation_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours_red, hierarchy = cv2.findContours(dilation_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            # Mark up only the largest blue contour and draw it.
            if len(contours_blue) > 0:
                game_state[index] = "O"

            # Mark up only the largest red contour, and draw it.
            if len(contours_red) > 0:
                game_state[index] = "X"

            # For each found contour, increment the INDEX by 1.
            index += 1

        # Returns the flipped gamestate
        return np.flip(game_state)

    @staticmethod
    def watch(frame):
        """Works as a debug functionality if user
         wants to see the frame and mask"""
        cv2.imshow("Frame", frame)

    def stop(self):
        """Releases the capture and close all frames running.
        Return. True when everything is closed."""
        self.cap.release()
        cv2.destroyAllWindows()
        return True


"""# Simple example of usage.
if __main__ == '__main__':
    cap = cv2.VideoCapture(0)
    gameChecker = GameChecker(capture=cap, watch=True)

    while True:
        state = gameChecker.getGamestate()
        print(state)
        # Break loop with ESC-key
        key = cv2.waitKey(20) & 0xFF
        if key == 27:
            gameChecker.stop()
            break"""
