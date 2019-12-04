# Importing packages
from modbus_communication import ModbusClient
import time
import cv2
import numpy as np
from gamechecker import GameChecker

# Dictionary holding Modbus addresses
addresses = {
    '0': 140,
    '1': 141,
    '2': 142,
    'kkk': 148,
    'test': 149,
    'exampleRead': 000,
    'exampleSend': 000,
    'win': 150
}

# Reset the gamestate for each cycle
game_state = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

# Create a list of all possible win combinations
"""                     1          2          3          4          5          6          7          8  """
win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [6, 3, 0], [7, 4, 1], [8, 5, 2], [6, 4, 2], [8, 4, 0]]

# Main loop
if __name__ == '__main__':

    # Creating the client and camera capture.
    #client = ModbusClient(ip='158.38.140.250')
    cap = cv2.VideoCapture(1)
    # TODO -  SCALE DOWN THE CAPTURE

    game = GameChecker(capture=cap, watch=True)

    print("Objects created.")
    print("Client connecting...")
    while 1:

        """This is used for testing when I cannot use our
        robot for testing when I am away from the LAB"""
        string = str(input("enter below\n"))
        print(string)


        """Just a test"""
        if string == "s":
            game.

        if string == "check":
            print(str(game.getGamestateXO()))

        if string == "clean":

            if not game.cleanBoard():
                print("Needs clean")
            elif game.cleanBoard():
                print("its clean nigga")

        if string == "stop":
            print("Closing...\nThank you for shutting "
                  "me down properly\n"
                  "Good bye :) <3")
            game.stop()
            break
