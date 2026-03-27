import tkinter as tk
import random

# --- إعدادات اللعبة ---
WIDTH = 600
HEIGHT = 600
GRID_SIZE = 20
INITIAL_SPEED = 150  # السرعة عند البداية (ميلي ثانية)

class SnakeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("🐍 لعبة الثعبان المطورة")
        self.window.resizable(False, False)
        
        # إنشاء Canvas
        self.canvas = tk.Canvas(
            self.window, 
            width=WIDTH, 
            height=HEIGHT, 
            bg="#1a1a2e",
            highlightthickness=0
        )
        self.canvas.pack()
        
        # لوحة النتيجة
        self.score_label = tk.Label(
            self.window,
            text="النتيجة: 0  |  السرعة: 1",
            font=("Arial", 18, "bold"),
            bg="#16213e",
            fg="white",
            padx=20,
            pady=10
        )
        self.score_label.pack(fill=tk.X)
        
        # متغيرات اللعبة
        self.score = 0
        self.current_speed = INITIAL_SPEED
        self.direction = "Right"
        self.game_running = False
        self.snake = []
        self.food = None
        
        # التحكم بلوحة المفاتيح
        self.window.bind("<KeyPress>", self.on_key_press)
        
        # رسم الشبكة الخلفية
        self.draw_grid()
        
        # زر البدء
        self.start_button = tk.Button(
            self.window,
            text="🎮 ابدأ التحدي",
            font=("Arial", 16, "bold"),
            bg="#e94560",
            fg="white",
            command=self.start_game,
            padx=30,
            pady=10,
            cursor="hand2",
            activebackground="#ff4d6d"
        )
        self.start_button.pack(pady=10)
        
    def draw_grid(self):
        for i in range(0, WIDTH, GRID_SIZE):
            self.canvas.create_line(i, 0, i, HEIGHT, fill="#1f2f4f", width=1)
        for i in range(0, HEIGHT, GRID_SIZE):
            self.canvas.create_line(0, i, WIDTH, i, fill="#1f2f4f", width=1)
    
    def start_game(self):
        self.game_running = True
        self.score = 0
        self.current_speed = INITIAL_SPEED
        self.score_label.config(text=f"النتيجة: {self.score}  |  السرعة: 1")
        self.start_button.config(state="disabled")
        self.canvas.delete("game_over")
        
        # إعداد الثعبان (الرأس في المنتصف)
        self.snake = [(WIDTH//2, HEIGHT//2), 
                      (WIDTH//2 - GRID_SIZE, HEIGHT//2),
                      (WIDTH//2 - 2*GRID_SIZE, HEIGHT//2)]
        self.direction = "Right"
        
        self.create_food()
        self.game_loop()
    
    def create_food(self):
        """توليد الطعام مع التأكد أنه لا يظهر فوق جسم الثعبان"""
        while True:
            x = random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
            y = random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
            self.food = (x, y)
            if self.food not in self.snake:
                break
        
        self.canvas.delete("food")
        self.canvas.create_oval(
            x + 3, y + 3,
            x + GRID_SIZE - 3, y + GRID_SIZE - 3,
            fill="#00ff41", # لون أخضر فسفوري للطعام
            outline="white",
            tags="food"
        )

    def on_key_press(self, event):
        key = event.keysym
        if key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"
    
    def game_loop(self):
        if not self.game_running:
            return
        
        # حساب موقع الرأس الجديد
        head_x, head_y = self.snake[0]
        if self.direction == "Up": head_y -= GRID_SIZE
        elif self.direction == "Down": head_y += GRID_SIZE
        elif self.direction == "Left": head_x -= GRID_SIZE
        elif self.direction == "Right": head_x += GRID_SIZE
        
        new_head = (head_x, head_y)

        # التحقق من الاصطدام بالحواف أو الجسم
        if (head_x < 0 or head_x >= WIDTH or
            head_y < 0 or head_y >= HEIGHT or
            new_head in self.snake):
            self.game_over()
            return
        
        self.snake.insert(0, new_head)
        
        # التحقق من أكل الطعام
        if new_head == self.food:
            self.score += 10
            # زيادة السرعة: تقليل وقت الانتظار بمقدار 2ms مع كل أكلة (بحد أدنى 50ms)
            if self.current_speed > 50:
                self.current_speed -= 3
            
            level = (INITIAL_SPEED - self.current_speed) // 5 + 1
            self.score_label.config(text=f"النتيجة: {self.score}  |  المستوى: {int(level)}")
            self.create_food()
        else:
            self.snake.pop()
        
        self.draw_elements()
        self.window.after(self.current_speed, self.game_loop)
    
    def draw_elements(self):
        """رسم كل العناصر وتحديث الطبقات"""
        self.canvas.delete("snake")
        for i, (x, y) in enumerate(self.snake):
            color = "#e94560" if i == 0 else "#533483" # رأس أحمر وجسم بنفسجي
            self.canvas.create_rectangle(
                x + 1, y + 1, x + GRID_SIZE - 1, y + GRID_SIZE - 1,
                fill=color, outline="#16213e", tags="snake"
            )
        # التأكد أن الطعام يظهر دائماً في المقدمة
        self.canvas.tag_raise("food")
    
    def game_over(self):
        self.game_running = False
        self.start_button.config(state="normal", text="🔄 حاول مرة أخرى")
        self.canvas.create_text(
            WIDTH // 2, HEIGHT // 2,
            text=f"GAME OVER\nالنتيجة النهائية: {self.score}",
            font=("Arial", 35, "bold"),
            fill="#e94560",
            justify="center",
            tags="game_over"
        )

if __name__ == "__main__":
    game = SnakeGame()
    game.window.mainloop()