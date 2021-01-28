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
            self.size += 5
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





pile = Pile(10)

pile.push(2345)
pile.push(654)
pile.push(3040)
pile.push(0000)
pile.push(1111)
pile.push(947595)
pile.push(2343567654)
pile.push(123)
pile.push(80809)
pile.push(134252452)

pile.pop()

pile.pop()

pile.show()

print(f"Size: => {pile.size}")
print(f"State: => ", pile.empty())
print(f"Top: => {pile.top}")

