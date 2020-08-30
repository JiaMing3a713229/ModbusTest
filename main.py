from pymodbus.client.sync import ModbusTcpClient
import time


host = '127.0.0.1'
port = 502
#modbus connection to 1st device
try:
    client1 = ModbusTcpClient(host,port)
    connection = client1.connect()
    print ('connection to  '+host)
    request1 = client1.read_coils(0x00,1,unit=0x01)
    print(request1)

except:
    print ("Modbus connectie error")

#modbus_new_tcp("10.228.24.42", 502);

#read registers of 1st device
#close = client1.close()





