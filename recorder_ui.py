import tkinter as tk
from PIL import ImageGrab
from audio_recorder import start_recording, stop_recording


def screenshot():
    image = ImageGrab.grab()
    image.save("./screenshot/screenshot.png")


def recorder():

    window = tk.Tk()

    window.title("Sample Window")
    window.overrideredirect(True)
    window.wm_attributes("-topmost", True)
    window.title("Text Display")

    window.geometry("250x50")

    icons_frame = tk.Frame(window, padx=10, pady=10)
    icons_frame.pack()

    canvas = tk.Canvas(icons_frame, width=20, height=20)
    canvas.pack(side=tk.LEFT)
    canvas.create_oval(5, 5, 15, 15, fill="red")

    # start_button = tk.Button(icons_frame, text="Start",
    #                          command=start_recording)

    start_button = tk.Button(icons_frame, text="Start",
                             )
    start_button.pack(side=tk.LEFT)

    ss_button = tk.Button(icons_frame, text="Screenshot", command=screenshot)
    ss_button.pack(side=tk.LEFT)

    close_button = tk.Button(icons_frame, text="Stop", command=stop_recording)
    close_button.pack(side=tk.LEFT)

    quit_button = tk.Button(icons_frame, text="Close", command=window.quit)
    quit_button.pack(side=tk.LEFT)

    window.mainloop()
