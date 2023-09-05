import hashlib

# Simple user database as a dictionary
user_database = {}

def register(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user_database[username] = hashed_password
    print("User registered successfully!")

def login(username, password):
    if username in user_database:
        stored_password = user_database[username]
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if stored_password == hashed_password:
            print("Login successful!")
            return True
    print("Login failed!")
    return False

def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            register(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            login(username, password)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == '__main__':
    main()
