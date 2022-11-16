from pymodbus.client.sync import ModbusTcpClient
from datetime import datetime, time
import random
import json
import time

def current_time():
    now = datetime.now().isoformat()
    return now

host = '10.0.2.17'
port = 502
client = ModbusTcpClient(host, port)
while True:
    client.connect()

    rr = client.read_holding_registers(1000,1,unit=1)

    data = {
        "datetime" : current_time(),
        "data" : rr.registers
    }

    print(json.dumps(data))
    time.sleep(5)
