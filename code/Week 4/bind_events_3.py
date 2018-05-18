# Events παράδειγμα 3

import tkinter as tk

class MyApp ():
    def __init__(self, root):
        self.root = root
        root.title("Example 7: detecting events")
        root.geometry("400x300+300+300")
        self.create_widgets()

    def create_widgets(self):
        self.root.bind("", self.handler)
        self.root.bind("", self.focus)
        self.myText = tk.StringVar()
        self.mylabel = tk.Label(self.root, textvariable=self.myText,
                                font="Arial 30",bg="yellow")
        self.mylabel.pack(fill='both', expand=1)

    def handler(self, event):
        print("πατήθηκε: "+repr(event.char))
        self.myText.set( "πατήθηκε: "+str(event.char)+'\nκωδικός:{}'.format(ord(event.char)))
    def focus(self, event):
        self.root.focus_set()
        print ("clicked at", event.x, event.y)
        self.myText.set( "κλικ σε: " + str(event.x) + "," + str(event.y))

def main():
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()

main()
