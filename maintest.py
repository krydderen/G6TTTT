# Importing packages
from modbus_communication import ModbusClient
import time
import cv2
import numpy as np
from gamecheckerTESTER import GameChecker

# Dictionary holding Modbus addresses
addresses = {
    '0': 140,
    '1': 141,
    '2': 142,
    'kkk': 148,
    'test': 149
}

# Reset the gamestate for each cycle
game_state = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

# Create a list of all possible win combinations
win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [6, 3, 0], [7, 4, 1], [8, 5, 2], [6, 4, 2], [8, 4, 0]]

# Main loop
if __name__ == '__main__':

    # Creating the client and camera capture.
    # client = ModbusClient()
    cap = cv2.VideoCapture(0)
    game = GameChecker(capture=cap, watch=True)

    print("client created")
    print("Client connecting...")
    client = True
    while client:
        """This is used for testing when I cannot use our
        robot for testing when I am away from the LAB"""
        string = str(input("enter below\n"))
        print(string)

        """Just a test lmao"""
        if string == "lmao":
            print("epiclmao")

        """ TODO - change this to a statement where
        if the PLS or the UR3 robot asks for the game status, 
        send either that someone has won or a tie is found. 
        If else, send out a signal that implies that the game can'
        continue untill further notice."""
        if string == "cam":
            print(str(game.getGamestate()))

        if string == "check":
            print()
            """get and check the current gamestate up towards
            the winning conditions. This t"""
        if string == "stop":
            print("Closing...\nThank you for shutting "
                  "me down properly\n"
                  "Good bye :) <3")
            game.stop()
            break
