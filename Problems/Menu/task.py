pizza = ['Margarita', 'Four Seasons', 'Neapoletana', 'Vegetarian', 'Spicy']
salad = ["Caesar salad", "Green salad", "Tuna salad", "Fruit salad"]
soup = ["Chicken soup", "Ramen", "Tomato soup", "Mushroom cream soup"]

menu_choice = input()

if menu_choice == "pizza":
    print(', '.join(pizza))
elif menu_choice == "salad":
    print(', '.join(salad))
elif menu_choice == "soup":
    print(', '.join(soup))
else:
    print("Sorry, we don't have it in the menu")