from modbus_communication import ModbusClient

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

state = [1, 2, 1, 2, 1, 2, 1, 2, 1]

if __name__ == '__main__':
    # SPAM ALEXANDER
    alex = ModbusClient(ip='158.38.140.63')

    while alex.isConnected():

        test = alex.readInt(address=addresses['listen'], size=1)
        print(str(test), )

        if str(test) == "[1]":
            # notify that we send shit
            alex.sendInt(address=addresses['alex'], value=1)
            loop = 100
            for i in range(loop):
                print('{:s}\r'.format(''), end='', flush=True)
                print('Loading index: {:d}/'+str(loop)+'.format(i + 1), end='')
                print("looped " + str(i) + " time(s)")
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
