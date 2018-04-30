class Point():
    ''' ένα σημείο στο καρτεσιανό επίπεδο '''
    the_points = []
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)
        Point.the_points.append(self)
    def distance(self, p):
        return ((self.x - p.x)**2 + (self.y - p.y)**2 )**0.5
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'

# main program
while True:
    command = input('Εντολή (insert x,y ή delete x,y) :')
    if command =='': break
    if len(command.split())<2: continue
    coords = command.split()[1]
    if coords.count(',') != 1: continue
    x, y = coords.split(',')
    if x.isdigit() and y.isdigit():
        if command.split()[0] == 'insert':
            new_point = Point(x,y)
            print('Υπάρχουν συνολικά {} σημεία'.format(len(Point.the_points)))
            for p in Point.the_points:
                if p != new_point:
                    print('Το σημείο {} είναι σε απόσταση {:.2f} από το σημείο'.format(p, p.distance(new_point)))
        elif command.split()[0] == 'delete':
            deleted = False
            new_points = []
            for p in Point.the_points:
                if p.x == int(x) and p.y == int(y):
                    del p
                    deleted = True
                else: new_points.append(p)
            Point.the_points = new_points
            if deleted:
                print('Τα σημεία μετά τη διαγραφή είναι:')
                for p in Point.the_points: print(p)
            else: print('δεν βρέθηκε το σημείο')