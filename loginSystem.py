# simple login system with dictionary

database = {}
constantMessage1 = 'Username  '#i wanted to use a constant but had no idea what to do
#checks if username is in dattabase
def username_checker(username):
    return username in database.keys()
#for login
def login():
    username = input(constantMessage1)
    if not username_checker(username):
        return 0
    password = input("Password: ")
    if password == database[username]["password"]:
        return username
    else:
        return -1
#for register
def register():
    username = input(constantMessage1)
    if username_checker(username):
        return -1
    new_password = input("New Password: ")
    secret = input("Now enter your secrete phrase for safekeeping: ")
    database[username] = {"password": new_password, "secret": secret}
    return 1
            print("Thank You")
            break
        case _:
            print("error: invalid input")
