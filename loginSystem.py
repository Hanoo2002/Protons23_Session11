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
def choice_printer():
    print("\nWhat would you like to do?")
    print("1)login ")
    print("2)register ")
    print("3) Exit\n")
    choice = int(input("> "))
    print("")
    return choice
while True: #loop runs forever till break
    choice=choices_printer()
    match choice:
        case 1:

            has_username = login()
            if has_username == 0:
                print("error: username not found")
            elif has_username == -1:
                print("error: incorrect password")
            else:
                print(f"\nWelcome back, {has_username}!")
                print("Your secret phrase is:")
                print(database[has_username]["secret"])
            continue
        case 2:
            register=register()
            if registered == 1:
                print("\nSuccessfuly Registered!")
            elif registered==-1:
                print("error: username already exists")
            continue
        case 3:
            print("Thank You")
            break
        case _:
            print("error: invalid input")
