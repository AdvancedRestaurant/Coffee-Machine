# Make sure your output matches the assignment *exactly*
input_hours = int(input())

if input_hours < 2:
    print("That seems reasonable")
elif 2 <= input_hours <4:
    print("Do you have time for anything else?")
else:
    print("You need to get outside more!")