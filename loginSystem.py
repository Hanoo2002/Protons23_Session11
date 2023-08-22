# simple login system with dictionary
database = {}
constant = 'Username: '

#checks if username is in dattabase
def check_user(name):
    return name in database.keys()

#for login
def login():
    name = input(constant)
    if not check_user(name):
        return 0
    password = input("Password: ")
    if password == database[name]["password"]:
        return name
    else:
        return -1
    
#for register
def register():
    name = input(constant)
    if check_user(name):
        return -1
    new_pass = input("New Password: ")
    secrete = input("Now enter passwordour secrete phrase for safekeeping: ")
    database[name] = {"password": new_pass, "secret": secrete}
    return 1

def main_screen():
    print("\nWhat would you like to do?")
    print("1) login")
    print("2) register")
    print("3) Exit\n")
    num = int(input("> "))
    print("")
    return num

#loop runs forever till break
while True: 
    screen = main_screen()
    match screen:
        case 1:
            sign = login()
            if sign == 0:
                print("error: username not found")
            elif sign == -1:
                print("error: incorrect password")
            else:
                print(f"\nWelcome back, {sign}!")
                print("Your secret phrase is:")
                print(database[sign]["secret"])
            continue

        case 2:
            sign=register()
            if sign == 1:
                print("\nSuccessfuly Registered!")
            elif sign==-1:
                print("error: username already exists")
            continue
        
        case 3:
            print("Thank You")
            break
        case _:
            print("error: invalid input")
