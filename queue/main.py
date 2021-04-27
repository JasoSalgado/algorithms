from os import system
system('clear')

from queue import Queue

queue = Queue()
queue.push(12)
queue.push(23)
queue.push(56)
queue.push(78)
queue.push(89)
queue.push(100)
queue.push(47)


queue.pop()
queue.pop()
queue.pop()
queue.show()

queue.front_size()