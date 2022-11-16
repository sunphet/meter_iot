from pymodbus.client.sync import ModbusTcpClient
from datetime import datetime, time
import random
import time

host = '10.0.2.17'
port = 502
client = ModbusTcpClient(host, port)
while True:
    client.connect()
    data = random.randint(25,35)
    
    wr = client.write_registers(1000,data,unit=1)
    time.sleep(5)
