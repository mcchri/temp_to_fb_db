import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
# path to the private key
cred = credentials.Certificate("C:/Users/k_tur/OneDrive/Documents/cs/CS_project/lccs-test-bfbb9-firebase-adminsdk-x7grr-c87af7adbe.json")
# URL to the database
firebase_admin.initialize_app(cred,{'databaseURL': 'https://lccs-test-bfbb9-default-rtdb.europe-west1.firebasedatabase.app/'})
# get a reference to our db
ref = db.reference()

results = ref.get()
#print(results)
#print(type(results))
for k,v in results.items():
    print("Key is: ", k, " value is: ",v)
    for k2, v2 in v.items():
        print("Key is: ", k2, " value is: ", v2)