import pyrebase

firebase_config = {
    "apiKey": "AIzaSyDFZ1390gkmQ06UNpHtweS9k5PUWjTbknk",
    "authDomain": "fitfeast-dba46.firebaseapp.com",
    "databaseURL": "https://fitfeast-dba46-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "fitfeast-dba46",
    "storageBucket": "fitfeast-dba46.firebasestorage.app",
    "messagingSenderId": "226029188719",
    "appId": "1:226029188719:web:037843dfe45c4d6f0dff9a",
    "measurementId": "G-XSDHKKSDM9"
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()
