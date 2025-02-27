def calculate(num1, num2):
    print("Finding out calculate of", num1, num2)
    if num1 == num2:
        return num1
    elif num1 < num2:
        return calculate(num1, (num2-num1))
    else:
        return calculate(num2, (num1-num2))

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

print("The highest common factor of", num1, "and", num2, "is:", calculate(num1, num2))
