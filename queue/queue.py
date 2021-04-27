"""
Queue:
It a data structure characterized by being a sequence of elements where the insertion -push- operation is done end-to-end and the extraction operation -pop- is done by the other side.
This is a FIFO: First In, First Out

Operations:
- Insert
- Delete
- Search
- Queue state -empty or with elements-
- Return front size
- Return back size
"""

class Queue:

    def __init__(self):
        self.queue = []
        self.size = 0
    

    def empty(self):
        return len(self.queue) == 0
    

    def push(self, data):
        self.queue += [data]
        self.size += 1
    

    def pop(self):
        if self.empty():
            print('Empty queue')
        else:
            self.queue = [self.queue[i] for i in range(1, self.size)]
            self.size -= 1
    

    def show(self):
        n = self.size - 1
        while n > -1:
            print(f'{n} => {self.queue[n]}')
            n -= 1
    

    def front_size(self):
        if self.empty():
            print('Empty queue')
        else:
            print(f'First data: {self.queue[0]}')