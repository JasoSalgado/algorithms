"""
Node: 
"""
from os import system
system('clear')


class Node():

    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    

    # def __str__(self):
    #     return str(self.data)


def go_through(node):
    while node != None:
        print(node.data)
        node = node.next


node4 = Node(12)
node3 = Node(45, node4)
node2 = Node(67, node3)
node1 = Node(89, node2)

go_through(node1)

#print(node1, node2, node3, node4)