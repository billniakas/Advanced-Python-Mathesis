class C():
    num_instances = 0

    def __init__(self):
        C.num_instances += 1

    @staticmethod
    def print_num_instances():  # μέθοδος κλάσης
        print('Πλήθος στιγμιότυπων είναι :{}'.format(C.num_instances))
    # print_num_instances = staticmethod(print_num_instances)
