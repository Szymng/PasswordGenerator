import tkinter as tk
from generator import generate

window = tk.Tk()
window.title('Password Generator')
window.minsize(300, 200)

text = tk.Text(window, height='2', width='20')
text.pack()
text.insert(tk.END, 'Click generate')


def on_clicked():
    temp = generate()
    text.delete(1.0, 'end')
    text.insert(tk.END, temp)


button = tk.Button(window, text='Generate', command=on_clicked)
button.pack()

window.mainloop()