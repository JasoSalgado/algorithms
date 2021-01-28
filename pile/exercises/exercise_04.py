"""
Pile
"""

class Pile:
    def __init__(self, size):
        self.list = []
        self.top = 0
        self.size = size


    def empty(self):
        if self.top == 0:
            return True
        else:
            return False


    def push(self, data):
        if self.top < self.size:
            self.list += [data]
            self.top += 1
        else:
            self.size += 3
            self.list += [data]
            self.top += 1


    def pop(self):
        if self.empty():
            print("Pile is empty")
        else:
            self.top -= 1
            self.list = [self.list[x] for x in range(self.top)]


    def show(self):
        i = self.top - 1
        while i > - 1:
            print(f"{i} => {self.list[i]}")
            i -= 1


    def size(self):
        return self.top


    def top(self):
        return self.list[-1]


pile = Pile(3)

pile.push(50)
pile.push(23454)
pile.push(9876)
pile.push(4567)

pile.pop()

pile.show()
print(f"Size: => {pile.size}")
print(f"State: =>", pile.empty())
print(f"Top: => {pile.top}")
