# Bán kính có thể là số thập phân nên dùng float
r = float(input("Nhập bán kính đường tròn (R): "))
_pi = 3.14

# Công thức theo yêu cầu đề bài
cv = 2 * r * _pi
dt = _pi * r * r  # hoặc _pi * (r ** 2)

print(f"Chu vi (CV): {cv}")
print(f"Diện tích (DT): {dt}")