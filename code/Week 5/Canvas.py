# Εισαγωγή στο γραφικό υποδοχέα Canvas

import tkinter as tk

class App():
    def __init__(self, root):
        self.root = root
        self.root.title('canvas_1')
        self.canvas = tk.Canvas(self.root, width=400, height=600, bg='lightblue')
        self.canvas.pack()
        self.canvas.create_oval(10, 10, 100, 100, fill='orange') # πορτοκαλί κύκλος
        self.canvas.create_line(105, 450, 380, 580, fill="red", dash=(4, 4), width=5) # κόκκινη γραμμή
        self.canvas.create_rectangle(205, 10, 300, 105, outline='white', fill='lightgreen') # πράσινο κουτί
        xy = 10, 110, 100, 200
        self.canvas.create_arc(xy, start=0, extent=270, fill='yellow') # τόξο κύκλου
        self.canvas.create_polygon(205, 105, 285, 125, 166, 177, 210, 199, 205, 105, fill='red') # πολύγωνο
        self.canvas.create_text(250, 450, text='κείμενο', fill='blue', font='Arial 44') #κείμενο
        self.canvas.img = tk.PhotoImage(file='walking.gif')
        self.canvas.create_image(10, 350, image=self.canvas.img, anchor='nw') #εικόνα
        frm = tk.Frame(self.canvas, relief='groove', borderwidth=2)
        tk.Label(frm, text= self.insert_quote(), bg='lightyellow').pack()
        self.canvas.create_window(10, 250, window=frm, anchor='nw') #παράθυρο μέσα στον καμβά
        self.canvas.bind('<1>', self.move_all)
        self.canvas.bind('<2>', self.move_back)
    def move_all(self, event):
        for i in self.canvas.find_all(): self.canvas.move(i, 10, 0)
    def move_back(self, event):
        for i in self.canvas.find_all(): self.canvas.move(i, -10, 0)
    def insert_quote(self):
        return '''Η Τσακωνική διάλεκτος
Η Τσακωνική διάλεκτος είναι ελληνογενής
διαλεκτική ομάδα που μιλιέται στην περιοχή
της νότιας Κυνουρίας της Αρκαδίας.'''

root = tk.Tk()
App(root)
root.mainloop()
