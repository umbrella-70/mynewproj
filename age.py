import datetime
useryear=int(input("Enter your DOB Year:"))
currentyear=datetime.date.today().year
print(currentyear-useryear,"Years Old")
