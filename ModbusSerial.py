
from urllib.parse import urlencode              #importing urlencode from urllib library
from urllib.request import Request, urlopen     #similarly importing other functionalities
                                                #these will help in posting data to webpage



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
    volt = random.randint(219,230)
    current = random.randint(50,1200)
    power = random.randint(1200,1999)
    energy = random.randint(4000,8000)
    frequency = round(random.uniform(49.00, 50.99),2)
    rec_date_time = current_time()

    print("\nVoltage :" ,volt)
    print("Current :" ,current)
    print("Energy :" ,energy)
    print("Frequency :" ,frequency)
    print("Date_time :" ,rec_date_time)
    
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
    
