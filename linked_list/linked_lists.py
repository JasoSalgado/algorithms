"""
Linked lists are data structures similar than arrays or lists but, to access to the element is through a pointer

Simple linked list
It has a link by node. This link points out to the following node in the list or to the null value or None if is the last node.
"""
from .node import Node

class SimpleLinkedList():
    def __init__(self):
        self.first_node = None
        self.last_node = None


    def empty(self):
        return self.first_node == None
    

    def add_last_node(self, data):
        if self.empty:
            self.first_node = self.last_node = Node(data)
        else:
            aux = self.last_node
            self.last_node = aux.next_node = Node(data)
    

    def add_init(self, data):
        if self.empty():
            self.first_node = self.last_node = Node()
        else:
            aux = Node(data)
            aux.next_node = self.first_node
            self.first_node = aux


    def delete_last_node(self):
        aux = self.first_node
        while aux.next_node != self.last_node:
            aux = aux.next_node
        aux.next_node = None
        self.last_node = aux
    

    def delete_init(self):
        self.first_node = self.first_node.next_node
        
        
    
    def go_through(self):
        aux = self.first_node
        while aux != None:
            print(aux.data)
            aux = aux.next_node