# Radiobutton

import tkinter as tk
class App():
    def __init__(self, w):
        self.v = tk.IntVar()
        sel = [('Μονόκλινο',1), ('Δίκλινο',2),('Τρίκλινο',3)]
        for t,val in sel:
            tk.Radiobutton(w,text=t, font=('Arial', 30),
                           variable=self.v, fg= 'blue',
                           value=val, command=self.handle,
                           padx=5, pady=5).pack(anchor='w')
    def handle(self):
        print(self.v.get())
w=tk.Tk()
App(w)
w.mainloop()
