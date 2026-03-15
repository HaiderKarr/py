import tkinter as tk
from tkinter import messagebox

def process_logic(text, shift, is_arabic, mode):
    if mode == 'decrypt':
        shift = -shift
    result = ""
    for char in text:
        if is_arabic and '\u0621' <= char <= '\u064A':
            start_pos = ord('\u0621')
            new_char = chr((ord(char) - start_pos + shift) % 28 + start_pos)
            result += new_char
        elif char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char
    return result

def run_action(mode):
    text = entry_text.get()
    try:
        shift = int(entry_shift.get())
        is_arabic = var_lang.get() == 1
        res = process_logic(text, shift, is_arabic, mode)
        entry_result.delete(0, tk.END)
        entry_result.insert(0, res)
    except ValueError:
        messagebox.showerror("خطأ", "يرجى إدخال رقم صحيح للإزاحة")

# إعداد الواجهة
root = tk.Tk()
root.title("نظام التشفير السري الخاص")
root.geometry("450x400")

tk.Label(root, text="النص المراد معالجته:").pack(pady=5)
entry_text = tk.Entry(root, width=50, justify='right')
entry_text.pack()

tk.Label(root, text="مفتاح الإزاحة (الرقم السري):").pack(pady=5)
entry_shift = tk.Entry(root, width=10, justify='center')
entry_shift.pack()

var_lang = tk.IntVar(value=1)
tk.Radiobutton(root, text="اللغة العربية", variable=var_lang, value=1).pack()
tk.Radiobutton(root, text="English", variable=var_lang, value=2).pack()

# أزرار العمليات
frame_btns = tk.Frame(root)
frame_btns.pack(pady=20)

btn_enc = tk.Button(frame_btns, text="تشفير 🔒", command=lambda: run_action('encrypt'), bg="#d1ffd1", width=15)
btn_enc.pack(side=tk.LEFT, padx=5)

btn_dec = tk.Button(frame_btns, text="فك التشفير 🔓", command=lambda: run_action('decrypt'), bg="#ffd1d1", width=15)
btn_dec.pack(side=tk.LEFT, padx=5)

tk.Label(root, text="النتيجة:").pack()
entry_result = tk.Entry(root, width=50, justify='right', font=("Arial", 10, "bold"))
entry_result.pack(pady=5)

root.mainloop()