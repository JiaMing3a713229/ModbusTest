from pymodbus.client.sync import ModbusTcpClient
import time
from enum import Enum

host = '127.0.0.1'
port = 502
nb_loop = nb_fail = 0
Slave_ID = 2

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

        #read CartPos(um), X~RZ
        addr =0xF0
        rc=client1.read_holding_registers(addr,12,unit=0x02)
        #write RL ID
        addw =0x220
        write_value = 1
        rc=client1.write_register(addw,write_value,unit=0x02)

        #read current RL ID
        addr = 0x210
        rc=client1.read_holding_registers(addr,12,unit=0x02)

        time.sleep(2)



        #write_relief_point_data
        valueX = 595608
        valueY = 0
        valueZ = 581910
        valueRX = -180000
        valueRY = 1367
        valueRZ = 0
        Posture = 0x0000

        arrayX = [0x00, 0x00]
        arrayX[0] = valueX & 0x00FFFF
        arrayX[1] = (valueX >> 16) & 0x0000ffff

        arrayY = [0x00, 0x00]
        arrayY[0] = valueY & 0x00FFFF
        arrayY[1] = (valueY >> 16) & 0x0000ffff

        arrayZ = [0x00, 0x00]
        arrayZ[0] = valueZ & 0x00FFFF
        arrayZ[1] = (valueZ >> 16) & 0x0000ffff

        arrayRX = [0x00, 0x00]
        arrayRX[0] = valueRX & 0x00FFFF
        arrayRX[1] = (valueRX >> 16) & 0x0000ffff

        arrayRY = [0x00, 0x00]
        arrayRY[0] = valueRY & 0x00FFFF
        arrayRY[1] = (valueRY >> 16) & 0x0000ffff

        arrayRZ = [0x00, 0x00]
        arrayRZ[0] = valueRZ & 0x00FFFF
        arrayRZ[1] = (valueRZ >> 16) & 0x0000ffff
        # 三個欄位為：(起始Address, 要讀入的AI數量, Modbus slave ID)

        #client1.write_register(0x0000, 0x0101, unit=0x02)

        #rc = client1.write_register(0x220,1,unit=0x02)
        #rc1 = client1.write_register(0x220,1,unit=0x02)
        for i in range(5):
            rc = client1.write_registers(pointAddress.X.value,arrayX,unit=0x02)
            rc = client1.write_registers(pointAddress.Y.value, arrayY, unit=0x02)
            rc = client1.write_registers(pointAddress.Z.value, arrayZ, unit=0x02)
            rc = client1.write_registers(pointAddress.RX.value, arrayRX, unit=0x02)
            rc = client1.write_registers(pointAddress.RY.value, arrayRY, unit=0x02)
            rc = client1.write_registers(pointAddress.RZ.value, arrayRZ, unit=0x02)
            rc = client1.write_register(pointAddress.UF.value, 0, unit=0x02)
            rc = client1.write_register(pointAddress.POS.value, Posture, unit=0x02)
            rc = client1.write_register(pointAddress.COORD.value, 0, unit=0x02)
            rc = client1.write_register(pointAddress.TF.value, 0, unit=0x02)

        #write Open&Run
        addw = 0x228
        write_value = 6
        rc=client1.write_register(addw,write_value,unit=0x02)


        time.sleep(5)

        #read RLRunCount, CycleTime, CollisionState

        addr = 0x1000
        rc=client1.read_holding_registers(addr,6,unit=0x02)

        #rc = client1.read_holding_registers(02,unit=0x02)
        #print(rc.registers)
        #client1.write_register(0x0002, 0x0101, unit=0x02)
        #client1.write_register(0x0006, 0x0101, unit=0x02)
        #client1.write_register(0x0007, 0x0101, unit=0x02)
        #rl = client1.read_holding_registers(0x0000,1,unit=0x01)


        #result1=rl.registers
        #print(result1)



    except:
        print ("Modbus connectie error")

#modbus_new_tcp("10.228.24.42", 502);

#read registers of 1st device
#close = client1.close()
def write_relief_point_data():
    #write relief point data

    valueX =595608
    valueY = 0
    valueZ = 581910
    valueRX = -180000
    valueRY = 1367
    valueRZ = 0
    Posture = 0x0000


    arrayX=[0x00,0x00]
    arrayX[0]= valueX & 0x00FFFF
    arrayX[1]=(valueX >> 16) & 0x0000ffff

    arrayY=[0x00,0x00]
    arrayY[0]= valueY & 0x00FFFF
    arrayY[1]=(valueY >> 16) & 0x0000ffff

    arrayZ=[0x00,0x00]
    arrayZ[0] = valueZ & 0x00FFFF
    arrayZ[1] = (valueZ >> 16) & 0x0000ffff

    arrayRX = [0x00, 0x00]
    arrayRX[0] = valueRX & 0x00FFFF
    arrayRX[1] = (valueRX >> 16) & 0x0000ffff

    arrayRY= [0x00, 0x00]
    arrayRY[0] = valueRY & 0x00FFFF
    arrayRY[1] = (valueRY >> 16) & 0x0000ffff

    arrayRZ = [0x00, 0x00]
    arrayRZ[0] = valueRZ & 0x00FFFF
    arrayRZ[1] = (valueRZ >> 16) & 0x0000ffff


if __name__ == "__main__":
    run_sync_client()



