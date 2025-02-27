def getInput():
    print("Enter your age")
    age = input()
    print("Enter your mark")
    mark = int(input())
    return age, mark

def calcOne(mark):
    mark = mark * 2
    return mark

def calcTwo(mark):
    mark = mark * 1.5
    return mark

def calcThree(mark):
    mark = mark * 0.8
    return mark

age, mark = getInput()
if age <= "14":
    mark = calcOne(mark)
    mark = calcTwo(mark)
    mark = calcThree(mark)
    
elif age == "15":
    mark = calcTwo(mark)
    mark = calcThree(mark)
    
else:
    mark = calcThree(mark)
    
print(mark)