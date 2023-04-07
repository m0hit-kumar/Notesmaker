import tkinter as tk
import webbrowser
import os
from PIL import Image, ImageTk
from recorder_ui import recorder


def open_pdf(event, filename):
    cd = os.getcwd()
    print(cd + "/pdf_files/" + filename)
    webbrowser.open_new(cd + "/pdf_files/" + filename)


def close_current():
    root.destroy()
    recorder()


root = tk.Tk()

# Creating four frames for the top row
frame1 = tk.Frame(root, width=400, height=300, bg="white")
frame1.grid(row=0, column=0, padx=0, pady=10)

frame2 = tk.Frame(root, width=400, height=300, bg="white")
frame2.grid(row=0, column=1, padx=0, pady=10)

start_button = tk.Button(frame1, text="Start", font=(
    "Helvetica", 36), bg="green", fg="white", command=close_current)
start_button.pack(fill=tk.BOTH, expand=True)

image = tk.PhotoImage(file="./images/pdf-1.png").subsample(3)

# Creating frames for second row dynamically
x = os.listdir("./pdf_files")
pdf_files = [i for i in x if i.endswith(".pdf")]

for i, pdf_file in enumerate(pdf_files):
    frame = tk.Frame(root, width=300, height=200, bg="white")
    frame.grid(row=1, column=i, padx=20, pady=10)

    label = tk.Label(frame, image=image)
    label.pack()

    label.bind("<Button-1>", lambda event,
               filename=pdf_file: open_pdf(event, filename))

    label_text = tk.Label(frame, text=f"Image {i+1}")
    label_text.pack()


root.mainloop()
