q1 = input("What is the capital of England?: ")
q2 = input("What is the largest cell in the human body?: ")
q3 = input("What is the largest country in the world?: ")
q4 = input("Who painted the Mona Lisa?: ")
q5 = input("What is the fastest land animal?: ")
points = 0

if q1.lower() == "london":
    points = points + 1
if q2.lower() == "ovum":
    points = points + 1
if q3.lower() == "russia":
    points = points + 1
if q4.lower == "leonardo da vinci":
    points = points + 1
if q5.lower() == "cheetah":
    points = points + 1

if points > 3:
    print("Well done! You got {} out of 5".format(points))
else:
    print("You lost! You got {} out of 5".format(points))
