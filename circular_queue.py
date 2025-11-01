

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Circular Queue Overflow!")
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = item
            print(f"{item} added to circular queue.")
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item
            print(f"{item} added to circular queue.")

    def dequeue(self):
        if self.front == -1:
            print("Circular Queue Underflow!")
        elif self.front == self.rear:
            print(f"{self.queue[self.front]} dequeued from circular queue.")
            self.front = self.rear = -1
        else:
            print(f"{self.queue[self.front]} dequeued from circular queue.")
            self.front = (self.front + 1) % self.size

    def display(self):
        if self.front == -1:
            print("Circular Queue is empty!")
        else:
            print("Circular Queue elements:")
            i = self.front
            while True:
                print(self.queue[i])
                if i == self.rear:
                    break
                i = (i + 1) % self.size

while True:
    try:
        max_size = int(input("Enter size of the circular queue: "))
        if max_size <= 0:
            print("Invalid size. Must be greater than 0.")
        else:
            break
    except ValueError:
        print("Invalid value! Please enter an integer.")

cq = CircularQueue(max_size)

while True:
    print("\n------ CIRCULAR QUEUE MENU ------")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        item = input("Enter element to enqueue: ")
        cq.enqueue(item)
    elif choice == '2':
        cq.dequeue()
    elif choice == '3':
        cq.display()
    elif choice == '4':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")
