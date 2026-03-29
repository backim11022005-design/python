n = int(input("Nhập vào một số nguyên dương: "))

# Kiểm tra chia hết cho cả 2 và 3 trước
if n % 2 == 0 and n % 3 == 0:
    print(f"{n} chia hết cho cả 2 và 3")
elif n % 2 == 0:
    print(f"{n} chia hết cho 2")
elif n % 3 == 0:
    print(f"{n} chia hết cho 3")
else:
    print(f"{n} không chia hết cho 2 cũng không chia hết cho 3")