num1 = int(input("Enter number 1 "))
num2 = int(input("Enter number 2 "))
if num1 >= num2:
    num1 += num2
    print(num1)
else:
    num2 -= num1
    print(num2)