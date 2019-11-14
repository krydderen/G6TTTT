# Importing packages
from modbus_communication import ModbusClient
import time

# Dictionary holding Modbus addresses
addresses = {
    '0': 140,
    '1': 141,
    '2': 142,
    'kkk': 148
}


# Main loop
if __name__ == '__main__':
    # Creating objects
    client = ModbusClient()
    print("Client connecting...")
    while client.isConnected():
        print("Client connected.")
        cmd = input("ENTER CMD\n")

        if str(cmd) == "EXIT":
            print("Shutting down...")
            break

        client.sendInt(value=(int(cmd)), address=addresses['1'])
        response = client.readInt(address=addresses['1'], size=1)
        print(response)

        """time.sleep(1)
        # Resetting to 0
        client.sendInt(value=0, address=addresses['0'])
        response = client.readInt(address=addresses['0'], size=1)
        print(response)"""

    client.close()