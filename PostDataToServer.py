from datetime import datetime, time

import time                                     #importing time library of Python3
import requests
import json
import random 

mcu_id =  '777888'
headers = {'content-type': 'application/json'}

def current_time():
    now = datetime.now().isoformat()
    return now


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
    url = 'http://xn--12c5cbudkbb0yh.com/meter/updatescript.php'
    payload = {'mcu_id' : '777888' , 'volt' : volt , 'current' : current , 'power' : power, 'energy' : energy , 'frequency' : frequency , 'rec_date_time' : rec_date_time}   #Set POST fields here and their values
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(payload)
    print ("\n" ,r.json)

    time.sleep(15)
    