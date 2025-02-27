target = "50"
numberGuessed = False

while numberGuessed == False:
    userInput = input("Enter your number: ")


    if userInput > target:
        print("Too high!")

    elif userInput < target:
        print("Too low!")

    else:
        print("Correct!")
        numberGuessed = True
