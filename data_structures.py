"""Reusable data structures for the Python learning portfolio."""
class Stack:
    """A bounded last-in, first-out collection."""
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be greater than zero")
        self.capacity = capacity
        self._items = []
    def push(self, item):
        if self.is_full():
            raise OverflowError("stack is full")
        self._items.append(item)
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]
    def is_empty(self):
        return not self._items
    def is_full(self):
        return len(self._items) == self.capacity
    def __len__(self):
        return len(self._items)

class Queue:
    """A bounded first-in, first-out collection."""
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be greater than zero")
        self.capacity = capacity
        self._items = []
    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("queue is full")
        self._items.append(item)
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[0]
    def is_empty(self):
        return not self._items
    def is_full(self):
        return len(self._items) == self.capacity
    def __len__(self):
        return len(self._items)

class CircularQueue:
    """A bounded FIFO queue backed by a fixed-size circular buffer."""
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be greater than zero")
        self.capacity = capacity
        self._items = [None] * capacity
        self._front = 0
        self._size = 0
    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("circular queue is full")
        rear = (self._front + self._size) % self.capacity
        self._items[rear] = item
        self._size += 1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty circular queue")
        item = self._items[self._front]
        self._items[self._front] = None
        self._front = (self._front + 1) % self.capacity
        self._size -= 1
        return item
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty circular queue")
        return self._items[self._front]
    def is_empty(self):
        return self._size == 0
    def is_full(self):
        return self._size == self.capacity
    def __len__(self):
        return self._size
