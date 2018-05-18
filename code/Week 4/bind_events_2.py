
# Events παράδειγμα 2

import tkinter as tk
class MyApp ():
    def __init__(self, root):
        self.root = root
        root.title("Παράδειγμα 8: γεγονότα")
        root.geometry("400x300+300+300")
        self.create_widgets()
    def create_widgets(self):
        self.l = tk.Label(self.root, text='', font = 'Arial 40')
        self.l.pack(expand=True, fill='both')
        self.l.bind("", lambda e:self.l.config(text='Έχει μπει'))
        self.l.bind("", lambda e: self.l.config(text='Έχει βγει'))
def main():
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
if __name__ == '__main__': main()

