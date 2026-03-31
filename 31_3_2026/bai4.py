n = int(input("Nhập n (n < 20): "))

if n >= 20:
    print("Vui lòng nhập n nhỏ hơn 20.")
else:
    print(f"Các số chia hết cho 5 hoặc 7 từ 1 đến {n} là:")
    for i in range(1, n + 1):
        if i % 5 == 0 or i % 7 == 0:
            print(i, end=" ")