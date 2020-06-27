index_of_synthetic = float(input())

if index_of_synthetic < 2:
    print("Analytic")
elif 2 <= index_of_synthetic <= 3:
    print("Synthetic")
else:
    print("Polysynthetic")
