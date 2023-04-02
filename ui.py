import tkinter as tk
import webbrowser


def open_pdf(event):
    webbrowser.open_new("Os.pdf")


def open_pdf2(event):
    webbrowser.open_new("idea.pdf")


root = tk.Tk()

# Creating four frames for the top row
frame1 = tk.Frame(root, width=400, height=300, bg="white")
frame1.grid(row=0, column=0, padx=0, pady=10)

frame2 = tk.Frame(root, width=400, height=300, bg="white")
frame2.grid(row=0, column=1, padx=0, pady=10)


frame3 = tk.Frame(root, width=300, height=300, bg="orange")
frame3.grid(row=0, column=2, padx=10, pady=10)

frame4 = tk.Frame(root, width=300, height=300, bg="red")
frame4.grid(row=0, column=3, padx=10, pady=10)

frame5 = tk.Frame(root, width=280, height=300, bg="blue")
frame5.grid(row=0, column=4, padx=10, pady=10)


image = tk.PhotoImage(file="pdf-1.png").subsample(3)

# Creating frames for second row
frame6 = tk.Frame(root, width=300, height=200, bg="white")
frame6.grid(row=1, column=0, padx=20, pady=50)

label6 = tk.Label(frame6, image=image)
label6.pack()

label6.bind("<Button-1>", open_pdf)

label_text6 = tk.Label(frame6, text="Image 1")
label_text6.pack()

frame7 = tk.Frame(root, width=300, height=200, bg="white")
frame7.grid(row=1, column=1, padx=20, pady=10)

label7 = tk.Label(frame7, image=image)
label7.pack()

label7.bind("<Button-1>", open_pdf2)

label_text7 = tk.Label(frame7, text="Image 2")
label_text7.pack()

frame8 = tk.Frame(root, width=300, height=200, bg="white")
frame8.grid(row=1, column=2, padx=20, pady=10)

label8 = tk.Label(frame8, image=image)
label8.pack()

label_text8 = tk.Label(frame8, text="Image 3", font=("Helvetica", 16, "bold"))
label_text8.pack()

frame9 = tk.Frame(root, width=300, height=200, bg="white")
frame9.grid(row=1, column=3, padx=20, pady=10)

label9 = tk.Label(frame9, image=image)
label9.pack()

label_text9 = tk.Label(frame9, text="Image 4")
label_text9.pack()

frame10 = tk.Frame(root, width=280, height=200, bg="white")
frame10.grid(row=1, column=4, padx=20, pady=10)

label10 = tk.Label(frame10, image=image)
label10.pack()

label_text10 = tk.Label(frame10, text="Image 5")
label_text10.pack()

# Creating frames for third row
frame11 = tk.Frame(root, width=300, height=200, bg="white")
frame11.grid(row=2, column=0, padx=20, pady=10)

label11 = tk.Label(frame11, image=image)
label11.pack()

label_text11 = tk.Label(frame11, text="Image 6")
label_text11.pack()


frame12 = tk.Frame(root, width=300, height=200, bg="white")
frame12.grid(row=2, column=1, padx=20, pady=10)
label12 = tk.Label(frame12, image=image)
label12.pack()


frame13 = tk.Frame(root, width=300, height=200, bg="white")
frame13.grid(row=2, column=2, padx=20, pady=10)

label13 = tk.Label(frame13, image=image)
label13.pack()

frame14 = tk.Frame(root, width=300, height=200, bg="white")
frame14.grid(row=2, column=3, padx=20, pady=10)

label14 = tk.Label(frame14, image=image)
label14.pack()

frame15 = tk.Frame(root, width=280, height=200, bg="white")
frame15.grid(row=2, column=4, padx=20, pady=10)

# Create a label within the frame and set the image
label15 = tk.Label(frame15, image=image)
label15.pack()

label_text15 = tk.Label(frame15, text="OPEN THIS PDF")
label_text15.pack()


root.mainloop()
