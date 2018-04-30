# κλάση Student
class Student():
    """ένα άτομο που σπουδάζει"""
    def __init__(self, name, age, origin=''):
        self.name = name
        self.age = int(age)
        self.origin = origin

    def get_age(self):
        return str(self.age) + ' χρονών'

# ορισμός αντικειμένων τύπου Student
s1 = Student('Ορέστης',22,'Βόλος')
s2 = Student('Μαρία',19,'Σπάρτη')
s3 = Student('Ζωή', 20)
s4 = Student('Κώστας', 21)
print(s1.name)
print(s1.get_age())