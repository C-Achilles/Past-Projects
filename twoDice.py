from random import *
import matplotlib.pyplot as plt

xline=[]

def rollDice(i):
  j=0
  while j <= i:
    roll1=randint(1,6)
    roll2=randint(1,6)
 
    rollTotal=roll1+roll2
    xline.append(rollTotal)
#    print("Roll 1 is: " + str(roll1))
#    print("Roll 2 is: " + str(roll2))
#    print(rollTotal)
    j=j+1

rollDice(1000)
print(xline)
plt.plot(xline)
plt.show()
