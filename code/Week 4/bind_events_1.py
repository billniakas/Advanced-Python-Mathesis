# Events παράδειγμα 1

import tkinter as tk
class MyApp ():
    def __init__(self, root):
        self.root = root
        root.title("Παράδειγμα 1: γεγονότα")
        self.create_widgets()
    def create_widgets(self):
        self.f = tk.Frame(self.root, width=300, height=300,
                          borderwidth=10, bg='lightblue')
        self.f.pack(expand=True, fill='both')
        self.f.bind("", lambda event: print('2 click at', event.x, event.y))
        self.f.bind("", lambda event: print('1 click at', event.x, event.y))
def main():
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
if __name__ == '__main__': main()
