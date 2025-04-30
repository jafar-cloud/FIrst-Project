import tkinter as tk

window = tk.Tk()
window.geometry("1000x1000")


label = tk.Label(window, text="Enter name:")
label.pack()

entry = tk.Entry(window)
entry.pack()

label2 = tk.Label(window, text="Gender")
label2.pack()

gender = tk.StringVar()
gender.set(None)

radiobutton1 = tk.Radiobutton(window, text="Male", value="male", variable=gender)
radiobutton1.pack()

radiobutton2 = tk.Radiobutton(window, text="Female", value="female", variable=gender)
radiobutton2.pack()

label3 = tk.Label(window, text="Write feedback:")
label3.pack()

text_area = tk.Text(window, width=90, height=30)
text_area.pack()

def on_click():
    user_name = entry.get()
    user_gender = gender.get()
    print(user_name)
    print(gender.get())
    print(text_area.get(1.0, tk.END))


button = tk.Button(window, text="Submit", command=on_click)
button.pack()

print(entry.get())

tk.mainloop()