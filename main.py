# Importing packages
from modbus_communication import ModbusClient

# Dictionary holding Modbus addresses
addresses = {
    '0': 140,
    '1': 141,
    '2': 142
}


# Main loop
if __name__ == '__main__':
    # Creating objects
    client = ModbusClient()
    print("Client connecting...")
    while client.isConnected():
        print("Client connected.")
        client.sendInt(value=1, address=addresses['0'])
        response = client.readInt(address=addresses['0'], size=1)
        print(response)
        break
    client.close()