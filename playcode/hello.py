from tkinter import Tk, ttk

root = Tk()
label = ttk.Label(root, text='Hello World!')
label.pack()
label.config(foreground='blue', background='yellow')
label.config(font = ('Myriad Pro', 20, 'bold'))
root.mainloop()
