import json

with open("data.json", "r") as file:
    data = json.load(file)

ans = None
user = None
password = None

def login(): 
    global user
    
    print("'Log in' or 'Create account'?")
    ans = input().lower()
    
    if ans == "log in":
        
        print("What's your username")
        user = input()
        
        print("What is your password?")
        password = input()
        
        if password == data[user]['password']:
            pass
        else:
            print("Invalid password, try again")
            login()
            
    elif ans == "create account":
            
            print("What's your username, password (comma separated)")
            new_user = input()
            new_user_credentials = new_user.split(",")
            if len(new_user_credentials) > 2:
                print("Too many arguments, please enter a 'username, password'")
                login()
                
            user = new_user_credentials[0].strip()
            password = new_user_credentials[1].strip()
        
            if user in data:
                print("Username already in use, please try again")
                login()
        
            create_user(user, password)
    
def ask_intent(user):
    
    print("What do you want to do? (transfer, balance, exit")
    intent = input().lower()

    if intent == "transfer":
        transfer(user)
        
    elif intent == "balance":
        print(f"Your balance is {data[user]['balance']}")
        
    elif intent == "create new account":
        print("Enter new username, password (comma separated)")
        new_user = input()

        new_user_credentials = new_user.split(",")
        
        user = new_user_credentials[0].strip()
        password = new_user_credentials[1].strip()
        
        create_user(user, password)

    elif intent == "exit":
        exit()
def transfer(user):
    global ans
    
    print("Who do you want to transfer to? " + str(list(data.keys())))
    ans = input().lower()
    
    def ask_amount():
        print("How much would you like to transfer?")
        amount = input()
        
        if "," in amount:
            amount = amount.replace(",", "")
            amount = int(amount)
            
        if amount > data[user]['balance']:
            print("You can't transfer more than you have, try again")
            
        else:
            data[user]['balance'] -= amount
            data[ans]['balance'] += amount
            print("Transfer successful!")
            print(f"{user} balance: {data[user]['balance']}")
            print(f"{ans} balance: {data[ans]['balance']}")
            save_data(data)
            
    if ans in data:
        ask_amount()
        
    else:
        print("That username doesn't exist, create a new user and transfer? Yes/No")
        create = input().lower()
        
        if create == "yes":
            print("Password? ")
            password = input()
            create_user(ans, password)
            ask_amount()
            
        else:
            transfer(user)
            ask_amount()


def create_user(user, password):
    
        data[user] = {"balance": 0, "password": password}
        save_data(data)

def save_data(data):
    
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
        
login()
ask_intent(user)
