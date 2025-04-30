import tkinter as tk

def clear():
    entry.delete(0, tk.END)

window = tk.Tk()

window.geometry("1000x1000")

entry = tk.Entry(window)
entry.grid(row=0, column=0, padx=20, pady=20)



allowed_chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/', ' ']

def equals_click():
    user_inp = entry.get()
    
    if not user_inp:
        raise Exception("User input must not be empty!")

    for char in user_inp:
        if char not in allowed_chars:
            raise Exception("Invalid arithmetic detected. Please change input.")

    try:
        res = eval(user_inp)
    except ZeroDivisionError:
        print("Dividing by zero is not allowed. plz try again.")
    else:
        if isinstance(res, float):
            res = round(res, 3)

        clear()
        entry.insert(0, res)



equals = tk.Button(window, text='=', command=equals_click)
clear_button = tk.Button(window, text='C', command=clear)

equals.grid(row=5, column=0)
clear_button.grid(row=6, column=0)


window.mainloop()