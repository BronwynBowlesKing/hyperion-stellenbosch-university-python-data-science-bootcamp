hour = int(input("Enter the hour. Just include the first part of the time (hour) from 0 (midnight) to 23 (11 pm) and leave out the minutes (:00): "))

if 0 <= hour < 12:        # 00 to 11 
    greeting = "Good morning"

elif 12 <= hour < 19:     # 12 to 18 
    greeting = "Good afternoon"

elif 19 <= hour < 23:     # 19 to 22 PM
    greeting = "Good evening"
    
else:                     # 23
    greeting = "Get to bed"

print(greeting)
