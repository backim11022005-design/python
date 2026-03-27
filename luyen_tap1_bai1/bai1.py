class PhepToanPython:
    def __init__(self, a, b, c):
        # Khởi tạo các biến với giá trị truyền vào
        self._a = a
        self._b = b
        self._c = c

    def thuc_thi(self):
        # 1. Các phép toán số học (Arithmetic)
        print("--- 1. Phép toán số học ---")
        print(f"Cộng (_a + _b): {self._a + self._b}")
        print(f"Trừ (_a - _c): {self._a - self._c}")
        print(f"Nhân (_b * _c): {self._b * self._c}")
        print(f"Chia (_a / _b): {self._a / self._b:.2f}")
        print(f"Lũy thừa (_c ** _b): {self._c ** self._b}") # 5 mũ 3

        # 2. Toán tử quan hệ (Comparison)
        print("\n--- 2. Toán tử quan hệ ---")
        print(f"Lớn hơn (_a > _b): {self._a > self._b}")
        print(f"Nhỏ hơn (_b < _c): {self._b < self._c}")
        print(f"Bằng (_a == 16): {self._a == 16}")
        print(f"Khác (_b != _c): {self._b != self._c}")

        # 3. Toán tử gán (Assignment)
        print("\n--- 3. Toán tử gán ---")
        temp = self._a  # Dùng biến tạm để thử nghiệm
        temp += 5;  print(f"Cộng gán (temp += 5): {temp}")
        temp /= 3;  print(f"Chia gán (temp /= 3): {temp:.2f}")
        temp *= 2;  print(f"Nhân gán (temp *= 2): {temp:.2f}")

        # 4. Toán tử logic (and, or, not)
        print("\n--- 4. Toán tử logic ---")
        print(f"AND (_a > 10 and _b < 5): {self._a > 10 and self._b < 5}")
        print(f"OR (_a < 10 or _c == 5): {self._a < 10 or self._c == 5}")
        print(f"NOT (not(_a == _b)): {not(self._a == self._b)}")

        # 5. Toán tử thao tác bit (Bitwise)
        print("\n--- 5. Toán tử thao tác bit ---")
        print(f"Bitwise AND (_a & _c): {self._a & self._c}")
        print(f"Bitwise OR (_a | _b): {self._a | self._b}")
        print(f"Bitwise XOR (_a ^ _c): {self._a ^ self._c}")
        print(f"Dịch trái 3 vị trí (_a << 3): {self._a << 3}")
        print(f"Dịch phải 2 vị trí (_a >> 2): {self._a >> 2}")

# --- Chạy chương trình ---
# Khởi tạo đối tượng với các giá trị đề bài cho: _a=16, _b=3, _c=5
bai_tap = PhepToanPython(16, 3, 5)
bai_tap.thuc_thi()