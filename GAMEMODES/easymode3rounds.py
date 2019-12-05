"""
Code for easy gamemode in Tic
Tac Toe where two UR3 robots go
against eachother... like 2 year olds..
and have to win atleast 2 times before they stop.

Code by: Kevin Moen Storvik
Version: 1.0
"""
from modbus_communication import ModbusClient
from gamechecker import GameChecker
import random
import cv2
import time

# Idk lmao
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Numbers of what the robots are allowed to pick.
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# Main loop
if __name__ == '__main__':

    # Creates the objects, here our two robots and the video capture
    UR31 = ModbusClient(ip='158.38.140.249')
    UR32 = ModbusClient(ip='158.38.140.250')
    cap = cv2.VideoCapture(1)

    # Creates an instance of GameChecker where we input our capture and
    # want to watch the feed from the cams.
    game = GameChecker(capture=cap, watch=True)

    # Puts both the robots in a list so we can switch between players later.
    players = [UR31, UR32]

    playerstest = ["player1", "player2"]

    # Current win standings
    currentWins = [0, 0]

    # Sets how many wins one must have to end the game
    wins = 3

    # Chooses a random player to start the game
    startplayer = random.randint(0, 1)  # Decides who starts
    # The player who starts gets his turn taken first.
    turn = startplayer

    while UR31.isConnected() and UR32.isConnected():
        while 1:
            # Resets the current fields our robots are allowed to pick.
            numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

            # Checks if the board is not clean. If clean, skip this if-sentence.
            if not game.cleanBoard():
                # Sends an Integer to the UR2 robot, which takes care of wiping the board.
                # First, we set the value to 0 to ensure that our wiping will commence.
                UR32.sendInt(address=143, value=0)
                # Then we sleep for a second. This is necessary because we send and read too quickly
                time.sleep(1)
                # Send out our buttwiping signal
                UR32.sendInt(address=143, value=69)
                # Sleep again because the code is too fast...
                time.sleep(1)
                # Now we wait for feedback. This means that we wait until the robot sets an addresses value to 0.
                UR32.wait_feedback()
            else:
                # We get.cleanBoard returned TRUE, and we do not need to clean the board.
                print("Machine idle and board clean...")

            # Making sure our robot is 'reset', same as what we did in game.cleanBoard.
            UR31.sendInt(address=141, value=0)


            print("Drawing board.")
            # Value 20 is a special command for the easy mode. It
            UR31.sendInt(address=141, value=20)
            # Sleep a second because we are too fast.
            time.sleep(1)
            # wait_feedback_drawboard() is a special feedback signal that waits for
            # the first robot to become idle
            print("Waiting for board to become drawn...\n")
            time.sleep(2)
            UR31.wait_feedback_drawboard()

            turnstaken = 0

            for x in range(len(numbers)):
                time.sleep(1)
                winnerFound = game.didSomeoneWin()

                if winnerFound:
                    print("Winner found.")
                    break

                turnstaken += 1
                player = players[turn]
                turn = (turn + 1) % len(players)

                selection = random.randint(0, len(numbers) - 1)
                goner = numbers.pop(selection)
                print(goner)

                print("Player " + str(turn + 1) + " picks " + goner)

                player.sendInt(address=143, value=int(goner))
                print("Waiting for " + str(turn + 1) + " to become idle...\n" )
                time.sleep(1)
                player.wait_feedback()

            print("Turns taken " + str(turnstaken))

            wincombo = game.getWinCombo()

            print(wincombo)

            """ TODO - FIX THIS"""
            if wincombo == 9:
                wincombo = 0

            UR32.sendInt(address=150, value=wincombo)
            time.sleep(1)
            UR32.wait_feedback_drawboard()

            currentWinner = game.getWinner()

            if currentWinner == "red":
                currentWins[0] = currentWins[0].__add__(1)
            elif currentWinner == "blue":
                currentWins[1] = currentWins[1].__add__(1)
            elif currentWinner == "none":
                print("lmao no one won so no score for anyone")

            print("#1: " + str(currentWins[0]) + "   #2: " + str(currentWins[1]))

            if currentWins[0] == wins:
                print("Player X wins.")
                break
            elif currentWins[1] == wins:
                print("Player O wins.")
                break

        break
    game.stop()
    UR31.close()
    UR32.close()
