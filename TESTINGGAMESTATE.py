from modbus_communication import ModbusClient

client = ModbusClient(ip='158.38.140.249')

client.wait_feedback()