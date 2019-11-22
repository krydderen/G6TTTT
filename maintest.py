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
    client = ModbusClient(ip='158.38.140.250')
    cap = cv2.VideoCapture(1)
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

            print(game_state)

            wincombo = 0
            # Check if the current gamestate gives out any winners or a tie.
            for comb in win_combinations:
                # Check for a tie first, if no tie, check if "O" or "X" wins. If neither, continue the game
                if "-" not in game_state:
                    """ - SENDING SIGNAL - """
                    """ ~ THE VALUE HERE IS 9, WHICH MEANS A TIE. ~ """
                    wincombo = 9

                    # TODO -  PROBABLY HAVE TO HAVE EVERY OF THE EIGHT COMBINATIONS HERE...
                elif game_state[comb[0]] == "X" and game_state[comb[1]] == "X" and game_state[comb[2]] == "X":
                    wincombo = (win_combinations.index(comb) + 1)
                elif game_state[comb[0]] == "O" and game_state[comb[1]] == "O" and game_state[comb[2]] == "O":
                    wincombo = (win_combinations.index(comb) + 1)

            print(wincombo)
            client.sendInt(address=addresses['win'], value=wincombo)

            """ Try to send win-combination. """
            """try:
                intwin = int(wincombo)

                if intwin == 0:
                    print(str(intwin) + " was found, continue..")

                elif intwin in range(1,8):
                    print(str(intwin) + " was found, winner decided.")

                elif intwin == 9:
                    print(str(intwin) + " was found, tie decided.")

                client.sendInt(address=addresses['win'],value=intwin)
            except ValueError:
                print("Value out of bounds.")

"""

        """ ~ VENTURING FURTHER DOWN THE CODE IS JUST A DEMONSTRATION AND TESTING OF THE KODE ~ """

        """Just a test lmao"""
        if string == "lmao":
            print("epiclmao")

        """ TODO - change this to a statement where
        if the PLS or the UR3 robot asks for the game status, 
        send either that someone has won or a tie is found. 
        If else, send out a signal that implies that the game can'
        continue untill further notice."""
        if string == "check":
            print(str(game.getGamestate()))

        if string == "stop":
            print("Closing...\nThank you for shutting "
                  "me down properly\n"
                  "Good bye :) <3")
            game.stop()
            break
