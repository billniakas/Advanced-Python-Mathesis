# PhotoImage 

import tkinter as tk
import random

class App():
    def __init__(self, root):
        self.root = root
        blue = '#3e719a'
        yellow = '#fddb6a'
        self.root.config(bg=random.choice([blue,yellow]))
        self.image1 = tk.PhotoImage(file="python_logo.gif")
        self.x = self.image1.width()
        self.y = self.image1.height()
        print(self.x, self.y)
        puzzle = []
        for i in range(5):
            for j in range(2):
                x1,y1 = int(i*self.x/5), int(j*self.y/2)
                x2,y2 = x1+int(self.x/5), y1+int(self.y/2)
                puzzle.append(self.subimage(x1,y1,x2,y2, self.image1))
        random.shuffle(puzzle)
        for n,im in enumerate(puzzle):
            if not n%5 :
                f = tk.Frame(self.root)
                f.pack(expand=True, fill='both')
            l = tk.Label(f, image=im, bg =random.choice([blue,yellow]))
            l.pack(side='left', padx=2, pady=2)
            l.image = im

    def subimage(self, x1,y1, x2,y2, spritesheet):
        dst = tk.PhotoImage()
        dst.tk.call(dst, 'copy', spritesheet, '-from', x1,y1, x2,y2, '-to', 0, 0)
        return dst

root = tk.Tk()
App(root)
root.mainloop()
