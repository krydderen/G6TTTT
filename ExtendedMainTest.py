# Importing packages
from modbus_communication import ModbusClient
import time
import cv2
import numpy as np
from gamechecker import GameChecker
import traceback

# Dictionary holding Modbus addresses
addresses = {
    '0': 140,
    '1': 141,
    '2': 142,
    'kkk': 148,
    'test': 149,
    'exampleRead': 000,
    'exampleSend': 000
}

# Dictionary holding Modbus IP addresses
ipaddresses = {
    'UR3.1': '158.38.140.249',
    'PLS': '158.38.140.63'
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

        try:

            """This is used for testing when I cannot use our
            robot for testing when I am away from the LAB"""
            string = str(input("enter below\n"))
            print(string)

            """Just a test lmao"""
            if string == "lmao":
                print("epiclmao")

            if string == "test123":
                while 1:
                    test = client.readInt(address=31000, size=1)
                    print(test)
                    if str(test) == "[1]":
                        print("HEI KEVIN")
                        break

            if string == "spam":
                while 1:
                    client.sendInt(address=32000, value=1)


            """WORKS"""
            if string == "pls":
                while 1:
                    address = 32002
                    num = input("Enter number\n")

                    if num == "stop":
                        print("exiting...")
                        break

                    print("sending " + str(num))

                    client.sendInt(address=address, value=int(num))


            if string == "send":
                add = input("address")
                while 1:
                    number = input("type number\n")

                    if number == "stop":
                        break
                    client.sendInt(address=int(add), value=int(number))


            if string == "test":

                while 1:
                    time.sleep(1)
                    testread = client.readInt(address=142, size=1)
                    print(testread)

                    if str(testread) == "[0]":
                        number = input("type number\n")
                        if number == "stop":
                            break
                        try:
                            client.sendInt(address=143, value=int(number))
                        except Exception as e:
                            print("Error: " + str(e))
                            print(traceback.format_exc())
                    else:
                        print("Machine not idle...")


            """ TODO - change this to a statement where
            if the PLS or the UR3 robot asks for the game status, 
            send either that someone has won or a tie is found. 
            If else, send out a signal that implies that the game can'
            continue untill further notice."""
            if string == "q":
                state = game.cleanBoard()
                print(str(state))


            if string == "iyg":
                print()
                """get and check the current gamestate up towards
                the winning conditions. This t"""
            if string == "stop":
                print("Closing...\nThank you for shutting "
                      "me down properly\n"
                      "Good bye :) <3")
                #game.stop()

                break
        except Exception as e:
            print("Error: " + str(e))
            print(traceback.format_exc())

