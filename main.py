from pymodbus.client.sync import ModbusTcpClient
import time
from enum import Enum

host = '127.0.0.1'
port = 502
class pointAddress(Enum):
    X = 0x1010
    Y = 0x1012
    Z = 0x1014
    RX = 0x1016
    RY = 0x1018
    RZ = 0x101A
    UF = 0x101C
    POS = 0x101D
    COORD = 0x101E
    TF = 0x101F
    JRC = 0x1020

def run_sync_client():

#modbus connection to 1st device
    try:
        client1 = ModbusTcpClient(host,port)
        connection = client1.connect()
        print ('connection to  '+host)



        client1.write_register(0x0000, 0x0101,unit=0x01)
        client1.write_register(0x0001, 0x0101, unit=0x01)
        client1.write_register(0x0002, 0x0101, unit=0x01)
        client1.write_register(0x0006, 0x0101, unit=0x01)
        client1.write_register(0x0007, 0x0101, unit=0x01)

        rc=client1.read_holding_registers(0x0000,16,unit=0x01)
        result1=rc.registers
        print(result1)



    except:
        print ("Modbus connectie error")

#modbus_new_tcp("10.228.24.42", 502);

#read registers of 1st device
#close = client1.close()
if __name__ == "__main__":
    run_sync_client()




