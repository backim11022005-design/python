import tkinter as tk
import random

# --- CẤU HÌNH BAN ĐẦU ---
WIDTH = 600
HEIGHT = 600
INITIAL_SPEED = 120 # Tốc độ ban đầu (ms)
SPACE_SIZE = 20
BODY_COLOR = "#2ecc71" # Xanh lá nhẹ
HEAD_COLOR = "#27ae60" # Xanh lá đậm
FOOD_COLOR = "#e74c3c" # Màu đỏ táo
BG_COLOR = "#2c3e50"   # Màu xanh đen hiện đại

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rắn Săn Mồi Pro - Python 3.14")

        self.score = 0
        self.speed = INITIAL_SPEED
        self.direction = 'down'

        # Hiển thị điểm số
        self.label = tk.Label(self.root, text=f"Điểm: {self.score} | Tốc độ: {self.speed}ms", 
                              font=('Consolas', 20), fg="white", bg=BG_COLOR)
        self.label.pack(fill='x')

        self.canvas = tk.Canvas(self.root, bg=BG_COLOR, height=HEIGHT, width=WIDTH, highlightthickness=0)
        self.canvas.pack()

        # Điều khiển
        self.root.bind('<Left>', lambda e: self.change_direction('left'))
        self.root.bind('<Right>', lambda e: self.change_direction('right'))
        self.root.bind('<Up>', lambda e: self.change_direction('up'))
        self.root.bind('<Down>', lambda e: self.change_direction('down'))

        # Khởi tạo rắn (3 đốt)
        self.snake_coords = [(100, 100), (100, 80), (100, 60)]
        self.snake_body = []
        self.food = None
        
        self.start_game()

    def start_game(self):
        for x, y in self.snake_coords:
            square = self.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=BODY_COLOR, tag="snake")
            self.snake_body.append(square)
        self.canvas.itemconfig(self.snake_body[0], fill=HEAD_COLOR)

        self.create_food()
        self.next_turn()

    def create_food(self):
        # Sửa lỗi chia số thực cho Python 3.14 bằng //
        x = random.randint(0, (WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.food = (x, y)
        self.canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

    def next_turn(self):
        x, y = self.snake_coords[0]

        if self.direction == "up": y -= SPACE_SIZE
        elif self.direction == "down": y += SPACE_SIZE
        elif self.direction == "left": x -= SPACE_SIZE
        elif self.direction == "right": x += SPACE_SIZE

        # --- TÍNH NĂNG XUYÊN TƯỜNG ---
        if x < 0: x = WIDTH - SPACE_SIZE
        elif x >= WIDTH: x = 0
        if y < 0: y = HEIGHT - SPACE_SIZE
        elif y >= HEIGHT: y = 0

        new_head = (x, y)

        # Kiểm tra đâm vào thân mình
        if new_head in self.snake_coords:
            self.game_over()
            return

        self.snake_coords.insert(0, new_head)
        square = self.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=HEAD_COLOR)
        self.canvas.itemconfig(self.snake_body[0], fill=BODY_COLOR)
        self.snake_body.insert(0, square)

        # Kiểm tra ăn mồi
        if x == self.food[0] and y == self.food[1]:
            self.score += 1
            # Tăng tốc độ: nhanh hơn 3ms mỗi lần ăn, tối thiểu là 40ms
            if self.speed > 40:
                self.speed -= 3
            
            self.label.config(text=f"Điểm: {self.score} | Tốc độ: {self.speed}ms")
            self.canvas.delete("food")
            self.create_food()
        else:
            del self.snake_coords[-1]
            self.canvas.delete(self.snake_body[-1])
            del self.snake_body[-1]

        self.root.after(self.speed, self.next_turn)

    def change_direction(self, new_direction):
        opposites = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}
        if new_direction != opposites.get(self.direction):
            self.direction = new_direction

    def game_over(self):
        self.canvas.delete("all")
        self.canvas.create_text(WIDTH/2, HEIGHT/2, font=('Consolas', 50, 'bold'), 
                                text="GAME OVER", fill="#e74c3c")
        self.canvas.create_text(WIDTH/2, HEIGHT/2 + 60, font=('Consolas', 20), 
                                text=f"Tổng điểm: {self.score}", fill="white")

if __name__ == "__main__":
    root = tk.Tk()
    # Không cho phép thay đổi kích thước cửa sổ để tránh lỗi hiển thị
    root.resizable(False, False)
    game = SnakeGame(root)
    root.mainloop()