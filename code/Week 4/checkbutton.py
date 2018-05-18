
# Checkbutton

import tkinter as tk
class MyApp():
    def __init__(self, root):
        self.root = root
        self.color = '#66f0ff'
        self.widgets()
    def widgets(self):
        self.l = tk.Label(self.root, text='Επιλέξτε τα σπορ που σας αρέσουν: ',
                          font="Arial 18", bg=self.color)
        self.l.pack(fill='both', expand =1)
        self.answer1 = tk.StringVar()
        self.check1 = tk.Checkbutton(self.root, text='football ', command=self.check,
                        font="Arial 26", bg=self.color, variable=self.answer1, onvalue='football', offvalue='')
        self.check1.pack( side = 'left', fill = 'both', expand = 1)
        self.answer2 = tk.StringVar()
        self.check2 = tk.Checkbutton(self.root, text='basket ', command= self.check,
                        font="Arial 26",bg=self.color, variable=self.answer2, onvalue='basket', offvalue='')
        self.check2.pack( side = 'left', fill = 'both', expand = 1)
        self.count = 0
    def check(self):
        print('Έχουν επιλεγεί: ', self.answer1.get(), self.answer2.get())

root = tk.Tk()
myapp = MyApp(root)
root.mainloop()


