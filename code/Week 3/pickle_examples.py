# παράδειγμα αποθήκευσης λεξικού σε pickle

import pickle  # βιβλιοθήκη pickle για μόνιμη αποθήκευση αντικειμένων


def main():
    my_dict = {'1': 'καλημέρα', (1, 2): 33.3 + 22.2j, 3: [[10, 20], [30, 40]]}
    print(my_dict)
    with open('pickle0.db', 'wb') as f:
        pickle.dump(my_dict, f)


if __name__ == '__main__': main()

# παράδειγμα ανάγνωσης λεξικού από αρχείο pickle

import pickle  # βιβλιοθήκη pickle για μόνιμη αποθήκευση αντικειμένων
import os.path  # βιβλιοθήκη για σύνδεση με λειτουργικό σύστημα


def main():
    # φορτώνουμε το λεξικό my_dict από το αρχείο pickle0.db αν υπάρχει
    if os.path.isfile('pickle0.db'):
        with open('pickle0.db', 'rb') as f:
            my_dict = pickle.load(f)
        for k, v in my_dict.items(): print(k, '\t--->', v)
    else:
        print('το αρχείο δεν υπάρχει')


if __name__ == '__main__': main()

# παράδειγμα αποθήκευσης αντικειμένων σε pickle

import pickle  # βιβλιοθήκη pickle για μόνιμη αποθήκευση αντικειμένων
import os.path  # βιβλιοθήκη για σύνδεση με λειτουργικό σύστημα


def main():
    # φορτώνουμε τα αντικείμενα από το αρχείο pickle αν υπάρχει
    if os.path.isfile('obj1.db'):
        with open('obj1.db', 'rb') as f:
            my_dict = pickle.load(f)
            print('pickle file size: {}'.format(os.path.getsize('obj1.db')))
    else:
        my_dict = {}
    print('my_dict:', my_dict)
    # βρόχος αλληλεπίδρασης με χρήστη: εισαγωγή στοιχείων λεξικού
    while True:
        command = input('δώσε κλειδί:τιμή ή [enter] ....:')
        if command == '':
            break
        elif command.count(':') == 1:
            key = command.split(':')[0].strip()
            val = command.split(':')[1].strip()
            my_dict[key] = val
    # έξοδος από το πρόγραμμα, αποθήκευση αντικειμένων σε αρχείο pickle
    print('pickling my_dict')
    with open('obj1.db', 'wb') as f:
        pickle.dump(my_dict, f)
    print('pickle file size: {}'.format(os.path.getsize('obj1.db')))


if __name__ == '__main__': main()