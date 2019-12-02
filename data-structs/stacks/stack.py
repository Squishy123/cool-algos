# LinkedList Node
class Node:
    # Defines a new node passing in a value and next node reference
    def __init__(self, value, ref=None):
        self.value = value
        self.next = ref

# Implementation of Stack using a LinkedList
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        n = Node(value, self.head)
        self.head = n
        self.size += 1

    def peek(self):
        return self.head.value

    def pop(self):
        val = self.head.value
        self.head = self.head.next
        self.size -= 1
        return val
