# Caveman

import tkinter as tk
import random
from tkinter import simpledialog
import os.path
import time

class Artifact():
    def __init__(self, canvas):
        self.canvas = canvas
        self.image = {'left':None, 'right':None}
        self.art = None
        while True: # όρισε αρχικά διανύσματα κίνησης
            self.direction_x = random.randint(-5,5)
            self.direction_y = random.randint(-5,5)
            if abs(self.direction_x)>=2 and abs(self.direction_y)>=2: break
        self.direction = 'right' if self.direction_x >= 0 else 'left' #μεταβλητή επιλογής εικόνας
        self.run = False
        self.speed = random.randint(5,10) # όρισε ταχύτητα ενημέρωσης, όσο μικρότερη τόσο πιο γρήγορα τρέχει
        # TODO η μεταβλητή self.speed μπορεί να παίρνει τιμές από μεταβλητό εύρος τιμών ανάλογα με βαθμό δυσκολίας
    def create_artifact(self): # τοποθετείται το αντικείμενο σε θέση που να μην υπάρχει άλλο αντικείμενο
        while True:
            x = random.randint(padx, width-10*padx)
            y = random.randint(pady, height-10*pady)
            self.art = self.canvas.create_image(x,y, image=self.image[self.direction], anchor='nw')
            if not self.hit_object(): break
            self.canvas.delete(self.art)
        self.run = True
    def move(self):
        self.canvas.move(self.art, self.direction_x , self.direction_y )
        coords= self.canvas.bbox(self.art)
        if coords: # έλεγχος για τα όρια του καμβά
            new_direction = False
            if coords[0] < margin : #αριστερή πλευρά
                self.direction_x = abs(self.direction_x)
                new_direction = True
            if coords[2] > width-margin: # δεξιά πλευρά
                self.direction_x = -abs(self.direction_x)
                new_direction = True
            if coords[1] < margin  : # πάνω πλευρά
                self.direction_y = abs(self.direction_y)
                new_direction =True
            if coords[3] > height-margin: # κάτω πλευρά
                self.direction_y = -abs(self.direction_y)
                new_direction = True
            if new_direction: self.set_direction()
            overlapped_objects = self.canvas.find_overlapping(*coords)
            detect_collision = True
            if len(overlapped_objects)>2: # if more than the obejct itself and the background image
                detect_collision = self.handlecollision(overlapped_objects)
            if detect_collision and self.run:
                root.after(self.speed, self.move)
    def handlecollision(self, t):
        pass # αυτή η συνάρτηση εξαρτάται από τη συμπεριφορά του artifact
    def set_direction(self): # αλλαγή εικόνας κατεύθυνσης
        if self.art and self.direction_x >= 0 and self.image['right']:
            self.direction = 'right'
            self.canvas.itemconfig(self.art, image=self.image['right'])
        elif self.art and self.direction_x <0 and self.image['left']:
            self.direction = 'left'
            self.canvas.itemconfig(self.art, image=self.image['left'])
    def stop(self):
        self.run= False
    def hit_object(self): # έλεγχος αν χτύπησε άλλο αντικείμενο του καμβά
        overlapping_items = self.canvas.find_overlapping(*self.canvas.bbox(self.art))
        #print('number of overlapping items=',len(overlapping_items) )
        return False if len(overlapping_items) <= 2 else True

class Mammooth(Artifact):
    remaining = 0
    @staticmethod
    def reset():
        Mammooth.remaining = 0
    def __init__(self, canvas):
        Artifact.__init__(self, canvas)
        self.image['right'] = tk.PhotoImage(file='media/mammoth_right.gif')
        self.image['left'] = tk.PhotoImage(file='media/mammoth_left.gif')
        Mammooth.remaining = Mammooth.remaining + 1
        self.create_artifact()
    def handlecollision(self, t):
        self.direction_x= -self.direction_x
        self.direction_y= -self.direction_y
        self.set_direction()
        if game.theman.the_man in t: # αν χτυπήθηκα από τον πρωτόγονο
            Mammooth.remaining = Mammooth.remaining - 1
            game.score.caught_mamooth()
            self.canvas.delete(self.art)
            game.theman.fat_caveman()
            self.canvas.after(1000, game.theman.back_to_normal)
            if Mammooth.remaining == 0:
                game.stop_game()
            return 0
        return 1

class Dragon(Artifact):
    def __init__(self, canvas):
        Artifact.__init__(self,canvas)
        self.image['right'] = tk.PhotoImage(file='media/dragon_right.gif')
        self.image['left'] = tk.PhotoImage(file='media/dragon_left.gif')
        self.create_artifact()
    def handlecollision(self, t):
        self.direction_x = -self.direction_x #TODO to check for better collision physics
        self.direction_y = -self.direction_y
        self.set_direction()
        if game.theman and game.theman.the_man in t and not (game.theman.in_hospital or
                game.theman.eating_mammooth): # αν χτύπησα τον πρωτόγονο ...
            game.theman.dead_caveman()
            self.canvas.after(1000, game.theman.back_to_normal)
            game.score.hit_by_dragon()
        return 1

