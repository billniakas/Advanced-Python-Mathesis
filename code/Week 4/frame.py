import tkinter as tk
class MyApp(tk.Frame):
    def __init__(self, root):
        self.root =root
        root.title('Παράδειγμα Frames')
        root.resizable(False, False)
        myfont = 'Arial 30'
        #Πρώτο πλαίσιο Frame
        self.f1 = tk.LabelFrame(root, text='Frame1')
        self.f1.pack(fill = 'both', expand=True, side='top', padx=5,pady=5)
        red = tk.Label(self.f1, text=' Red ', font=myfont, bg="red")
        red.pack(fill = 'both', expand=1, side='left')
        blue = tk.Label(self.f1, text='Blue ', font=myfont, bg='blue')
        blue.pack(fill = 'both', expand=1, side='left')
        green = tk.Label(self.f1, text='Green', font=myfont, bg='green')
        green.pack(fill = 'both', expand=1, side='left')
        # Δεύτερο πλαίσιο Frame
        self.f2 = tk.LabelFrame(root, text='Frame2')
        self.f2.pack(side='bottom', fill='both', expand=1, padx=5, pady=5)
        yellow = tk.Label(self.f2, text='Yellow', font=myfont, bg='yellow')
        yellow.pack(expand=1, fill='both')
root = tk.Tk()
MyApp(root)
root.mainloop()
