chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769

user_money = abs(int(input()))
if user_money < chicken:
    print("None")
elif chicken <= user_money < goat:
    if (user_money // chicken) == 1:
        print((user_money // chicken), "chicken")
    elif (user_money // chicken) >= 2:
        print((user_money // chicken), "chickens")
elif goat <= user_money < pig:
    if (user_money // goat) == 1:
        print((user_money // goat), "goat")
    elif (user_money // goat) >= 2:
        print((user_money // goat), "goats")
elif pig <= user_money < cow:
    if (user_money // pig) == 1:
        print((user_money // pig), "pig")
    elif (user_money // pig) >= 2:
        print((user_money // pig), "pigs")
elif cow <= user_money < sheep:
    if (user_money // cow) == 1:
        print((user_money // cow), "cow")
    elif (user_money // cow) >= 2:
        print((user_money // cow), "cows")
# elif user_money >= sheep:
#     if (user_money // sheep) == 1:
#         print((user_money // sheep), "sheep")
#     elif (user_money // sheep) >= 2:
#         print((user_money // sheep), "sheep")
else:
    print((user_money // sheep), "sheep")