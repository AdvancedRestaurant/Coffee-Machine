column = int(input())
row = int(input())

if (column == 1 and row == 1) or (column == 1 and row == 8) or (column == 8 and row == 1) or (column == 8 and row == 8):
    print(3)
elif (column == 1 and row !=1) or (column == 1 and row != 8):
    print(5)
elif (column == 8 and row !=1) or (column == 8 and row != 8):
    print(5)
elif (row == 1 and column != 1) or (row == 1 and column != 8):
    print(5)
elif (row == 8 and column != 1) or (row == 8 and column != 8):
    print(5)
else:
    print(8)