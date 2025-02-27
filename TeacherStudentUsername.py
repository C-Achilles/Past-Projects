first = input("Enter your first name: ")
last = input("Enter your last name: ")
role = input("Teacher or Student? ")

if role.lower() == "teacher":
    first = first[:2]
    last = last[-3:]
    username = last+first
elif role == "student":
    first = first[:3]
    last = last[-1:]
    username = first+last

print(username)
