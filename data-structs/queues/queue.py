# LinkedList Node
class Node:
    # Defines a new node passing in a value and next node reference
    def __init__(self, value, ref=None):
        self.value=value
        self.next=ref

# Implementation of Queue using a LinkedList
class Queue:
    def __init__(self):
        self.head=None
        self.size=0
    
    def enqueue(self, value):
        def aux(node):
            if(node.next == None):
                n = Node(value)
                node.next=n
            else:
                return aux(node.next)
        return aux(self.head)

    def dequeue(self):
        def aux(node):
            if(node.next == None):
                n=node.value
                node.next
                

    def peek(self):
        def aux(node):
            if(node.next == None):
                return node.value
            else:
                return aux(node.next)

        return aux(self.head)