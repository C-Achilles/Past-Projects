import csv
from datetime import *
from Test2 import *

# Set the date that wordle first started on 
beginning = datetime.strptime("Jun 18 2021 1:01am", '%b %d %Y %I:%M%p')
anotherGo = "yes"

# numOfDays will return how many days it has been since the beginning
def numOfDays(date1, date2):
    return (date2-date1).days

# Repeat the program for as long as the user would like to continue 
while anotherGo == "yes":

    #open the word list
    f=open("WordleListMay22.csv", "r")
    fReader= csv.reader(f)
    value= input("Are you inputting a date or a word? Type 'd' or 'w' ")

    #This section will return the date a given word will appear on 
    if value.lower() == "w":
        print("The point of the code is to enter a 5 letter word and the program will tell you when that word will run on Wordle")
        word = str(input("Enter your word: "))

        # Put the users word into a list
        listOfLetters = list(word)
        x=0

        # Search through the list of words for the words given by the user 
        for row in fReader:
            x+=1
            if listOfLetters == row:
                print("This word will appear on: " + (str(beginning + timedelta(days = x))))
                f.close()
                break

    # This code will return the word on a date the user has specified 
    elif value.lower() == "d":
        print("You will need to enter the date in this format: 10, Mar, 2022. This will need to be seperate though")
        inputDay = input("Enter the day: ")
        inputMonth = input("Enter the month: ")
        inputYear = input("Enter the year: ")

        # Convert the date into the number of days since the beginning of wordle
        dateTime = inputMonth + " " + inputDay + " " + inputYear + " 1:01am"
        newDate = datetime.strptime(dateTime, '%b %d %Y %I:%M%p')
        days = numOfDays(beginning, newDate)
        
        # Put the list of letters back into a single string
        for i in range(0, days):
            line = f.readline()
        print(line)
        f.close()

    # Ask the user if they would like to go again 
    anotherGo = input("Would you like another go? Type 'yes' or 'no' ").lower()
