num = int(input("Enter a number "))
age = input("Enter your age ")
if age <= "10":
    num = num / 10
elif age <= "18":
    num = num + 10
elif age > "18":
    num = num * 10

if num < 100:
    num = 0
    
print(num)