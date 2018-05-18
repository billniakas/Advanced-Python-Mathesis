# Dialogues

import tkinter as tk
from tkinter import messagebox, colorchooser, filedialog, simpledialog
class App():
    def __init__(self, root):
        self.root = root
        self.root.geometry('400x400+200+200')
        self.widgets()
    def widgets(self):
        self.current_color = "#6A9662"
        self.f = tk.Frame(self.root)
        self.f.pack(expand=True, fill = 'both')
        self.b1 = tk.Button(text='πληροφορία', font='Arial 48')
        self.b1.pack(side= 'top', expand=True, fill = 'both')
        self.b1.bind('', self.showinfo)
        self.b2 = tk.Button(text='άνοιγμα αρχείου', font='Arial 48')
        self.b2.pack(side='top', expand=True, fill='both')
        self.b2.bind('', self.file)
        self.b3 = tk.Button(text='χρώμα', font='Arial 48')
        self.b3.pack(side='top', expand=True, fill='both')
        self.b3.bind('', self.color)
        self.b4 = tk.Button(text='δώσε τιμές', font='Arial 48')
        self.b4.pack(side='top', expand=True, fill='both')
        self.b4.bind('', self.ask_value)
    def ask_value(self, event):
        ans = simpledialog.askstring("Title", "Το όνομά σας:")
        print(ans)
        ans = simpledialog.askinteger("Dialog Title", "Δώστε ένα ακέραιο")
        print(ans)
        ans = simpledialog.askinteger("Num", "τιμή μεταξύ 0 και 100",
                                      minvalue=0, maxvalue=100)
        print(ans)


    def color(self, event):
        print('color', event)
        result = colorchooser.askcolor(color=self.current_color, title="Colour Chooser")
        print(result)
        self.current_color = result[-1]
    def file(self, event):
        name = filedialog.askopenfilename()
        print(name)
    def showinfo(self, event):
        messagebox.showinfo('info',
                            'πάτησες στη θέση {},{}'.format(event.x, event.y))
root = tk.Tk()
App(root)
root.mainloop()

