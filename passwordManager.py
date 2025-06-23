class PasswordManager:
    def __init__(self):
        self.passwords = {}
        self.mainpassword = "pwd135"
    
    def authentication(self,password):
        return password == self.mainpassword

    def store_password(self, page, username, password):
        if page and username and password:
            self.passwords[page] =  {"username": username, "password": password}
            print("Password stored\n")
        else:
            print("Please enter the valid details")
    
    def retrieve_password(self, page):
        if page in self.passwords:
            username = self.passwords[page]["username"]
            password = self.passwords[page]["password"]
            print(f"Username: {username}")
            print(f"Password: {password}")
            print("Password retrieved\n")
        else:
            print("Page not found\n")

    def encryption(self):
        encrypted_passwords = {}
        for page,details in self.passwords.items():
            encrypted_passwords[page] = {
               "username": "".join([chr(ord(char) + 3) for char in details["username"]]),
               "password": "".join([chr(ord(char) + 3) for char in details["password"]])
            }
        return encrypted_passwords
    
    def decryption(self,encrypted_passwords):
        decrypted_passwords = {}
        for page,details in encrypted_passwords.items():
            decrypted_passwords[page] = {
                "username": "".join([chr(ord(char)-3) for char in details["username"]]),
               "password": "".join([chr(ord(char)-3) for char in details["password"]]) 
            }
        return decrypted_passwords
    
def passwords():
    p_manager = PasswordManager()
    attempts = 0
    while attempts < 3:
        main_password = input("Enter main password: ")
        if p_manager.authentication(main_password):
            print("Authenticated successful\n")
            break
        else:
            print("Incorrect password")
            attempts += 1
    if attempts == 3:
        print("Maximum attempts finished")
        return
    
    while True:
        print("Password Manager:")
        print("1. Store password")
        print("2. Retrieve password")
        print("3. Exit")
        option = input("Enter your option: ")
        if(option == "1"):
            page = input("Enter page name: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            p_manager.store_password(page, username, password)

        elif(option == "2"):
            page = input("Enter page name to retrieve: ")
            p_manager.retrieve_password(page)

        elif(option == "3"):
            print("Encrypted passwords: ")
            encrypted = p_manager.encryption()
            for page,details in encrypted.items():
                print(f"Page name: {page}")
                print(f"Username: {details['username']}")
                print(f"Password: {details['password']}")
                
            decrypted = p_manager.decryption(encrypted)
            print("\nDecrypted passwords: ")
            for page,details in decrypted.items():
                print(f"Page name: {page}")
                print(f"Username: {details['username']}")
                print(f"Password: {details['password']}")
            print("Exiting!!!")
            break
        else:
            print("Invalid option")
passwords()
