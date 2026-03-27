a = int(input("Nhập số thứ nhất (a): "))
b = int(input("Nhập số thứ hai (b): "))
c = int(input("Nhập số thứ ba (c): "))

# a) Tổng và Tích
print(f"--- Câu a ---")
print(f"Tổng: {a + b + c}")
print(f"Tích: {a * b * c}")

# b) Hiệu của 2 số bất kỳ (ví dụ a và b)
print(f"--- Câu b ---")
print(f"Hiệu của a và b là: {a - b}")

# c) Các phép chia giữa a và b
print(f"--- Câu c ---")
if b != 0:
    print(f"Chia lấy phần nguyên (a // b): {a // b}")
    print(f"Chia lấy phần dư (a % b): {a % b}")
    print(f"Kết quả chính xác (a / b): {a / b}")
else:
    print("Không thể chia cho số 0!")