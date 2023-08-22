# simple login system with dictionary

database = {}
MESSAGE1 = "Username"
#checks if username is in dattabase
def checking(username):
    return username in database.keys()
#for login
def Login():
    username= input( MESSAGE1)
    if not checking(username):
        return 0
    password= input("Password: ")
    if password== database[x]["password"]:
        return username
    else:
        return -1
#for register
def register():
    username= input(MESSAGE1)
    if checking(username):
        return -1
    password = input("New Password: ")
    secret = input("Now enter your secrete phrase for safekeeping: ")
    database[username] = {"password": password, "secret": secret}
    return 1
def choosing():
    print("\nWhat would you like to do?")
    print("1) ")
    print("2) ")
    print("3) Exit\n")
    v = int(input("> "))
    print("")
    return v
while True: #loop runs forever till break
    c = choosing()
    match c:
        case 1:

            s = register()
            if s == 0:
                print("error: username not found")
            elif s == -1:
                print("error: incorrect password")
            else:
                print(f"\nWelcome back, {s}!")
                print("Your secret phrase is:")
                print(database[s]["secret"])
            continue
        case 2:
            s=Login()
            if s == 1:
                print("\nSuccessfuly Registered!")
            elif s==-1:
                print("error: username already exists")
            continue
        case 3:
            print("Thank You")
            break
        case _:
            print("error: invalid input")
