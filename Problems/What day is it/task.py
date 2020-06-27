utc_input = input()
tuesday = ["0", "+1", "+2", "+3", "+4", "+5", "+6", "+7", "+8", "+9", "+10", "+11", "+12", "+13", "-10", "-9", "-8",
           "-7", "-6", "-5", "-4", "-3", "-2", "-1"]
wednesday = "+14"
monday = ["-12", "-11"]

if utc_input in tuesday:
    print("Tuesday")
elif utc_input == wednesday:
    print("Wednesday")
elif utc_input in monday:
    print("Monday")