class Caveman():
    def __init__(self, canvas):
        self.canvas = canvas
        self.caveman_right = tk.PhotoImage(file='media/caveman_right.gif')
        self.caveman_left = tk.PhotoImage(file='media/caveman_left.gif')
        self.fat_caveman_images = [ tk.PhotoImage(file='media/caveman_fat2.gif'),
                                    tk.PhotoImage(file='media/caveman_fat_left.gif') ]
        self.dead_caveman_image = tk.PhotoImage(file='media/caveman_dead.gif')
        # put gif image on canvas
        # pic's upper left corner (NW) on the canvas is at x,y
        self.the_man = self.canvas.create_image(80, 500, image=self.caveman_right, anchor='nw')
        self.in_hospital = False
        self.eating_mammooth = False
        self.dancing = 0
    def fat_caveman(self):
        self.canvas.itemconfig(self.the_man, image=self.fat_caveman_images[self.dancing%2])
        self.eating_mammooth = True
        self.dancing += 1
        if self.dancing < 5: self.canvas.after(50, self.fat_caveman)
    def dead_caveman(self):
        self.canvas.itemconfig(self.the_man, image=self.dead_caveman_image)
        self.in_hospital = True
    def back_to_normal(self):
        self.canvas.itemconfig(self.the_man, image=self.caveman_right)
        self.in_hospital = False
        self.eating_mammooth = False
        self.dancing = 0
    def moveright(self, event):
        self.canvas.itemconfig(self.the_man, image=self.caveman_right)
        x = self.canvas.bbox(self.the_man)
        #print(x)
        if x[2]<=width and game.run:
            self.canvas.move(self.the_man, 20, 0)
    def moveleft(self, event):
        self.canvas.itemconfig(self.the_man, image=self.caveman_left)
        x = game.canvas.bbox(game.theman.the_man)
        if x[0]> 0 and game.run:
            game.canvas.move(game.theman.the_man, -20, 0)
    def moveup(self,event):
        x = game.canvas.bbox(game.theman.the_man)
        if x[1]>0 and game.run:
            game.canvas.move(game.theman.the_man, 0, -20)
    def movedown(self,event):
        x = game.canvas.bbox(game.theman.the_man)
        if x[3] 0: self.score = 0
            game.stop_game()
        self.report()
    def report(self):
        game.thescore.set('Σκορ: ' + str(self.score))

