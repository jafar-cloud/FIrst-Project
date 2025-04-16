from pytube import YouTube
from pytube.exceptions import RegexMatchError
import tkinter as tk

window = tk.Tk()

window.geometry('800x800')

label = tk.Label(window, text="Paste the link here")
label.pack()

entry = tk.Entry(window)
entry.pack()


def on_click():
    print(entry.get())
    
    try:
        yt = YouTube(entry.get())
    except RegexMatchError:
        print("Invalid link.")
    else:
        stream = yt.streams.get_highest_resolution()
        stream.download()
        print("Downloaded.")


button = tk.Button(window, text="Submit", command=on_click)
button.pack()

print()


window.mainloop()