# Importing packages
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client.sync import ModbusTcpClient
import time


class ModbusClient(object):
    """Establishes a secure connection with the
    Modbus slave. Will be able to read and write
    to all of the available I/O."""
    #158.38.140.249
    def __init__(self, ip):
        self.ip = ip
        self.client = ModbusTcpClient(self.ip)
        self.connection = self.client.connect()

    def isConnected(self):
        """Returns the connection status.
        Return: True if connected, False if not."""
        return self.connection

    def sendInt(self, value, address):
        """Send a 32 bit value to the first modbus unit.
        Parameters: value and address where the value will be
        stored in.
        Return: Result if it was successful or not."""
        builder = BinaryPayloadBuilder(byteorder=Endian.Big)
        builder.add_16bit_int(value)
        payload = builder.build()
        result = self.client.write_registers(address, payload, skip_encode=True, unit=1)
        print(result)

        """ TESTING """
        if str(result).startswith("Modbus Error:"):
            print("Sending again because of error...")
            result = self.client.write_registers(address, payload, skip_encode=True, unit=1)

        return result

    def sendFloat(self, value, address):
        """Send a 32 bit value to the first modbus unit.
        Parameters: value and address where the value will be
        stored in.
        Return: Result if it was successful or not."""
        builder = BinaryPayloadBuilder(byteorder=Endian.Big)
        builder.add_32bit_float(value)
        payload = builder.build()
        result = self.client.write_registers(address, payload, skip_encode=True, unit=1)
        return result

    def readInt(self, address, size=20):
        """Reads the number of addresses that the size contains.
        The readings start from the given address.
        Return: An array of read values"""
        response = self.client.read_holding_registers(address, size, unit=1)
        return response.registers

    def readFloat(self, address=12301, size=2):
        """Reads two bytes from the given start address.
        Returns the decoded float value"""
        response = self.client.read_holding_registers(address, size, unit=1)
        decoder = BinaryPayloadDecoder.fromRegisters(response.registers,
                                                     byteorder=Endian.Big,
                                                     wordorder=Endian.Little)
        value = decoder.decode_32bit_float()
        return value

    def close(self):
        """Closes the connection with the port.
        Return: True when the connection is closed."""
        self.client.close()
        return True

    def wait_feedback(self, address=142):
        """ Takk Andreas for kodesnutten :)))))"""
        done = False
        while not done:
            response = self.client.read_holding_registers(address, size=1, unit=1)

            #print(response.registers)
            if str(response.registers) == "[0]":
                done = True

    def wait_feedback_drawboard(self, address=140):
        """ Takk Andreas for kodesnutten :)))))"""
        done = False
        while not done:
            response = self.client.read_holding_registers(address, size=1, unit=1)

            #print(response.registers)
            if str(response.registers) == "[0]":
                done = True

    def wait_feedback_pls(self, address, wantedAnswer):
        """ Takk Andreas for kodesnutten :)))))"""
        done = False
        while not done:
            response = self.client.read_holding_registers(address, size=1, unit=1)

            print(response.registers)
            if str(response.registers) == str(wantedAnswer):
                done = True





# Simple example of usage
if __name__ == '__main__':
    client = ModbusClient()

    while client.isConnected():
        client.readFloat()
