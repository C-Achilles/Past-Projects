percentage = int(input("Enter your percentage"))
if percentage == 100:
    print("Full")

else:
    timeToCharge = (100 - percentage)*10
    hours = timeToCharge//60
    minutes = timeToCharge%60
    print(hours, " hours and ", minutes, " minutes until fully charged")
