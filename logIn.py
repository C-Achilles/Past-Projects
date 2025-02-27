import csv


def logIn():
    enter = False
    while enter == False:
        f=open("LogIn.csv", "r")
        fReader = csv.reader(f)
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        for row in fReader:
            if username == row[0]:
                if password == row[1]:
                    enter = True
                else:
                    print("Wrong password. Please try again.")
            else:
                print("No such user")
        f.close()
    print("Welcome")


def newUser():
    f=open("LogIn.csv", "a")
    writer = csv.writer(f)
    apply = False
    while apply == False:
        username = input("Enter your new username: ")
        password = input("Enter your new password: ")
        check = input("Re-enter your new password: ")
        if password == check:
            user = [username, password]
            writer.writerow(user)
            apply = True
        else:
            print("Those passwords dont match. Please try again.")
    f.close()


while True:
    command = input("Would you like to log in (L), Create a new user (N), or shut down (S) ")
    if command.upper() == "L":
        logIn()
    elif command.upper() == "N":
        newUser()
    else:
        break
