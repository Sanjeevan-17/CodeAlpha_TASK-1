import firebase_admin
from firebase_admin import credentials, db

# Load service account key
cred = credentials.Certificate("serviceAccountKey.json")

# Initialize Firebase app
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://task-1-ba4e7-default-rtdb.firebaseio.com/'
})
