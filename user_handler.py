from firebase_admin import db

def insert_user(user_data):
    ref = db.reference('users')

    # Get existing users from DB
    existing_users = ref.get()

    if existing_users:
        for user_id, details in existing_users.items():
            if details.get('email') == user_data['email']:
                print("❌ Duplicate user. Not adding to database.")
                return

    # If no duplicate, push new user
    new_ref = ref.push(user_data)
    print("✅ User added successfully with ID:", new_ref.key)
