import math

# Nhập các hệ số
a = float(input("Nhập hệ số a (a khác 0): "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if a == 0:
    print("Đây không phải phương trình bậc 2 (a phải khác 0)")
else:
    # Tính Delta
    delta = b**2 - 4*a*c
    print(f"Delta = {delta}")

    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Phương trình có nghiệm kép: x = {x}")
    else:
        # Trường hợp delta > 0
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Phương trình có 2 nghiệm phân biệt:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")