# Πολλά παράθυρα με την Toplevel

import tkinter as tk
import random
class MyApp():
    def __init__(self, root):
        big_font ='Arial 80'
        screen_x = root.winfo_screenwidth()
        screen_y = root.winfo_screenheight()
        # random colors
        self.r = lambda: random.randint(0, 255) # τυχαίος αριθμός από 0..255
        root.geometry('200x200+100+100')
        l = tk.Label(root, text='0', bg='black', fg='white', font=big_font)
        l.pack(expand=True, fill = 'both')
        for i in range(50):
            x= random.randint(0, screen_x - 200)
            y= random.randint(0, screen_y - 200)
            w = tk.Toplevel() # άλλα παράθυρα
            w.geometry('200x200+{}+{}'.format(x,y))
            l = tk.Label(w, text=str(i+1), font=big_font, bg = self.random_colour())
            l.pack(expand=True, fill = 'both')
    def random_colour(self):
        return '#{:02X}{:02X}{:02X}'.format(self.r(), self.r(), self.r())
root = tk.Tk() # βασικό παράθυρο
MyApp(root)
root.mainloop()
