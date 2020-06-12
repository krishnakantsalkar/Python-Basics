class Enemy:
    # static variable
    hp = 200

    # constructor
    def __init__(self, atk, mp):  # self ~ this // instance variables avl. during instance creation
        self.atk = atk
        self.mp = mp

    def getatk(self):
        return self.atk
