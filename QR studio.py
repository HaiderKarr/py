from tkinter import filedialog
import qrcode
from tkinter import *
from PIL import Image, ImageTk

def generate_qr():
    global tk_img 
    data = entry.get() 

    if data != "":
        qr = qrcode.make(data)
        qr.save("qr_temp.png")
        
        
        img = Image.open("qr_temp.png")
        img = img.resize((200, 200))
        tk_img = ImageTk.PhotoImage(img) 
        
        qr_label.config(image=tk_img) 

def save_qr():
    file = filedialog.asksaveasfilename(defaultextension=".png",
                                      filetypes=[("PNG file", "*.png")])
    if file:
        qr = qrcode.make(entry.get())
        qr.save(file)

root = Tk()
root.title("QR Studio") 
root.geometry("450x600") 
root.config(bg="#0f172a")

title_label = Label(root, text="QR Generator", 
              font=("Arial", 22, "bold"),
              fg="white", bg="#0f172a")
title_label.pack(pady=10)

entry = Entry(root, font=("Arial", 14), width=25)
entry.pack(pady=10) 

preview = Label(root, text="Preview",
                fg="white", bg="#0f172a")
preview.pack()

qr_label = Label(root, bg="#0f172a")
qr_label.pack(pady=10)

generate_btn = Button(root,
                      text="Generate QR", 
                      bg="green", fg="white",
                      font=("Arial", 12),
                      command=generate_qr) 
generate_btn.pack(pady=5)

save_btn = Button(root,
                  text="Save Image", 
                  bg="blue", fg="white",
                  command=save_qr)
save_btn.pack(pady=5)

root.mainloop()