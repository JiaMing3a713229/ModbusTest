from pymodbus.client.sync import ModbusTcpClient
import time


host = '127.0.0.1'
port = 502
#modbus connection to 1st device
try:
    client1 = ModbusTcpClient(host,port)
    connection = client1.connect()
    print ('connection to  '+host)
    #request1 = client1.write_register(0x01,97,unit=0x01)
    #requeset1=client1.read_coils(0x02,64,unit=0x01)
    #print(requeset1.bits[0])
    request1 = client1.read_holding_registers(0x01,64,unit=0x01)
    result1=request1.registers
    print(result1)
    print(result1[0])



except:
    print ("Modbus connectie error")

#modbus_new_tcp("10.228.24.42", 502);

#read registers of 1st device
#close = client1.close()





