best_sleep = int(input())
over_sleep = int(input())
current_sleep = int(input())


if current_sleep < best_sleep:
    print("Deficiency")
else:
    if current_sleep > over_sleep:
        print("Excess")
    else:
        print("Normal")

