import tkinter as tk


window = tk.Tk()

listbox = tk.Listbox(window, width=30, height=10)
listbox.pack()

window.geometry("1000x1000")

text = tk.Text(window, width=30, height=30)

text.pack()

i = 1

def on_add_click():
    global i 
    task = text.get(1.0, tk.END)

    if task == '\n':
        raise ValueError("Task cannot be empty.")
    
    listbox.insert(i, task)
    i += 1


def on_delete_click():
    selected = listbox.curselection()
    
    if not selected:
        raise Exception("Cannot delete without selecting.")
    
    listbox.delete(selected)


def on_clear_all_click():
    listbox.delete(0, tk.END)

def on_complete_click():
    selected = listbox.curselection()
    
    if not selected:
        raise Exception("Cannot complete a task without selecting.")
    
    listbox.delete(selected)
    selected = str(selected) + "(Done)"
    listbox.insert(0, selected)


add_button = tk.Button(window, text="Add", command=on_add_click)
add_button.pack()

delete_button = tk.Button(window, text="Delete", command=on_delete_click)
delete_button.pack()

clear_all_button = tk.Button(window, text="Clear All", command=on_clear_all_click)
clear_all_button.pack()

complete_button = tk.Button(window, text="Completed Task", command=on_complete_click)
complete_button.pack()

window.mainloop()