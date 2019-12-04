from modbus_communication import ModbusClient
import traceback
import time

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

game_state = ["-", "-", "O", "-", "X", "-", "-", "-", "-"]
""""     1  2  3  4  5  6  7  8  9"""
state = [0, 0, 0, 0, 0, 0, 0, 0, 0]

if __name__ == '__main__':
    # SPAM ALEXANDER
    alex = ModbusClient(ip='158.38.140.63')

    while alex.isConnected():
        try:
            test = alex.readInt(address=addresses['listen'], size=1)
            #print(str(test))

            if str(test) == "[0]":
                print("Alexander won't listen, you sack of wet turd..:(  ('[0]')")

            if str(test) == "[1]":
                time.sleep(1)
                print("Alexander wants to know your location.")
                # notify that we send shit
                alex.sendInt(address=addresses['alex'], value=1)
                loop = 1
                for i in range(loop):

                    #print("looped " + str(i) + " times...")

                    alex.sendInt(address=addresses['1'], value=state[0])
                    alex.sendInt(address=addresses['2'], value=state[1])
                    alex.sendInt(address=addresses['3'], value=state[2])
                    alex.sendInt(address=addresses['4'], value=state[3])
                    alex.sendInt(address=addresses['5'], value=state[4])
                    alex.sendInt(address=addresses['6'], value=state[5])
                    alex.sendInt(address=addresses['7'], value=state[6])
                    alex.sendInt(address=addresses['8'], value=state[7])
                    alex.sendInt(address=addresses['9'], value=state[8])

                # we done sending shit
                alex.sendInt(address=addresses['alex'], value=0)

                print("Alexander is not interesed in your wares no more. Disconnect.")
                time.sleep(3)
                break
            if str(test) == "[11]":
                print("We in boiss")
                # notify that we send shit
                alex.sendInt(address=addresses['alex'], value=1)
                loop = 1
                for i in range(loop):
                    print("looped " + str(i) + " times...")

                    if game_state[0] == "X":
                        alex.sendInt(address=['1'], value=1)
                    elif game_state[0] == "0":
                        alex.sendInt(address=['1'], value=2)
                    elif game_state[0] == "-":
                        alex.sendInt(address=['1'], value=0)

                    if game_state[0] == "X":
                        alex.sendInt(address=['2'], value=1)
                    elif game_state[0] == "0":
                        alex.sendInt(address=['2'], value=2)
                    elif game_state[0] == "-":
                        alex.sendInt(address=['2'], value=0)

                    if game_state[0] == "X":
                        alex.sendInt(address=['3'], value=1)
                    elif game_state[0] == "0":
                        alex.sendInt(address=['3'], value=2)
                    elif game_state[0] == "-":
                        alex.sendInt(address=['3'], value=0)

                    if game_state[0] == "X":
                        alex.sendInt(address=['4'], value=1)
                    elif game_state[0] == "0":
                        alex.sendInt(address=['4'], value=2)
                    elif game_state[0] == "-":
                        alex.sendInt(address=['4'], value=0)

                    if game_state[0] == "X":
                        alex.sendInt(address=['5'], value=1)
                    elif game_state[0] == "0":
                        alex.sendInt(address=['5'], value=2)
                    elif game_state[0] == "-":
                        alex.sendInt(address=['5'], value=0)

                    if game_state[0] == "X":
                        alex.sendInt(address=['6'], value=1)
                    elif game_state[0] == "0":
                        alex.sendInt(address=['6'], value=2)
                    elif game_state[0] == "-":
                        alex.sendInt(address=['6'], value=0)

                    if game_state[0] == "X":
                        alex.sendInt(address=['7'], value=1)
                    elif game_state[0] == "0":
                        alex.sendInt(address=['7'], value=2)
                    elif game_state[0] == "-":
                        alex.sendInt(address=['7'], value=0)

                    if game_state[0] == "X":
                        alex.sendInt(address=['8'], value=1)
                    elif game_state[0] == "0":
                        alex.sendInt(address=['8'], value=2)
                    elif game_state[0] == "-":
                        alex.sendInt(address=['8'], value=0)

                    if game_state[0] == "X":
                        alex.sendInt(address=['9'], value=1)
                    elif game_state[0] == "0":
                        alex.sendInt(address=['9'], value=2)
                    elif game_state[0] == "-":
                        alex.sendInt(address=['9'], value=0)


                # we done sending shit
                alex.sendInt(address=addresses['alex'], value=0)

                print("Done sending shit")


        except Exception as e:
            print("Error: " + str(e))
            print(traceback.format_exc())