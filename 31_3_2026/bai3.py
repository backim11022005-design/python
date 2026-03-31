print("Các số chia hết cho 2 và 3 trong khoảng 80-100:")
for i in range(80, 101):
    if i % 2 == 0 and i % 3 == 0:
        print(i, end=" ")
