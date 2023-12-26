import tkinter as tk
import random
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry('340x340')
window.config(bg='#4f3d57')

def roll():
    result = random.randrange(1, 7)
    label_result.config(text=f"Result: {result}")

    image_path = f'{result}.png'
    dice_image = Image.open(image_path).convert('RGBA')
    dice_image = dice_image.resize((180, 180))  # Resize the image if needed
    dice_image = ImageTk.PhotoImage(dice_image)
    dice_label.config(image=dice_image)
    dice_label.image = dice_image

button = tk.Button(window,
                   text='Roll the dice',
                   command=roll,
                   font=('Times New Roman', 16),
                   bg='#a584b3',
                   fg='white')

button.pack(pady=20)

dice_label = tk.Label(window,
                      bg='#4f3d57')
dice_label.pack()

label_result = tk.Label(window,
                        text="",
                        font=('Times New Roman', 16),
                        bg='#4f3d57',
                        fg='white')

label_result.pack(pady=20)

window.mainloop()

