import tkinter as tk
import random
from tkinter import messagebox

class Minesweeper:
    def __init__(self, root, rows=10, cols=10, mines=10):
        self.root = root
        self.root.title("Minesweeper - Python 3.14")
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.buttons = []
        self.mine_locations = set()
        self.revealed_count = 0
        self.game_over = False
        self.setup_ui()
        self.place_mines()

    def setup_ui(self):
        for r in range(self.rows):
            row_btns = []
            for c in range(self.cols):
                btn = tk.Button(self.root, width=3, height=1, font=('Arial', 12, 'bold'),
                                command=lambda r=r, c=c: self.click(r, c))
                btn.bind("<Button-3>", lambda e, r=r, c=c: self.flag(r, c)) # Chuột phải cắm cờ
                btn.grid(row=r, column=c)
                row_btns.append(btn)
            self.buttons.append(row_btns)

    def place_mines(self):
        while len(self.mine_locations) < self.mines:
            r, c = random.randint(0, self.rows-1), random.randint(0, self.cols-1)
            self.mine_locations.add((r, c))

    def count_adjacent_mines(self, r, c):
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if (r+dr, c+dc) in self.mine_locations:
                    count += 1
        return count

    def click(self, r, c):
        if self.game_over or self.buttons[r][c]['text'] == "🚩": return
        
        if (r, c) in self.mine_locations:
            self.buttons[r][c].config(text="💣", bg="red")
            self.game_over = True
            messagebox.showerror("BÙM!", "Bạn đạp trúng mìn rồi!")
            self.root.destroy()
        else:
            self.reveal(r, c)
            if self.revealed_count == (self.rows * self.cols) - self.mines:
                messagebox.showinfo("Thắng!", "Chúc mừng! Bạn là chuyên gia gỡ mìn.")
                self.root.destroy()

    def reveal(self, r, c):
        if not (0 <= r < self.rows and 0 <= c < self.cols) or \
           self.buttons[r][c]['state'] == 'disabled': return

        self.buttons[r][c].config(state='disabled', relief=tk.SUNKEN, bg="#ddd")
        self.revealed_count += 1
        mines_near = self.count_adjacent_mines(r, c)
        
        if mines_near > 0:
            colors = ["", "blue", "green", "red", "darkblue", "darkred", "cyan", "black", "gray"]
            self.buttons[r][c].config(text=str(mines_near), fg=colors[mines_near])
        else:
            # Nếu không có mìn xung quanh, tự động mở các ô lân cận (Thuật toán loang)
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr != 0 or dc != 0:
                        self.reveal(r+dr, c+dc)

    def flag(self, r, c):
        if self.buttons[r][c]['state'] == 'normal':
            current_text = self.buttons[r][c]['text']
            self.buttons[r][c].config(text="🚩" if current_text == "" else "", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    game = Minesweeper(root)
    root.mainloop()