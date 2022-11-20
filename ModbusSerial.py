
from urllib.parse import urlencode              #importing urlencode from urllib library
from urllib.request import Request, urlopen     #similarly importing other functionalities
                                                #these will help in posting data to webpage
from struct import *

from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
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

    #------------- Get voltage ---------------
    address = 0
    count   = 4
    result  = client.read_input_registers(address, count,  unit=1)
    volt = format(BinaryPayloadDecoder.fromRegisters(result.registers, Endian.Big, Endian.Big).decode_32bit_float(),'0.1f')
    print(volt)

    #------------- Get Current ---------------
    address = 6
    count   = 4
    result  = client.read_input_registers(address, count,  unit=1)
    current = format(BinaryPayloadDecoder.fromRegisters(result.registers, Endian.Big, Endian.Big).decode_32bit_float(),'0.2f')
    print(current)

    #------------- Get voltage ---------------
    address = 70
    count   = 4
    result  = client.read_input_registers(address, count,  unit=1)
    Frequency = format(BinaryPayloadDecoder.fromRegisters(result.registers, Endian.Big, Endian.Big).decode_32bit_float(),'0.1f')
    print(Frequency)
    #------------- Get Energy ---------------
    address = 72
    count   = 4
    result  = client.read_input_registers(address, count,  unit=1)
    Energy = format(BinaryPayloadDecoder.fromRegisters(result.registers, Endian.Big, Endian.Big).decode_32bit_float(),'0.1f')
    print(Energy)





    """


    #volt = client.read_holding_registers(address=1, count=2, unit=1)
    volt = client.read_input_registers(address=0 , count=4, unit=1)        

    rec_date_time = current_time()

    volt = random.randint(219,230)
    current = random.randint(50,1200)
    power = random.randint(1200,1999)
    energy = random.randint(4000,8000)
    frequency = round(random.uniform(49.00, 50.99),2)
    

    print("\nVoltage :" ,volt)
    print("Current :" ,current)
    print("Energy :" ,energy)
    print("Frequency :" ,frequency)
    print("Date_time :" ,rec_date_time)
   
    a = volt.registers[0] << 24 & volt.registers[1] << 16 & volt.registers[2] << 8 & volt.registers[3]
    
    print(a)

    print("Voltage 0 :" ,volt.registers[0])
    print("Voltage 1 :" ,volt.registers[1])
    print("Voltage 2 :" ,volt.registers[2])
    print("Voltage 3 :" ,volt.registers[3])



    print( hex(volt.registers[0]))
    print( hex(volt.registers[1]))

    mypack = pack('>HH',volt.registers[0],volt.registers[1])
    print (mypack)
    f = unpack('f', mypack)[0]
    print (f)

    # Posting data to database server
    url = 'https://xn--12c5cbudkbb0yh.com/meter/updatescript.php'
    #post_fields = {'mcu_id' : '777888' , 'volt' : volt , 'current' : current , 'power' : power, 'energy' : energy , 'frequency' : frequency , 'rec_date_time' : rec_date_time}   #Set POST fields here and their values
    post_fields = {'mcu_id' : '777888' , 'volt' : volt , 'rec_date_time' : rec_date_time}   #Set POST fields here and their values
    
    #xpost_fields = {'mcu_id' : mcu_id }   #Set POST fields here and their values

    request = Request(url, urlencode(post_fields).encode())     # Posting data to webpage 

    try:
        json = urlopen(request).read().decode()
    except:
        print('Can\'t connect to server!') 
    else:   
        print(json)
 """
    time.sleep(1)
       
