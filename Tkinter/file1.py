import tkinter as tk


window = tk.Tk()

window.title("Hello, World")

window.geometry("400x400")

label = tk.Label(window, text="This is my first TKinter project.")

label.pack()

button = tk.Button(window, text="Click Me")
button.pack()

frame = tk.Frame(window)
frame.pack()

window.mainloop()
