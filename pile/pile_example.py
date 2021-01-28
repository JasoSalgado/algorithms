"""
Pile:

    It is a ordered list or data structure. The way we insert data is LIFO Last In, First Out.
    To apile data we use push and to remove data we use pop.

    Functioning:
    Create: We create an empty pile (constructor).
    Size: It returns the elements of the pile.
    Pile: It adds an element to the pile (push).
    Unstack: It removes the last data from the pile (pop).
    Top: It returns the element that is on top of the pile (top or peek).
    Empty: It returns true is the pile is empty or false in case of the pile has an element (empty).

    Piles can be static and dynamic size.
"""

class Pile:
    # Constructor
    def __init__(self, size):
        # Empty list
        # Top
        # Size
        self.list = []
        self.top = 0
        self.size = size


    # Empty method
    def empty(self):
        # If top is empty (== 0) there are no elements
        if self.top == 0:
            return True
        else:
            return False


    # Push method
    def push(self, data):
        # If top is smaller than the lenth of size we can push data
        if self.top < self.size:
            self.list += [data]
            # So, we can increment in 1
            self.top += 1
        else:
            # Make it dynamic
            self.size += 5
            self.list += [data]
            self.top += 1
            #print(f"Pile is full and we cannot insert more data, because it is limited to: {self.size} data")


    def pop(self):
        # We check if out pile is empty
        if self.empty():
            print("Pile is empty")
        else:
            # Decrese the pile in 1
            self.top -= 1
            # We use list comprehensions to replace the list for the new list that we iterate
            self.list = [self.list[x] for x in range(self.top)]


    # Show data
    def show(self):
        # To show the list in a stack from index 0 to n number
        i = self.top - 1
        while i > -1:
            print(f"{i} => {self.list[i]}")
            i -= 1

    # Size data
    def size(self):
        return self.top


    # Top data
    def top(self):
        return self.list[-1]



