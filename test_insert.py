import firebase_init  # initializes Firebase
from user_handler import insert_user

# Sample test users
user_1 = {
    "name": "Alice",
    "email": "alice@gmail.com",
    "phone": "1234567890"
}

user_2 = {
    "name": "Bob",
    "email": "alice@gmail.com", 
    "phone": "9876543210"
}
user_3= {
    "name": "charlie",
    "email": "cahrlie@gmail.com",  # same email as user_1 (duplicate)
    "phone": "9876543210"
}

# Insert test data
insert_user(user_1)  # Should insert
insert_user(user_2)  # Should insert
insert_user(user_3)  # Should detect duplicate