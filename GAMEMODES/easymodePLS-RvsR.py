"""
Code for easy gamemode in Tic
Tac Toe where two UR3 robots go
against eachother... like 2 year olds..

Code by: Kevin Moen Storvik
Version: 1.1
"""
from modbus_communication import ModbusClient
from gamechecker import GameChecker
import random
import cv2
import time
import traceback

addresses = {
    '1': 32201,
    '2': 32202,
    '3': 32203,
    '4': 32204,
    '5': 32205,
    '6': 32206,
    '7': 32207,
    '8': 32208,
    '9': 32209,
    'alex': 32217,
    'listen': 201,
    'sendingchoice': 32218
}
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#numbers = [0]

drawboard = ['2', '5', '6', '10', '11']

# Main loop
if __name__ == '__main__':
    # Creating objects
    cap = cv2.VideoCapture(1)
    game = GameChecker(capture=cap, watch=False)
    while 1:

        PLS = ModbusClient(ip='158.38.140.63')

        while PLS.isConnected():
            try:
                # Listens for when we want to start the program
                start = PLS.readInt(address=207, size=1)
                start = PLS.readInt(address=207, size=1)
                print(str(start))

                while str(start) == "[1]":
                    # Turns starts at 0
                    turn = 0
                    # Give system time to respond
                    time.sleep(0)
                    # PLS.wait_feedback_pls(address=208, wantedAnswer="[]")
                    turnstaken = 0

                    clean = game.cleanBoard()

                    # If the board is not clean, send request to wash
                    if not clean:
                        print("Wash please.")
                        time.sleep(0)
                        PLS.sendInt(address=32221, value=1)

                        print("request to wash sent........")
                        time.sleep(1)

                    # If not, notify that it is clean.
                    else:
                        print("Board clean.")
                        time.sleep(0)
                        PLS.sendInt(address=32221, value=0)

                        print("warned that it is clean")
                        time.sleep(1)

                    # Checks who has their turn
                    p1 = PLS.readInt(address=125, size=1)
                    p2 = PLS.readInt(address=126, size=1)

                    # Probably a dumb if..
                    if str(p1) == "[1]" or str(p2) == "[1]":
                        # P1 has their turn
                        if str(p1) == "[1]":
                            turn = 0
                        # P2 has their turn
                        elif str(p2) == "[1]":
                            turn = 1

                    for x in range(len(numbers)):
                        # Start scan
                        PLS.wait_feedback_pls(address=201, wantedAnswer="[1]")

                        # Fetching some values
                        state = game.getGamestate12()
                        winnerFound = game.didSomeoneWin()
                        numbers = game.returnRemainingFields()

                        # Stop the game if a winner is found
                        if winnerFound:
                            print("Winner found.")
                            break

                        # For each turn, add 1
                        turnstaken += 1

                        # should swap players
                        turn = (turn + 1) % 2  # 2 players

                        if len(numbers) > 0:
                            # Get the random magic field number.
                            selection = random.randint(0, len(numbers) - 1)
                            goner = numbers.pop(selection)
                            # Debugging print
                            print("Selected number is..." + str(goner))

                        # Else we done, and we outta here
                        else:
                            print("No more fields left...")
                            PLS.sendInt(address=32218, value=0)  # Because there is no alternatives left.
                            break

                        # Send designated value to ALEXANDER
                        PLS.sendInt(address=32218, value=int(goner))
                        print("Sent designated value to ALEXANDER\n")

                        # Send board status.
                        PLS.sendInt(address=addresses['1'], value=state[0])
                        print("Sending first tile...")
                        PLS.sendInt(address=addresses['2'], value=state[1])
                        print("Sending second tile...")
                        PLS.sendInt(address=addresses['3'], value=state[2])
                        print("Sending third tile...")
                        PLS.sendInt(address=addresses['4'], value=state[3])
                        print("Sending fourth tile...")
                        PLS.sendInt(address=addresses['5'], value=state[4])
                        print("Sending fifth tile...")
                        PLS.sendInt(address=addresses['6'], value=state[5])
                        print("Sending sixth tile...")
                        PLS.sendInt(address=addresses['7'], value=state[6])
                        print("Sending seventh tile...")
                        PLS.sendInt(address=addresses['8'], value=state[7])
                        print("Sending 8th tile...")
                        PLS.sendInt(address=addresses['9'], value=state[8])
                        print("Sending 9th tile...")

                        # Warn Alexander that we are done sending the drugs

                        PLS.sendInt(address=32217, value=1)  # BOOL
                        print("Done sending...\n")
                        time.sleep(4)

                    print("Turns taken " + str(turnstaken))

                    # WHO WON
                    winner = game.getWinner()
                    if winner == "red":
                        PLS.sendInt(address=32219, value=1)
                    elif winner == "blue":
                        PLS.sendInt(address=32219, value=2)
                    elif winner == "none":
                        PLS.sendInt(address=32219, value=0)

                    # SEND WIN COMBO TO ALEXANDER HAMILTON
                    wincombo = game.getWinCombo()
                    print(wincombo)
                    PLS.sendInt(address=32220, value=wincombo)
                    time.sleep(1)
                    break

                if start == "[0]":
                    print("not ready..")
            # Whenever we get an exception, the program will not stop
            except Exception as e:
                print("Error: " + str(e))
                print(traceback.format_exc())
                break

