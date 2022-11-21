
from urllib.parse import urlencode              #importing urlencode from urllib library
from urllib.request import Request, urlopen     #similarly importing other functionalities
                                                #these will help in posting data to webpage
from struct import *

from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
#from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.compat import iteritems


from pymodbus.client.sync import ModbusSerialClient as ModbusClient 
from datetime import datetime, time

#This section is not mandatory for connection
from pymodbus.constants import Defaults


import time                                     #importing time library of Python3
import random 


Defaults.RetryOnEmpty = True
Defaults.Timeout = 5
Defaults.Retries = 5


#mcu_id , 	volt , 	current , 	power, energy, frequency , date_time ,	rec_date_time	

mcu_id =  '777888'

def current_time():
    now = datetime.now().isoformat()
    return now
  
client = ModbusClient(method='rtu', port='/dev/ttyUSB0', timeout=20, stopbits=1,bytesize=8, parity='N', baudrate= 9600)





try:
    client.connect()
    print("Serial port connected.")
except:
    print("Serial port connection error!")


while True:
    print('-----------------------------------------')
    print('MCU ID : ', mcu_id)

    #------------- Get voltage ---------------
    address = 0
    count   = 4
    result  = client.read_input_registers(address, count,  unit=1)
    volt = format(BinaryPayloadDecoder.fromRegisters(result.registers, Endian.Big, Endian.Big).decode_32bit_float(),'0.1f')
    print('Volt : ',volt, ' V.')

    #------------- Get Current ---------------
    address = 6
    count   = 4
    result  = client.read_input_registers(address, count,  unit=1)
    current = format(BinaryPayloadDecoder.fromRegisters(result.registers, Endian.Big, Endian.Big).decode_32bit_float(),'0.2f')
    print('Current : ',current, ' A.')

    #------------- Get voltage ---------------
    address = 70
    count   = 4
    result  = client.read_input_registers(address, count,  unit=1)
    frequency = format(BinaryPayloadDecoder.fromRegisters(result.registers, Endian.Big, Endian.Big).decode_32bit_float(),'0.1f')
    print('Frequency : ',frequency, ' Hz.')
    
    #------------- Get power ---------------
    address = 12
    count   = 4
    result  = client.read_input_registers(address, count,  unit=1)
    power = format(BinaryPayloadDecoder.fromRegisters(result.registers, Endian.Big, Endian.Big).decode_32bit_float(),'0.1f')
    print('Power : ',power, ' W.')

    #------------- Get Energy ---------------
    address = 72
    count   = 4
    result  = client.read_input_registers(address, count,  unit=1)
    energy = format(BinaryPayloadDecoder.fromRegisters(result.registers, Endian.Big, Endian.Big).decode_32bit_float(),'0.1f')
    print('Energy : ',energy, ' kWh.')
    
    #------------- Date time ---------------
    rec_date_time = current_time()
    print('Time stamp : ',rec_date_time)

 
    # Posting data to database server
    url = 'https://xn--12c5cbudkbb0yh.com/meter/updatescript.php'
    post_fields = {'mcu_id' : '777888' , 'volt' : volt , 'current' : current , 'power' : power, 'energy' : energy , 'frequency' : frequency , 'rec_date_time' : rec_date_time}   #Set POST fields here and their values
     
    #xpost_fields = {'mcu_id' : mcu_id }   #Set POST fields here and their values

    request = Request(url, urlencode(post_fields).encode())     # Posting data to webpage 

    try:
        json = urlopen(request).read().decode()
    except:
        print('Can\'t connect to server!') 
    else:   
        print(json)

    time.sleep(60)
       
