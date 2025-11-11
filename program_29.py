class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    def show(self):
        print(f"The Vector is {self.i}i + {self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    def show(self):
        print(f"The Vector is {self.i}i + {self.j}j + {self.k}k ")
a = TwoDVector(1, 2)
b = ThreeDVector(1, 2, 3)
a.show()
b.show()