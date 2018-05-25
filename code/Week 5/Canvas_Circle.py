# Ανάδραση σε επιλογή κύκλου

'''
Να ζωγραφήσετε 100 τυχαίους κόκκινους κύκλους ακτίνας 10 pixel. Όταν επιλέγεται ένας από
τους κύκους να αντιδρά αλλάζοντας χρώμα.
'''

import tkinter as tk
import random

class App():
    def __init__(self, root):
        self.root = root
        self.root.title('canvas_1')
        self.canvas = tk.Canvas(self.root, width=600, height=600, bg='lightblue')
        self.canvas.pack()
        radius=10
        for i in range(100): #100 κύκλοι διάμετρου radius
            x, y = random.randint(radius, 600 - radius), random.randint(radius, 600 - radius)
            self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="red")
        self.canvas.bind('<1>', self.click)
        self.canvas.bind('', self.back)
    def click(self, event):
        if self.canvas.find_withtag('current'):
            self.canvas.itemconfig('current', fill="blue")
    def back(self, event):
        if self.canvas.find_withtag('current'):
            self.canvas.itemconfig('current', fill="red")

root = tk.Tk()
App(root)
root.mainloop()

