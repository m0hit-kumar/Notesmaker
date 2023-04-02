import tkinter as tk
from PIL import ImageGrab


def screenshot():
    image = ImageGrab.grab()
    image.save("./screenshot/screenshot.png")


window = tk.Tk()

window.title("Sample Window")
window.overrideredirect(True)
window.wm_attributes("-topmost", True)
window.title("Text Display")

window.geometry("200x50")

icons_frame = tk.Frame(window, padx=10, pady=10)
icons_frame.pack()

canvas = tk.Canvas(icons_frame, width=20, height=20)
canvas.pack(side=tk.LEFT)
canvas.create_oval(5, 5, 15, 15, fill="red")

ss_button = tk.Button(icons_frame, text="Screenshot", command=screenshot)
ss_button.pack(side=tk.LEFT)

stop_button = tk.Button(icons_frame, text="Stop", command=window.quit)
stop_button.pack(side=tk.LEFT)

window.mainloop()
