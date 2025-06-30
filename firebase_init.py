import firebase_admin
from firebase_admin import credentials, db

# Load service account key
cred = credentials.Certificate("serviceAccountKey.json") #ADD FIREBASE JSON FILE

# Initialize Firebase app
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https:/-------' #ADD YOU ARE FIREBASE API
})
