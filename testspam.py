from modbus_communication import ModbusClient
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

state = [2, 2, 2, 1, 1, 1, 2, 2, 2]

if __name__ == '__main__':
    # SPAM ALEXANDER
    alex = ModbusClient(ip='158.38.140.63')

    while alex.isConnected():
        try:
            test = alex.readInt(address=addresses['listen'], size=1)
            print(str(test))

            if str(test) == "[1]":
                print("We in boiss")
                # notify that we send shit
                alex.sendInt(address=addresses['alex'], value=1)
                loop = 1
                for i in range(loop):
                    print("looped " + str(i) + " times...")

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

                print("Done sending shit")

        except Exception as e:
            print("Error: " + str(e))
            print(traceback.format_exc())