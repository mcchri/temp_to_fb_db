import serial
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
 
 
def something_changed(response):
    print(response.event_type)
    print(response.data)
 
cred = credentials.Certificate("C:/Users/k_tur/OneDrive/Documents/prokectPrep1/Test/lccs-test-bfbb9-firebase-adminsdk-x7grr-c87af7adbe.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://lccs-test-bfbb9-default-rtdb.europe-west1.firebasedatabase.app/'})
 
ref = db.reference().child('temperature_log')
my_ref = ref.listen(something_changed)

