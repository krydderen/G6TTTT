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
    client = ModbusClient()
    cap = cv2.VideoCapture(0)
    # TODO -  SCALE DOWN THE CAPTURE

    game = GameChecker(capture=cap, watch=True)

    print("Objects created.")
    print("Client connecting...")
    while client.isConnected():

        """This is used for testing when I cannot use our
        robot for testing when I am away from the LAB"""
        string = str(input("enter below\n"))
        print(string)

        """If the EXAMPLE addresses picks up the int. 1, it means 
        that the machines are idle and we are now ready to capture 
        the current gamestate. When the gamestate is captured, we then
        take the gamestate and compare them with all the possible 
        winning combinations in a 3x3 tic tac toe game. When this is done,
        we can send out an int to the PLS or UR3 robot where we either signal
        that a win combination was found, along with which combination that won,
        signal that it was a tie and nobody won, or that nobody has won yet
        and the game can continue."""
       # if client.readInt(address=addresses['exampleRead'], size=1) == 1:
        if string == "cam":

            # Fetch the game state
            game_state = game.getGamestate()

            # Check if the current gamestate gives out any winners or a tie.
            for comb in win_combinations:
                # Check for a tie first, if no tie, check if "O" or "X" wins. If neither, continue the game
                if "-" not in game_state:
                    """ - A DEBUG PRINT - """
                    print("Nobody wins, game ends in a tie.")

                    """ - SENDING SIGNAL - """
                    """ ~ THE VALUE HERE IS 9, WHICH MEANS A TIE. ~ """
                    client.sendInt(address=addresses['win'], value=9)

                    # TODO -  PROBABLY HAVE TO HAVE EVERY OF THE EIGHT COMBINATIONS HERE...
                elif game_state[comb[0]] == "X" and game_state[comb[1]] == "X" and game_state[comb[2]] == "X":
                    """ - A DEBUG PRINT ¯\_(ツ)_/¯ - """
                    print("Player X wins.")

                    """ ~ INT WHICH HOLDS WHICH COMBO WON ~ """
                    wincombo = 0

                    """ - SENDING SIGNAL - """
                    """ ~ THE VALUE SENT HERE GOES FROM 1-8, WHICH IS WHERE THE WIN WAS FOUND FOR "X" 
                        SO THAT WE CAN GET THE ROBOT TO MARK THE WINNING ROW, COLUMN OR DIAGONAL ~ """
                    client.sendInt(address=addresses['win'], value=wincombo)

                elif game_state[comb[0]] == "O" and game_state[comb[1]] == "O" and game_state[comb[2]] == "O":
                    """ - A DEBUG PRINT ¯\_(ツ)_/¯ - """
                    print("Player O wins.")

                    """ ~ INT WHICH HOLDS WHICH COMBO WON ~ """
                    wincombo = 0

                    """ - SENDING SIGNAL - """
                    """ ~ THE VALUE SENT HERE GOES FROM 1-8, WHICH IS WHERE THE WIN WAS FOUND FOR "O" 
                        SO THAT WE CAN GET THE ROBOT TO MARK THE WINNING ROW, COLUMN OR DIAGONAL ~ """
                    client.sendInt(address=addresses['win'], value=wincombo)

                    """ ~ IF NO WINS OR TIE IS FOUND, SEND 0 ~ """
                else:
                    client.sendInt(address=addresses['win'], value=0)



        """ ~ VENTURING FURTHER DOWN THE CODE IS JUST A DEMONSTRATION AND TESTING OF THE KODE ~ """

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
