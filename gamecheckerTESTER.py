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

        # Shows the picture captured and used for calculating winners, tie or scan again
        return game_state

    @staticmethod
    def watch(frame):
        """Works as a debug finctionality if user
         wants to see the frame and mask"""
        cv2.imshow("Frame", frame)

    def stop(self):
        """Releases the calture and close all frames running.
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
