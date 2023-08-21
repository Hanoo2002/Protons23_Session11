# simple login system with dictionary

database = {}
constantMessage1 = 'Username  '#i wanted to use a constant but had no idea what to do
#checks if username is in dattabase
def printingOutAllChoicesAndReturnUserChoice():
    print("\nWhat would you like to do?")
    print("1) Log in ")
    print("2) Register ")
    print("3) Exit\n")
    v = int(input("Choice: "))
    print("")
    return v

def checkingCaseOfUserNameInDataBase(x):
    return x in database.keys()

def logging_in():
    x = input(constantMessage1)
    if  not checkingCaseOfUserNameInDataBase:
        return 0
    y = input("Password: ")
    if y == database[x]["password"]:
        return x
    else:
        return -1
#for register
def signing_up():
    x = input(constantMessage1)
    if checkingCaseOfUserNameInDataBase(x):
        return -1
    y = input("New Password: ")
    z = input("Now enter your secrete phrase for safekeeping: ")
    database[x] = {"password": y, "secret": z}
    return 1

while True: #loop runs forever till break
    c = printingOutAllChoicesAndReturnUserChoice()
    match c:
        case 1 : #case of log in

            s = logging_in()
            if s == 0:
                print("error: username not found")
            elif s == -1:
                print("error: incorrect password")
            else:
                print(f"\nWelcome back,{s}!")
                print("Your secret phrase is:")
                print(database[s]["secret"])
            continue
        case 2: #case of sign up
            s=signing_up()
            if s == 1:
                print("\nSuccessfuly Registered!")
            elif s==-1:
                print("error: username already exists")
            continue
        case 3: #Exit
            print("Thank You")
            break
        case _:
            print("error: invalid input")
