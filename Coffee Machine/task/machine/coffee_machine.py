# # Write your code here
# cups_of_coffee = input("Write how many cups of coffee you will need:")
# water = 200 * int(cups_of_coffee)
# milk = 50 * int(cups_of_coffee)
# beans = 15 * int(cups_of_coffee)
# print("For " + cups_of_coffee + " cups of coffee you will need:")
# print(str(water) + " ml of water")
# print(str(milk) + " ml of milk")
# print(str(beans) + " g of coffee beans")
# water_input = int(input("Write how many ml of water the coffee machine has:"))
# milk_input = int(input("Write how many ml of milk the coffee machine has:"))
# beans_input = int(input("Write how many grams of coffee beans the coffee machine has:"))
# cups_of_coffee = int(input("Write how many cups of coffee you will need:"))
#
# water_output = water_input * int(cups_of_coffee)
# milk_output = milk_input * int(cups_of_coffee)
# beans_output = beans_input * int(cups_of_coffee)
#
# min_water = 200
# min_milk = 50
# min_beans = 15
#
#
# min_coffee = [int(min_water), int(min_milk), int(min_beans)]
# coffee_input = [int(water_input), int(milk_input), int(beans_input)]
# wanted_output = [int(water_output), int(milk_output), int(beans_output)]
#
# wanted_input = [(min_coffee[0] * cups_of_coffee), (min_coffee[1] * cups_of_coffee),
#                 (min_coffee[2] * cups_of_coffee)]
#
# required_input = [(wanted_output[0]//wanted_input[0]), (wanted_output[1]//wanted_input[1]),
#                   (wanted_output[2]//wanted_input[2])]
#
# if water_input == 0 and milk_input == 0 and beans_input == 0 and cups_of_coffee == 0:
#     print("Yes,I can make that amount of coffee")
# elif min(required_input) == cups_of_coffee:
#     print("Yes, I can make that amount of coffee")
# elif min(required_input) < cups_of_coffee:
#     print("No, I can only make", min(required_input), "of coffee")
# elif min(required_input) > cups_of_coffee:
#     print("Yes, I can make that amount of coffee (and even", min(required_input) - cups_of_coffee, "more than that)")
#
water = 400
milk = 540
beans = 120
cups = 9
money = 550

espresso = [250, 0, 16, 4]
latte = [350, 75, 20, 7]
cappuccino = [200, 100, 12, 6]


def current():
    print("The coffee machine has:")
    print(water, "of water")
    print(milk, "of milk")
    print(beans, "of coffee beans")
    print(cups, "of disposable cups")
    print(money, "of money")


def buy():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3- cappuccino:")
    purchase = int(input())
    print(purchase)
    global water
    global milk
    global beans
    global cups
    global money
    global latte
    global cappuccino
    global espresso
    if purchase == 1:
        water = water - espresso[0]
        beans = beans - espresso[2]
        cups = cups - 1
        money = money + espresso[3]
        current()
    elif purchase == 2:
        water = water - latte[0]
        milk = milk - latte[1]
        beans = beans - latte[2]
        cups = cups - 1
        money = money + latte[3]
        current()
    elif purchase == 3:
        water = water - cappuccino[0]
        milk = milk - cappuccino[1]
        beans = beans - cappuccino[2]
        cups = cups - 1
        money = money + cappuccino[3]
        current()


def fill():
    global water
    global milk
    global beans
    global cups
    print("Write how many ml of water do you want to add:")
    new_water = int(input())
    water = water + new_water
    print("Write how many ml of milk do you want to add:")
    new_milk = int(input())
    milk = milk + new_milk
    print("Write how many grams of coffee beans do you want to add:")
    new_beans = int(input())
    beans = beans + new_beans
    print("Write how many disposable cups of coffee do you want to add:")
    new_cups = int(input())
    cups = cups + new_cups
    current()


def take():
    global money
    print("I gave you $", money)
    money = money * 0
    print()
    current()


def main():
    current()
    print()
    print("Write action (buy, fill, take):")
    user_input = input().lower()
    print(user_input)

    if user_input == "buy":
        buy()
    elif user_input == "fill":
        fill()
    elif user_input == "take":
        take()


main()
