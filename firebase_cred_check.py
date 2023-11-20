import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
# path to the private key
cred = credentials.Certificate("C:/Users/k_tur/OneDrive/Documents/cs/CS_project/lccs-test-bfbb9-firebase-adminsdk-x7grr-c87af7adbe.json")
# URL to the database
firebase_admin.initialize_app(cred,{'databaseURL': 'https://lccs-test-bfbb9-default-rtdb.europe-west1.firebasedatabase.app/'})
# get a reference to our db
ref = db.reference('/') # the / is referencing the root of our database - the very start
# adding some data
# use a dictionary
ref.set({'users': {'user1': {'name':'bob',
                   'height':'tall',
                   'age':200},
         'user2':{'name':'jane',
                  'height':'small',
                  'age':200}
         }}) #the dictionary goes in {}, a {} inside a {} is a nested dictionary