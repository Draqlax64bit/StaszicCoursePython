class Automat:
    def __init__(self):  # stan początkowy zawsze musi być
        self.gumy = 6
        self.monety = 0


    def wrzuc_monete(self):
        if self.gumy > 0:
            self.monety += 1
            self.gumy -= 1
            print('masz gume')
        else:
            print('nie mama gum')


