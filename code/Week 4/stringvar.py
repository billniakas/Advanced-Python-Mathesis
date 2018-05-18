
# StringVar

import tkinter as tk
class MyApp():
    def __init__(self, root):
        self.r = root
        self.myText = tk.StringVar()
        self.myText.set(30*' ')
        self.mylabel = tk.Label(self.r, textvariable = self.myText, width=30,
                                font="Arial 20")
        self.mylabel.pack(fill='both', expand=1)
        self.b = tk.Button(self.r, text="  button  ", font = "Arial 30",
                        bg="yellow", command=self.buttonPressed)
        self.b.pack(fill='both', expand=1)
        self.count = 0
    def buttonPressed(self):
        self.count += 1
        if self.count == 1 : end =  'ά '
        else: end = 'ές'
        self.myText.set('Το πλήκτρο πατήθηκε ' + str(self.count) + ' φορ'+end)

root = tk.Tk()
myapp = MyApp(root)
root.mainloop()