class Game():
    def __init__(self, root, width, height):
        self.root = root
        self.root.title('Caveman εκδ. 1.0')
        self.root.resizable(False, False)
        self.items = []
        self._elapsedtime = 0.0
        self.widgets()
        self.run = False
        self._start = 0.0
        self.username = ''

    def widgets(self):
        thefont = 'Arial 24'
        bigfont = 'Arial 44'
        self.f1 = tk.Frame(self.root)
        self.f1.pack(side='top')
        self.thescore = tk.StringVar()
        self.thescore.set('Σκορ:    ')
        self.timestr = tk.StringVar()
        time_display = tk.Label(self.f1, fg='green', bg='black', font=thefont, textvariable=self.timestr, width = 10)
        self._set_time(self._elapsedtime)
        time_display.pack(side='left', fill='x', expand=False, pady=2, padx=2)
        tk.Label(self.f1, textvariable=self.thescore, font=thefont, fg='red', width=10).pack(side='left', fill='x')
        self.button_info = tk.Button(self.f1, text= '  [ i ]  ', font=thefont, command=self.info, width= 10)
        self.button_info.pack(side='right', fill='x')
        self.button_save_score = tk.Button(self.f1, text=' Αποθήκευση σκορ ', font=thefont, command=self.save_score, width = 20)
        self.button_save_score.pack(side='right', fill='x')
        self.button_save_score.configure(state='disabled')
        self.button_start = tk.Button(self.f1, text=' Νέο παιχνίδι ', font=thefont, command=self.start_game, width = 15)
        self.button_start.pack(side='right', fill='x')
        self.f2 = tk.Frame(self.root)
        self.f2.pack(side='top')
        self.canvas = tk.Canvas(self.f2, width=width, height=height, bg='lightyellow')
        self.canvas.pack()
        self.splash = tk.PhotoImage(file='media/start.gif')
        self.splash_screen = self.canvas.create_image(150, 100, image=self.splash, anchor='nw')
        self.f3 = tk.Frame(self.root)
        self.f3.pack(side='top')
        self.captured = tk.Canvas(self.f3, width = 500, height=100, bg = 'lightgreen')
        self.captured.pack(side='left')
        self.lives = tk.Canvas(self.f3, width = 500, height=100, bg = 'lightcyan')
        self.lives.pack(side='left')

    def start_game(self):
        self.run = True
        self.score = Score()
        self.canvas.delete(self.splash_screen)
        Mammooth.reset()
        for i in self.items: del (i)
        self.canvas.delete('all')
        self.jungle = tk.PhotoImage(file='media/jungle.gif')
        # put gif image on canvas
        # pic's upper left corner (NW) on the canvas is at x=50 y=10
        self.thejungle = self.canvas.create_image(0,0, image=self.jungle, anchor='nw')
        self.items = []
        self.cave_back = tk.PhotoImage(file='media/cave_back.gif')
        self.thecave_back = self.canvas.create_image(0, height - 120, image=self.cave_back, anchor='nw')
        self.theman = Caveman(self.canvas)
        self.cave = tk.PhotoImage(file='media/cave.gif')
        self.thecave_back = self.canvas.create_image(0, height-120, image=self.cave, anchor='nw')
        # φόρτωσε μαμούθ
        for i in range(5):
            self.items.append(Mammooth(self.canvas))
        # φόρτωσε δράκους
        for i in range(5):
            self.items.append(Dragon(self.canvas))
        self.score.report()
        for i in self.items:
            i.move()
        root.bind('', self.theman.moveleft)
        root.bind('', self.theman.moveright)
        root.bind('', self.theman.moveup)
        root.bind('', self.theman.movedown)
        self.button_start.configure(state='disabled')
        self.start_timer()

    def stop_game(self):
        self.stop_timer()
        for i in self.items:
            i.stop()
        self.run = False
        self.button_save_score.configure(state='normal')
        self.button_start.configure(state='normal')

    def save_score(self):
        if not self.username:
            self.username = simpledialog.askstring('Όνομα χρήστη', 'Δώσε το όνομά σου:')
        if self.username:
            openfile = 'a' if os.path.isfile('hall_of_fame.txt') else 'w'
            with open('hall_of_fame.txt', openfile, encoding= 'utf-8') as f:
                f.write(self.username+';'+str(self.score.score)+';'+self._set_time(self._elapsedtime)+'\n')
                print(self.username+';'+str(self.score.score)+';'+self._set_time(self._elapsedtime)+'\n')
            self.button_save_score.configure(state='disabled')

    def retrieve_sorted_scores(self):
        the_famous = []
        if os.path.isfile('hall_of_fame.txt'):
            for line in open('hall_of_fame.txt', 'r', encoding='utf-8'):
                the_famous.append(line.strip().split(';'))
            for x in the_famous:  # reverse time in order to sort by multiple keys
                x.append(- (int(x[2].split(':')[0]) * 60 + int(x[2].split(':')[1])))
            the_famous = sorted(the_famous, key=lambda x: (x[1], x[3]), reverse=True)
            out = ''
            for n,f in enumerate(the_famous):
                out += f[0] + '\tscore:' + f[1] + '\ttime:' + f[2] + '\n'
                if n == 10: break
            return out
        return ''

    def info(self):
        message='''
        Πατήστε τα βελάκια για να κινήσετε τον πρωτόγονο έξω από τη σπηλιά του
        Κυνηγήστε τα μαμούθ! αξίζουν 100 πόντους το καθένα, αποφύγετε τους δράκους
        που κάθε χτύπημα τους στοιχίζει 50 πόντους.
        Ο πρωτόγονός σας αντέχει ως το πολύ 5 χτυπήματα.
        '''
        famous = self.retrieve_sorted_scores()
        if famous.strip():
            message += '\n\nTα ως τώρα υψηλότερα σκορ είναι:\n'+famous
        simpledialog.messagebox.showinfo("Τρωγλοδύτης v.1 Οδηγίες - Σκορ",message)

    def _set_time(self, elap):
        """ Όρισε με μορφή Minutes:Seconds το StringVar timestr """
        minutes = int(elap / 60)
        seconds = int(elap - minutes * 60.0)
        self.timestr.set('%02d:%02d' % (minutes, seconds))
        return '%02d:%02d' % (minutes, seconds)
    def _update_timer(self):
        """ Ανανέωσε το label with με τον χρόνο που έχει περάσει. """
        self._elapsedtime = time.time() - self._start
        self._set_time(self._elapsedtime)
        self._timer = self.root.after(200, self._update_timer)
    def start_timer(self):
        """ Ξεκίνησε τη μέτρηση του χρόνου """
        self._elapsedtime = 0.0
        self._start = time.time() - self._elapsedtime
        self._update_timer()
    def stop_timer(self):
        """ Σταμάτησε τη χρονομέτρηση """
        self.root.after_cancel(self._timer)
        self._elapsedtime = time.time() - self._start

if __name__ == '__main__' :
    root = tk.Tk()
    padx, pady = 15,15
    margin = 10
    width = 1000
    height = 600
    game = Game(root, width, height)
    root.mainloop()
