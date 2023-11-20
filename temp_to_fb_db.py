import serial
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
 
 
ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM4"
ser.open()
 
 
cred = credentials.Certificate("C:/Users/k_tur/OneDrive/Documents/prokectPrep1/Test/lccs-test-bfbb9-firebase-adminsdk-x7grr-c87af7adbe.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://lccs-test-bfbb9-default-rtdb.europe-west1.firebasedatabase.app/'})
 
ref = db.reference()
ref.update({'temperature_log':''})
ref = db.reference().child('temperature_log')
source = input("Please input the source of this data: ")

while True:
    mb_temperature = str(ser.readline().decode('utf-8'))
    print(len(mb_temperature))
    mb_temperature = mb_temperature.replace(" ","")
    mb_temperature = mb_temperature.replace("\r\n","")
    print("Len of temp is: ", len(mb_temperature))
    print(mb_temperature)
    if mb_temperature.isdigit():
        ref.update({str(int(time.time())):{'Temperature':mb_temperature, 'Location':source}})
    else:
        print("Check data source")