import datetime

print("Check if it's Tuesday!")

today = datetime.datetime.today()
dayOfWeek = today.weekday()

if dayOfWeek == 1:
    print("It's Tuesday!")
elif dayOfWeek == 2: 
    print("It's Wednesday.")    
else:
    print("It's not Tuesday.")
