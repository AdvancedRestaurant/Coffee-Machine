# put your python code here
first_number = float(input())
second_number = float(input())
user = input()

operations = ["+", "-", "/", "*", "mod", "pow", "div"]

if user == operations[0]:
    print(first_number + second_number)
elif user == operations[1]:
    print(first_number - second_number)
elif user == operations[2]:
    if second_number != 0:
        print(first_number / second_number)
    else:
        print("Division by 0!")
elif user == operations[3]:
    print(first_number * second_number)
elif user == operations[4]:
    if second_number != 0:
        print(first_number % second_number)
    else:
        print("Division by 0!")
elif user == operations[5]:
    print(first_number ** second_number)
elif user == operations[6]:
    if second_number != 0:
        print(first_number // second_number)
    else:
        print("Division by 0!")
