# Παραδείγματα με την pack

import tkinter as tk
class MyApp():
    def __init__(self, root):
        root.geometry('100x100+200+200')
        tk.Label(root, text='Label', bg='green').pack()
        tk.Label(root, text='Label2', bg='red').pack()
        # case 1
        w1 = tk.Toplevel()
        w1.geometry('100x100+300+200')
        tk.Label(w1, text='Label', bg='green').pack(expand=1, fill ='y')
        tk.Label(w1, text='Label2', bg='red').pack(fill = 'both')
        # case 2
        w2 = tk.Toplevel()
        w2.geometry('100x100+400+200')
        tk.Label(w2, text='Label', bg='green').pack(expand=1)
        tk.Label(w2, text='Label2', bg='red').pack(fill = 'both')
        # case 3
        w3 = tk.Toplevel()
        w3.geometry('100x100+500+200')
        tk.Label(w3, text='Label', bg='green').pack(fill='both', expand=1, side='left')
        tk.Label(w3, text='Label2', bg='red').pack(fill='both', expand=1, side='right')
        # case 4
        w4 = tk.Toplevel()
        w4.geometry('100x100+600+200')
        tk.Label(w4, text='Label', bg='green').pack(fill = 'both', expand=1)
        tk.Label(w4, text='Label2', bg='red').pack(fill = 'both', expand=1)
root = tk.Tk()
MyApp(root)
root.mainloop()
