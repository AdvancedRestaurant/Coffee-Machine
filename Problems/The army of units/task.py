army_input = int(input())

if army_input < 1:
    print("no army")
elif 1 <= army_input < 10:
    print("few")
elif 10 <= army_input < 50:
    print("pack")
elif 50 <= army_input < 500:
    print("horde")
elif 500 <= army_input < 1000:
    print("swarm")
else:
    print("legion")

