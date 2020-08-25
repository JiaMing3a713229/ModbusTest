from enum import Enum
from pymodbus.client.sync import ModbusTcpClient as ModbusClient

import sys
LOOP=1
SERVER_ID=17
ADDRESS_START=0
ADDRESS_END=99

class pointAdress(Enum):
    X = 0x1010,
    Y = 0x1012,
    Z = 0x1014,
    RX = 0x1016,
    RY = 0x1018,
    RZ = 0x101A,
    UF = 0x101C,
    POS = 0x101D,
    COORD = 0x101E,
    TF = 0x101F,
    JRC = 0x1020,


if __name__ == '__main__':
    rc=0
    nb_fail=0
    nb_loop=0
    addr=0
    nb=0
    tab_rq_bits=[]
    tab_rp_bits=[]
    tab_rq_registers=[]
    tab_rw_rq_registers=[]
    tab_rp_registers=[]
#TCP
    print("Connect to VRC\n")
    print("IP = 127.0.0.1\n")
    print("Port = 502\n")

    """ctx = modbus_new_tcp("172.29.152.4", 502);"""
    ctx = ModbusClient('192.168.27.44', 502)

    """ctx = modbus_new_tcp("127.0.0.1", 502);"""
    if ctx.connect()==False:
        sys.stderr("Connection failed: %s\n")
        ctx.close()

    """Allocate and initialize the different memory spaces """
    nb = ADDRESS_END - ADDRESS_START;



    print(pointAdress.X)
