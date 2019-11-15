# Importing packages
from modbus_communication import ModbusClient
import time
import cv2
import numpy as np

# Dictionary holding Modbus addresses
addresses = {
    '0': 140,
    '1': 141,
    '2': 142,
    'kkk': 148
}

# Reset the gamestate for each cycle
game_state = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

# Create a list of all possible win combinations
win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [6, 3, 0], [7, 4, 1], [8, 5, 2], [6, 4, 2], [8, 4, 0]]

# Fetch the video captured by the camera
cap = cv2.VideoCapture(0)

# Main loop
if __name__ == '__main__':
    number = 1

    print("client created")
    while number:
        print("Client connected.")
        cmd = input("ENTER CMD\n")

        if str(cmd) == "EXIT":
            print("Shutting down...")
            number=0

        if str(cmd) == "cam":
            while True:
                # Read the video captured from the camera and set a Region Of Interest
                ret, frame = cap.read()

                # Shows the picture captured and used for calculating winners, tie or scan again
                cv2.imshow("frame", frame)

                key = cv2.waitKey(100)
                if key == 27:
                    break
             # When ESC is pressed, close the program and destroy all windows.
            cap.release()
            cv2.destroyAllWindows()


