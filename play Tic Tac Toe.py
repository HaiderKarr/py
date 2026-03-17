import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("❌⭕ إكس أو")
        self.window.configure(bg="#2d3436")
        
        self.turn = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.game_over = False
        
        # عنوان
        title = tk.Label(
            self.window,
            text="لعبة إكس أو",
            font=("Arial", 24, "bold"),
            bg="#2d3436",
            fg="#dfe6e9",
            pady=10
        )
        title.grid(row=0, column=0, columnspan=3)
        
        # إنشاء الأزرار
        for i in range(3):
            for j in range(3):
                btn = tk.Button(
                    self.window,
                    text="",
                    font=("Arial", 40, "bold"),
                    width=3,
                    height=1,
                    bg="#636e72",
                    fg="white",
                    command=lambda r=i, c=j: self.click(r, c)
                )
                btn.grid(row=i+1, column=j, padx=5, pady=5)
                self.buttons[i][j] = btn
        
        # زر إعادة اللعبة
        restart_btn = tk.Button(
            self.window,
            text="🔄 إعادة",
            font=("Arial", 14),
            bg="#00b894",
            fg="white",
            command=self.reset
        )
        restart_btn.grid(row=4, column=0, columnspan=3, pady=10)
    
    def click(self, row, col):
        if self.game_over:
            return
        
        btn = self.buttons[row][col]
        if btn["text"] != "":
            return
        
        # وضع الرمز
        btn["text"] = self.turn
        btn["fg"] = "#00cec9" if self.turn == "X" else "#fd79a8"
        
        # التحقق من الفوز
        if self.check_win():
            messagebox.showinfo("🎉", f"اللاعب {self.turn} فاز!")
            self.game_over = True
            return
        
        # التحقق من التعادل
        if all(btn["text"] != "" for row in self.buttons for btn in row):
            messagebox.showinfo("🤝", "تعادل!")
            self.game_over = True
            return
        
        # تبديل الدور
        self.turn = "O" if self.turn == "X" else "X"
    
    def check_win(self):
        # صفوف
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return True
        # أعمدة
        for j in range(3):
            if self.buttons[0][j]["text"] == self.buttons[1][j]["text"] == self.buttons[2][j]["text"] != "":
                return True
        # أقطار
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True
        return False
    
    def reset(self):
        self.turn = "X"
        self.game_over = False
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
    
    def run(self):
        self.window.mainloop()

TicTacToe().run()