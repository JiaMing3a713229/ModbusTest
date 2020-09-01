from pymodbus.client.sync import ModbusTcpClient
import time
import random

host = '127.0.0.1'
port = 502
def run_sync_client():

#modbus connection to 1st device
    try:
        client1 = ModbusTcpClient(host,port)
        connection = client1.connect()
        print ('connection to  '+host)
        start_adress=0x00
        for i in range(99):
            print(int(start_adress))
            data1 = random.randint(1, 100)
            if start_adress>0x00:
                client1.write_coil((start_adress-0x01),0,unit=0x01)
                client1.write_coil(start_adress,'true',unit=0x01)
                client1.write_register(start_adress,data1,unit=0x01)
                time.sleep(0.2)
                start_adress+=1

            else:
                client1.write_coil(start_adress, 'true', unit=0x01)
                client1.write_register(start_adress, data1, unit=0x01)
                time.sleep(0.2)
                start_adress += 1

        #request1 = client1.write_register(0x01,97,unit=0x01)
        #requeset1=client1.read_coils(0x02,64,unit=0x01)
        #print(requeset1.bits[0])
        #rq=client1.write_register(0x01,96,unit=0x01)
        #print(rq.function_code)
        #request1 = client1.read_holding_registers(0x01,64,unit=0x01)
        #esult1=request1.registers
        #print(result1)
        #print(result1[0])



    except:
        print ("Modbus connectie error")

#modbus_new_tcp("10.228.24.42", 502);

#read registers of 1st device
#close = client1.close()
if __name__ == "__main__":
    run_sync_client()




