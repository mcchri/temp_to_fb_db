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

ref.update({'JaneDoe123':True})
ref = db.reference().child('classes')
ref.update({'Biology123':''})
ref.update({'Math123':''})

ref = db.reference().child('classes').child('Biology123')
ref.update({'Description':'Biology123 class', 'id':'Biology123', 'title':'Biology 123'})
ref = db.reference().child('classes').child('Math123')
ref.update({'Description':'Math123 class', 'id':'Math123', 'title':'Math123'})

ref = db.reference().child('classes').child('Biology123')
ref.delete()
