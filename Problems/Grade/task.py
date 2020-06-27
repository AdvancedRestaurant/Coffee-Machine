student_score = float(input())
max_score = int(input())

percentage = (student_score / max_score) * 100

if percentage < 60 and max_score != 0:
    print("F")
elif 60 <= percentage < 70 and max_score != 0:
    print("D")
elif 70 <= percentage < 80 and max_score != 0:
    print("C")
elif 80 <= percentage < 90 and max_score != 0:
    print("B")
# elif percentage > 90 and max_score != 0:
#     print("A")
else:
    print("A")
