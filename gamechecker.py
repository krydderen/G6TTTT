"""
Object tracking based on a HSV-mask,
and will contour out the wanted red
or blue markers and find its place with
the 3x3 of Tic Tac Toe in mind.

Code by: Kevin Moen Storvik
Version: 1.5
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

    def getGamestateXO(self):
        """Find and return the current gamestate"""
        _, frame = self.cap.read()
        # Reset the gamestate for each cycle
        game_state = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
        # Set up 9 Region Of Interests with the 9 tiles of TTT in mind
        roi = frame[170:330, 275:438]

        # Set up 9 Region Of Interests with the 9 tiles of TTT in mind
        tiles = [roi[0:42, 0:48],
                 roi[0:42, 60:105],
                 roi[0:42, 120:160],
                 roi[55:95, 0:48],
                 roi[55:95, 60:105],
                 roi[55:95, 120:160],
                 roi[120:155, 0:45],
                 roi[120:155, 60:105],
                 roi[120:155, 120:160]]

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

        # self.watch(frame,dilation_blue,dilation_red)
        # Returns the flipped gamestate
        return np.flip(game_state)

    def getGamestate12(self):
        """Find and return the current gamestate"""
        _, frame = self.cap.read()
        # Reset the gamestate for each cycle
        game_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        # Create the region of interest
        roi = frame[170:330, 275:438]

        # Set up 9 Region Of Interests with the 9 tiles of TTT in mind
        tiles = [roi[0:42, 0:48],
                 roi[0:42, 60:105],
                 roi[0:42, 120:160],
                 roi[55:95, 0:48],
                 roi[55:95, 60:105],
                 roi[55:95, 120:160],
                 roi[120:155, 0:45],
                 roi[120:155, 60:105],
                 roi[120:155, 120:160]]

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
                game_state[index] = 2

            # Mark up only the largest red contour, and draw it.
            if len(contours_red) > 0:
                game_state[index] = 1

            # For each found contour, increment the INDEX by 1.
            index += 1

        # self.watch(frame,dilation_blue,dilation_red)
        # Returns the flipped gamestate
        return np.flip(game_state)

    def getWinCombo(self):

        win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [6, 3, 0], [7, 4, 1], [8, 5, 2], [6, 4, 2], [8, 4, 0]]

        state = self.getGamestateXO()

        print(state)
        winner = False
        wincombo = 0
        # Check if the current gamestate gives out any winners or a tie.
        for comb in win_combinations:
            # Check for a tie first, if no tie, check if "O" or "X" wins. If neither, continue the game
            if state[comb[0]] == "X" and state[comb[1]] == "X" and state[comb[2]] == "X":
                winner = True
                wincombo = (win_combinations.index(comb) + 1)
            elif state[comb[0]] == "O" and state[comb[1]] == "O" and state[comb[2]] == "O":
                winner = True
                wincombo = (win_combinations.index(comb) + 1)

        if not winner:
            wincombo = 9

        return wincombo

    def didSomeoneWin(self):

        win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [6, 3, 0], [7, 4, 1], [8, 5, 2], [6, 4, 2], [8, 4, 0]]

        state = self.getGamestateXO()

        print(state)
        winner = False
        # Check if the current gamestate gives out any winners or a tie.
        for comb in win_combinations:
            # Check for a tie first, if no tie, check if "O" or "X" wins. If neither, continue the game
            if state[comb[0]] == "X" and state[comb[1]] == "X" and state[comb[2]] == "X":
                winner = True
            elif state[comb[0]] == "O" and state[comb[1]] == "O" and state[comb[2]] == "O":
                winner = True
        return winner

    def getWinner(self):

        win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [6, 3, 0], [7, 4, 1], [8, 5, 2], [6, 4, 2], [8, 4, 0]]

        state = self.getGamestateXO()

        print(state)
        winner = "none"
        # Check if the current gamestate gives out any winners or a tie.
        for comb in win_combinations:
            # Check for a tie first, if no tie, check if "O" or "X" wins. If neither, continue the game
            if state[comb[0]] == "X" and state[comb[1]] == "X" and state[comb[2]] == "X":
                winner = "red"
            elif state[comb[0]] == "O" and state[comb[1]] == "O" and state[comb[2]] == "O":
                winner = "blue"
        return winner

    def cleanBoard(self):
        CLEAN = True

        _, frame = self.cap.read()

        roi = frame[170:330, 275:438]

        # Convert RGB to HSV
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

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
            CLEAN = False

        # Mark up only the largest red contour, and draw it.
        elif len(contours_red) > 0:
            CLEAN = False

        print("Is the board clean? " + str(CLEAN))
        return CLEAN


    def returnRemainingFields(self):
        """Returns the remainder of fields left after
            a board scan. This is used in the game modes
            to determine whether the fields are avaiable
            or not"""

        # Gets the fields
        fields = self.getGamestate12()
        index = 0

        # Available fields
        left = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for elem in fields:
            if int(elem) != 0:
                # Remove taken field from available fields
                left.pop(index)
            else:
                index += 1
        # Return the remaining fields.

        if str(np.array(left)) == "[]":
            left = [0]

        return left

    @staticmethod
    def watch(frame, dil_red, dil_blue):
        """Works as a debug functionality if user
         wants to see the frame and mask"""
        cv2.waitKey(1)
        cv2.imshow("Frame", frame)
        cv2.imshow("Dilation Red", dil_red)
        cv2.imshow("Dilation Blue", dil_blue)

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
        state = gameChecker.getGamestateXO()
        print(state)
        # Break loop with ESC-key
        key = cv2.waitKey(20) & 0xFF
        if key == 27:
            gameChecker.stop()
            break"""
